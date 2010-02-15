###############################################################################
#
# sabx10.oxm - an SABX file manipulation library
# Copyright (C) 2009, 2010 Jay Farrimond (jay@sabikerides.com)
#
# This file is part of sabx10.oxm.
#
# sabx10.oxm is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# sabx10.oxm is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with sabx10.oxm.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
"""
Ride handling.

When I'm using SABX data to create maps, I like to process the XML data into a
more useful object hierarchy.  I de-reference the parking, turn, and seg ids
for each ride and create full object hierarchies for each.  This results in
lots of duplication, but gives data that is easy to manipulate and reference.
I also do some analysis of the rides and add things like distances and bounding
boxes to the relevant objects, and modify some of the standard objects to be
more programmer-friendly.

The entry point for this is the L{process_rides} function.  It orchestrates all
the processing and calculating and returns a ride list that looks like this:

 - C{list} of L{Ride}
   - index
   - parking: L{Parking}
   - turns: C{list} of L{Turn}
   - segs: C{list} of L{Segment}
     - C{list} of L{Waypoint}
   - stops: C{list} of L{Stop}
   - pois: C{list} of L{Poi}
   - combined: distance sorted C{list} of all turns, segments, stops, and pois
   - bounds: C{Box}
   - distance (length of ride)

Make note of the fact that all C{comment} and C{description} fields are
stripped of extra spaces and linefeeds during processing.
"""
from geom import Box
from utils import check_version
from parking import process_ride_parking
from segment import process_ride_segments
from stop import process_ride_stops
from poi import process_ride_pois
from turn import process_ride_turns

############################################################
# XML
############################################################

class Ride(object):
    """
    A C{Ride} object describes a ride and keeps track of all relevant ride
    information.  This information can vary depending on what created the ride.
    If it was created by parsing XML, then parking, turn list, and segment list
    are the id's of the relevant items.  If this was created while processing a
    ride, then parking, turn list, and segment list are L{Parking}, L{Turn},
    and L{Segment} objects instead.  The contents can therefore be infered from
    context.

    @ivar id: id of ride
    @type id: C{string}
    @ivar description: description of ride
    @type description: C{string}
    @ivar parking: C{id} of parking place for ride or L{Parking} object
    @type parking: C{string} or L{Parking}
    @ivar turns: C{list} of turn C{id}s or L{Turn} objects
    @type turns: C{list} of C{string} or L{Turn}
    @ivar segments: C{list} of segment C{id}s or L{Segment} objects
    @type segments: C{list} of C{string} or L{Segment}
    """
    def __init__(self, id, description, parking, turns, segs):
        """
        Save the passed-in information.

        @param id: id of ride
        @type id: C{string}
        @param description: description of ride
        @type description: C{string}
        @param parking: C{id} of parking place for ride or L{Parking} object
        @type parking: C{string} or L{Parking}
        @param turns: C{list} of turn C{id}s or L{Turn} objects
        @type turns: C{list} of C{string} or L{Turn}
        @param segs: C{list} of segment C{id}s or L{Segment} objects
        @type segs: C{list} of C{string} or L{Segment}
        """
        self.id = id
        self.description = description
        self.parking = parking
        self.turns = turns
        self.segs = segs

def _parse_ride_parking(xml_ride):
    """
    Take the C{Element} for a ride and extract the parking id for the ride.

    @param xml_ride: C{Element} for a ride
    @type xml_ride: C{Element}

    @return: parking id
    @rtype: C{string}
    """
    xml_parking = xml_ride.find('parking_ref')
    return xml_parking.attrib['id']

def _parse_ride_turns(xml_ride):
    """
    Take the C{Element} for a ride and extract the turn id's for the ride.

    @param xml_ride: C{Element} for a ride
    @type xml_ride: C{Element}

    @return: C{list} of turn id's
    @rtype: C{list} of C{string}
    """
    return [xml_turn.attrib['id'] for xml_turn in xml_ride.findall('turn_ref')]

def _parse_ride_segments(xml_ride):
    """
    Take the C{Element} for a ride and extract the segment id's for the ride.

    @param xml_ride: C{Element} for a ride
    @type xml_ride: C{Element}

    @return: C{list} of segment id's
    @rtype: C{list} of C{string}
    """
    return [xml_seg.attrib['id'] for xml_seg in xml_ride.findall('segment_ref')]

def _parse_ride_xml(xml_ride):
    """
    Take the C{Element} for a ride and turn it into a L{Ride} object. This
    L{Ride} object will be populated with lists of C{string} id's for the
    parking, turns, and segs of the ride.

    @param xml_ride: C{Element} for a ride
    @type xml_ride: C{Element}

    @return: L{Ride} object
    @rtype: L{Ride}
    """
    return Ride(id = xml_ride.attrib['id'], 
                description = xml_ride.findtext('description'),
                parking = _parse_ride_parking(xml_ride), 
                turns = _parse_ride_turns(xml_ride),
                segs = _parse_ride_segments(xml_ride))

