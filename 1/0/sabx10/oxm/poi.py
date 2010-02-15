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
POI handling.
"""
from geom import Point, Box
from utils import get_from_id

############################################################
# XML
############################################################

class Poi(Point):
    """
    A C{Poi} object sub-classes L{Point} and adds a description to describe a
    point of interest.

    @ivar description: description of the point of interest
    @type description: C{string}
    """
    def __init__(self, id, description, lat, lon):
        """
        Save the passed-in data.

        @param id: id of the point of interest
        @type id: C{string}
        @param description: description of the point of interest
        @type description: C{string}
        @param lat: latitude of point of interest
        @type lat: C{float}
        @param lon: longitude of point of interest
        @type lon: C{float}
        """
        Point.__init__(self, lat, lon, id=id)
        self.description = description

def _parse_poi_xml(xml_poi):
    """
    Take the C{Element} for a point of interest and turn it into a L{Poi}
    object.

    @param xml_poi: C{Element} for a point of interest
    @type xml_poi: C{Element}

    @return: L{Poi} object
    @rtype: L{Poi}
    """
    return Poi(id = xml_poi.attrib['id'], 
               description = xml_poi.findtext('description'),
               lat = xml_poi.findtext('lat'), 
               lon = xml_poi.findtext('lon'))

def parse_pois(xml_tree):
    """
    Get all the point of interest elements in the given C{Element} tree and
    create a list of them with L{Poi} objects.

    @param xml_tree: root of C{Element} tree that has points of interest in it
    @type xml_tree: C{Element} or C{ElementTree}

    @return: points of interest in a list and a dictionary
    @rtype: (C{list} of L{Poi},C{dict} of L{Poi})
    """
    xml_pois = xml_tree.findall('poi')
    poi_list = []
    poi_dict = {}
    for xml_poi in xml_pois:
        new_poi = _parse_poi_xml(xml_poi)
        poi_list.append(new_poi)
        poi_dict[new_poi.id] = new_poi

    return poi_list, poi_dict

############################################################
# RIDES
############################################################

def _poi_pts_dist(points):
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

def _process_pois_in_seg_data(ride_seg, xml_pois, index):
    """
    Process the segment, extracting the POIs and getting the bounds of the
    POIs.

    @param ride_seg: L{Segment} to process
    @type ride_seg: L{Segment}
    @param xml_pois: C{list} of C{Element}s for POIs in rideset
    @type xml_pois: C{list} of C{Element}
    @param index: next index to use for a POI
    @type index: C{int}

    @return: (POIs for segment, bounds, updated index)
    @rtype: (C{list} of L{Poi},L{Box},C{int})
    """
    seg_pois = []
    bounds = Box()
    for waypoint, dist in _poi_pts_dist(ride_seg.waypoints):
        if waypoint.poi is not None:
            poi_list = waypoint.poi.split()
            for poi_item in poi_list:
                xml_poi = get_from_id(xml_pois, poi_item.strip())

                new_poi = _parse_poi_xml(xml_poi)
                new_poi.description = " ".join(new_poi.description.split())
                new_poi.distance = ride_seg.start_dist + dist
                new_poi.off_route = new_poi.calculate_distance(waypoint)
                new_poi.index = index
                index += 1

                seg_pois.append(new_poi)
                bounds.expand_to_point(new_poi.lat, new_poi.lon)

    return seg_pois, bounds, index

def process_ride_pois(seg_set, xml_segs, xml_pois):
    """
    Process the point of interest references for the given ride and generate a
    list of L{Poi} objects for it and the bounding box for all of the POIs.

    @param seg_set: C{list} of L{Segment} objects for the ride
    @type seg_set: C{list} of L{Segment} objects
    @param xml_segs: C{list} of C{Element} segment objects for this ride
    @type xml_segs: C{list} of C{Element}s
    @param xml_pois: C{list} of C{Element} point of interest objects
    @type xml_pois: C{list} of C{Element}s

    @return: (C{list} of L{Poi},C{bounds})
    @rtype: (C{list},L{Box})
    """
    index = 1
    poi_list = []
    bounds = Box()
    for ride_seg in seg_set:
        new_pois, new_bounds, index = \
            _process_pois_in_seg_data(ride_seg, xml_pois, index)
        poi_list.extend(new_pois)
        bounds.expand_to_box(new_bounds)

    return poi_list, bounds
