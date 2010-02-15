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
Stop handling.
"""
from geom import Point, Box
from utils import get_from_id

############################################################
# XML
############################################################

class Stop(Point):
    """
    A C{Stop} object sub-classes L{Point} and adds a description and type to
    describe a stop.

    @ivar type: type of stop
    @type type: C{string}
    @ivar description: description of the stop
    @type description: C{string}
    """
    def __init__(self, id, type, description, lat, lon):
        """
        Save the passed-in data.

        @param id: id of the stop
        @type id: C{string}
        @param type: type of stop (convenience store, restaurant, etc...)
        @type type: C{string}
        @param description: description of the stop
        @type description: C{string}
        @param lat: latitude of the stop
        @type lat: C{float}
        @param lon: longitude of the stop
        @type lon: C{float}
        """
        Point.__init__(self, lat, lon, id=id)
        self.type = type
        self.description = description

def _parse_stop_xml(xml_stop):
    """
    Take the C{Element} for a stop and turn it into a L{Stop} object.

    @param xml_stop: C{Element} for a stop
    @type xml_stop: C{Element}

    @return: L{Stop} object
    @rtype: L{Stop}
    """
    return Stop(id = xml_stop.attrib['id'], 
                type = xml_stop.findtext('type'),
                description = xml_stop.findtext('description'), 
                lat = xml_stop.findtext('lat'),
                lon = xml_stop.findtext('lon'))

def parse_stops(xml_tree):
    """
    Get all the stop elements in the given C{Element} tree and create a list of
    them with L{Stop} objects.

    @param xml_tree: root of C{Element} tree that has stops in it
    @type xml_tree: C{Element} or C{ElementTree}

    @return: stops in a list and a dictionary
    @rtype: (C{list} of L{Stop},C{dict} of L{Stop})
    """
    xml_stops = xml_tree.findall('stop')
    stop_list = []
    stop_dict = {}
    for xml_stop in xml_stops:
        new_stop = _parse_stop_xml(xml_stop)
        stop_list.append(new_stop)
        stop_dict[new_stop.id] = new_stop        

    return stop_list, stop_dict

############################################################
# RIDES
############################################################

def _stop_pts_dist(points):
    """
    Generator that iterates through all the L{Point} objects, yielding the
    point and the distance to it along the line for each point.

    @param points: list of points for a segment
    @type points: C{list} of L{Point} objects

    @return: (L{Point},distance)
    @rtype: (L{Point},C{float})
    """
    dist = 0.0
    for index in range(len(points)-1):
        yield points[index], dist
        dist += points[index].calculate_distance(points[index+1])
    yield points[-1], dist

def _process_stops_in_seg_data(ride_seg, xml_stops, index):
    """
    Process the segment, extracting the stops and getting the bounds of the
    stops.

    @param ride_seg: L{Segment} to process
    @type ride_seg: L{Segment}
    @param xml_stops: C{list} of C{Element}s for stops in rideset
    @type xml_stops: C{list} of C{Element}
    @param index: next index to use for a stop
    @type index: C{int}

    @return: (stops for segment, bounds, updated index)
    @rtype: (C{list} of L{Stop},L{Box},C{int})
    """
    seg_stops = []
    bounds = Box()
    for waypoint, dist in _stop_pts_dist(ride_seg.waypoints):
        if waypoint.stop is not None:
            stop_list = waypoint.stop.split()
            for stop_item in stop_list:
                xml_stop = get_from_id(xml_stops, stop_item.strip())

                new_stop = _parse_stop_xml(xml_stop)
                new_stop.description = " ".join(new_stop.description.split())
                new_stop.distance = ride_seg.start_dist + dist
                new_stop.off_route = new_stop.calculate_distance(waypoint)
                new_stop.index = index
                index += 1

                seg_stops.append(new_stop)
                bounds.expand_to_point(new_stop.lat, new_stop.lon)

    return seg_stops, bounds, index

def process_ride_stops(seg_set, xml_segs, xml_stops):
    """
    Process the stop references for the given ride and generate a list of
    L{Stop} objects for it and the bounding box for all of the stops.

    @param seg_set: C{list} of L{Segment} objects for the ride
    @type seg_set: C{list} of L{Segment} objects
    @param xml_segs: C{list} of C{Element} segment objects for this ride
    @type xml_segs: C{list} of C{Element}s
    @param xml_stops: C{list} of C{Element} stop objects
    @type xml_stops: C{list} of C{Element}s

    @return: (C{list} of L{Stop},C{bounds})
    @rtype: (C{list},L{Box})
    """
    index = 1
    stop_list = []
    bounds = Box()
    for ride_seg in seg_set:
        new_stops, new_bounds, index = \
            _process_stops_in_seg_data(ride_seg, xml_stops, index)
        stop_list.extend(new_stops)
        bounds.expand_to_box(new_bounds)

    return stop_list, bounds