def parse_rides(xml_tree):
    """
    Parse the rides in the given XML tree and turn them into valid L{Ride}
    objects.

    @param xml_tree: root of C{Element} tree that has rides in it
    @type xml_tree: C{Element} or C{ElementTree}

    @return: rides in a list and a dictionary
    @rtype: (C{list} of L{Ride},C{dict} of L{Ride})
    """
    xml_rides = xml_tree.findall('ride')
    ride_list = []
    ride_dict = {}
    for xml_ride in xml_rides:
        new_ride = _parse_ride_xml(xml_ride)
        ride_list.append(new_ride)
        ride_dict[new_ride.id] = new_ride

    return ride_list, ride_dict

############################################################
# RIDES
############################################################

def _create_combined_list(ride):
    """
    Create a list containing all of the turns, segments, stops, and pois for
    the ride, ordered by distance into ride.

    @param ride: C{Ride} to process
    @type ride: C{Ride}

    @return: combined C{list}
    @rtype: C{list}
    """
    combined = []
    combined.extend(ride.turns)
    combined.extend(ride.segs)
    combined.extend(ride.stops)
    combined.extend(ride.pois)
    combined.sort(key=lambda x: x.distance)
    return combined

def _process_bounds(ride, seg_bounds, stop_bounds, poi_bounds):
    """
    Creating a bounding box that includes the bounds for the parking, segments,
    stops, and pois for this ride.

    @param ride: C{Ride} to process
    @type ride: C{Ride}
    @param seg_bounds: bounding C{Box} for segments
    @type seg_bounds: C{Box}
    @param stop_bounds: bounding C{Box} for stops
    @type stop_bounds: C{Box}
    @param poi_bounds: bounding C{Box} for pois
    @type poi_bounds: C{Box}

    @return: bounding box containing everything
    @rtype: L{Box}
    """
    bounds = Box()
    bounds.expand_to_point(ride.parking.lat, ride.parking.lon)
    bounds.expand_to_box(seg_bounds)
    bounds.expand_to_box(stop_bounds)
    bounds.expand_to_box(poi_bounds)
    return bounds

def _process_ride(ride_index, xml_ride, xml_parking_places, xml_segs, 
                  xml_turns, xml_stops, xml_pois, correct_ele=True):
    """
    Create a L{Ride} object and add pertinent calculated data.

    Calculated data includes:
      - index: index of ride
      - stops: C{list} of L{Stop}s for this ride
      - pois: C{list} of L{Poi}s for this ride
      - combined: distance sorted list of all turns, segments, stops, and pois
      - distance: length of entire ride
      - bounds: bounding box including all parking, segments, stops, and pois

    @param ride_index: index for this ride
    @type ride_index: C{int}
    @param xml_ride: C{Element} for a ride
    @type xml_ride: C{Element}
    @param xml_parking_places: C{list} of parking place C{Element}s
    @type xml_parking_places: C{list} of C{Element}
    @param xml_segs: C{list} of segment C{Element}s
    @type xml_segs: C{list} of C{Element}
    @param xml_turns: C{list} of turn C{Element}s
    @type xml_turns: C{list} of C{Element}
    @param xml_stops: C{list} of stop C{Element}s
    @type xml_stops: C{list} of C{Element}
    @param xml_pois: C{list} of poi C{Element}s
    @type xml_pois: C{list} of C{Element}
    @param correct_ele: make sure that the segment elevations match-up?
    @type correct_ele: C{boolean}

    @return: L{Ride}
    @rtype: L{Ride}
    """
    parking = process_ride_parking(xml_ride, xml_parking_places)
    segs, seg_bounds = process_ride_segments(xml_ride, xml_segs, correct_ele)
    stops, stop_bounds = process_ride_stops(segs, xml_segs, xml_stops)
    pois, poi_bounds = process_ride_pois(segs, xml_segs, xml_pois)
    turns = process_ride_turns(segs, xml_ride, xml_turns)
    
    new_ride = Ride(ride_index, xml_ride.findtext('description'), 
                    parking, turns, segs)
    new_ride.index = ride_index
    new_ride.stops = stops
    new_ride.pois = pois
    new_ride.combined = _create_combined_list(new_ride)
    new_ride.distance = new_ride.segs[-1].end_dist
    new_ride.bounds = _process_bounds(new_ride, seg_bounds, 
                                      stop_bounds, poi_bounds)

    return new_ride

def process_rides(xml_tree, correct_ele=True):
    """
    Process the rides in the XML tree and generate a list of L{Ride} objects
    and the bounding box for all of the rides.

    @param xml_tree: root of C{Element} tree that has rides in it
    @type xml_tree: C{Element} or C{ElementTree}
    @param correct_ele: make sure that the segment elevations match-up?
    @type correct_ele: C{boolean}

    @return: (C{list} of L{Ride}s,C{bounds} of ride)
    @rtype: (C{list} of L{Ride},L{Box})
    """
    check_version(xml_tree)
    xml_rides = xml_tree.findall('ride')
    xml_parking_places = xml_tree.findall('parking')
    xml_segs = xml_tree.findall('segment')
    xml_turns = xml_tree.findall('turn')
    xml_stops = xml_tree.findall('stop')
    xml_pois = xml_tree.findall('poi')

    bounds = Box()
    ride_list = []
    for ride_index, xml_ride in enumerate(xml_rides):
        new_ride = _process_ride(ride_index, xml_ride, xml_parking_places, 
                                 xml_segs, xml_turns, xml_stops, xml_pois,
                                 correct_ele)
        bounds.expand_to_box(new_ride.bounds)
        ride_list.append(new_ride)

    return ride_list, bounds
