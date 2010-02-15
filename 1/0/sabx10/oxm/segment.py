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
Segment handling.
"""
from geom import Point, Line, Box
from utils import get_from_id, check_version

############################################################
# XML
############################################################

class Waypoint(Point):
    """
    A C{Waypoint} object sub-classes L{Point} and adds stop and POI references.

    @ivar stop: space-delimited list of stop id's for this waypoint
    @type stop: C{string}
    @ivar poi: space-delimited list of poi id's for this waypoint
    @type poi: C{string}
    """
    def __init__(self, id, stop, poi, lat, lon, ele, usgs):
        """
        Save the passed-in data.

        @param id: id of the C{Waypoint}
        @type id: C{string}
        @param stop: space-delimited list of stop id's for this waypoint
        @type stop: C{string}
        @param poi: space-delimited list of poi id's for this waypoint
        @type poi: C{string}
        @param lat: latitude of the waypoint
        @type lat: C{float}
        @param lon: longitude of the waypoint
        @type lon: C{float}
        @param ele: observed elevation for this waypoint (meters above 
        sea level)
        @type ele: C{float}
        @param usgs: USGS elevation for this waypoint (meters above sea level)
        @type usgs: C{float}
        """
        Point.__init__(self, lat, lon, ele, usgs, id)
        self.stop = stop
        self.poi = poi

    def dup_point_data(self):
        """
        Create a new C{Waypoint} with the same data as this one.

        @return: duplicate C{Waypoint}
        @rtype: C{Waypoint}
        """
        return Waypoint(self.id, None, None, 
                        self.lat, self.lon, self.ele, self.usgs)

class Segment(Line):
    """
    A C{Segment} object sub-classes L{Line} and adds a host of extra data.

    @ivar id: id of the C{Segment}
    @type id: C{string}
    @ivar road: name of road for this C{Segment}
    @type road: C{string}
    @ivar fromto: SEGMENT_X to SEGMENT_Y
    @type fromto: C{string}
    @ivar comments: Extra information about this C{Segment}
    @type comments: C{string}
    @ivar lanes: number of lanes
    @type lanes: C{string}
    @ivar shoulder: width of shoulder
    @type shoulder: C{string}
    @ivar traffic: amount of traffic
    @type traffic: C{string}
    @ivar speed: speed limit
    @type speed: C{string}
    """
    def __init__(self, id, road, fromto, comments, 
                 lanes, shoulder, traffic, speed, waypoints):
        """
        Save the passed-in data.

        @param id: id of the C{Segment}
        @type id: C{string}
        @param road: name of road for this C{Segment}
        @type road: C{string}
        @param fromto: SEGMENT_X to SEGMENT_Y
        @type fromto: C{string}
        @param comments: Extra information about this C{Segment}
        @type comments: C{string}
        @param lanes: number of lanes
        @type lanes: C{string}
        @param shoulder: width of shoulder
        @type shoulder: C{string}
        @param traffic: amount of traffic
        @type traffic: C{string}
        @param speed: speed limit
        @type speed: C{string}
        """
        Line.__init__(self, waypoints)
        self.id = id
        self.road = road
        self.fromto = fromto
        self.comments = comments
        self.lanes = lanes
        self.shoulder = shoulder
        self.traffic = traffic
        self.speed = speed

def _parse_waypoint(xml_point):
    """
    Take the C{Element} for a waypoint and turn it into a L{Waypoint} object.

    @param xml_point: C{Element} for a waypoint
    @type xml_point: C{Element}

    @return: L{Waypoint} object
    @rtype: L{Waypoint}
    """
    stop = None
    if 'stop' in xml_point.attrib:
        stop = xml_point.attrib['stop']
    poi = None
    if 'poi' in xml_point.attrib:
        poi = xml_point.attrib['poi']
    return Waypoint(id = xml_point.attrib['id'], 
                    stop = stop, 
                    poi = poi,
                    lat = xml_point.findtext('lat'), 
                    lon = xml_point.findtext('lon'),
                    ele = xml_point.findtext('ele'), 
                    usgs = xml_point.findtext('usgs'))

def _parse_segment_waypoints(xml_seg):
    """
    Take the C{Element} for a segment and parse all the waypoints it contains.

    @param xml_seg: C{Element} for a segment
    @type xml_seg: C{Element}

    @return: C{list} of L{Waypoint} objects
    @rtype: C{list} of L{Waypoint}
    """
    return [_parse_waypoint(xml_pt) 
            for xml_pt in xml_seg.findall('waypoint')]

def _parse_segment_xml(xml_seg):
    """
    Take the C{Element} for a segment and turn it into a L{Segment} object.

    @param xml_seg: C{Element} for a segment
    @type xml_seg: C{Element}

    @return: L{Segment} object
    @rtype: L{Segment}
    """
    return Segment(id = xml_seg.attrib['id'], 
                   road = xml_seg.findtext('road'), 
                   fromto = xml_seg.findtext('fromto'), 
                   comments = xml_seg.findtext('comments'),
                   lanes = xml_seg.findtext('lanes'), 
                   shoulder = xml_seg.findtext('shoulder'),
                   traffic = xml_seg.findtext('traffic'), 
                   speed = xml_seg.findtext('speed'), 
                   waypoints = _parse_segment_waypoints(xml_seg))

def parse_segments(xml_tree):
    """
    Get all the segment elements in the given C{Element} tree and create a list
    of them with L{Segment} objects.

    @param xml_tree: root of C{Element} tree that has segments in it
    @type xml_tree: C{Element} or C{ElementTree}

    @return: segments in a list and a dictionary
    @rtype: (C{list} of L{Segment},C{dict} of L{Segment})
    """
    xml_segs = xml_tree.findall('segment')
    seg_list = []
    seg_dict = {}
    for xml_seg in xml_segs:
        new_seg = _parse_segment_xml(xml_seg)
        seg_list.append(new_seg)
        seg_dict[new_seg.id] = new_seg

    return seg_list, seg_dict

############################################################
# RIDE
############################################################

def _get_ride_segs(xml_ride, xml_segs):
    """
    Process the ride, creating L{Segment} objects for each of its segment
    references.

    @param xml_ride: C{Element} for a ride
    @type xml_ride: C{Element}
    @param xml_segs: C{list} of C{Element} segment objects for this rideset
    @type xml_segs: C{list} of C{Element}s

    @return: C{list} of L{Segment} objects
    @rtype: C{list} of L{Segment}
    """
    return [_parse_segment_xml(get_from_id(xml_segs, seg.attrib['id']))
            for seg in xml_ride.findall('segment_ref')]

def _correct_points(points, correction):
    """
    Apply an elevation correction to all the points in a list of waypoints.

    @param points: list of points to correct
    @type points: C{list} of L{Waypoint}
    @param correction: ammount to add to the L{Waypoint} elevations
    @type correction: C{float}

    @return: C{None}
    @rtype: C{None}
    """
    for pt in points:
        pt.ele += correction

def _correct_elevations(ride_segs):
    """
    Process the ride segments, making sure that the rise/fall between segment
    C{ele} endpoints is the same as the rise/fall of the USGS data.  This helps
    things out because C{ele} data taken from different rides can be off from
    eachother, though the relative data for the ride is correct.  This can make
    for sudden jumps in the elevation between segments, which makes for funny
    looking graphs and elevation analysis.

    @param ride_segs: C{list} of L{Segment} objects for the ride
    @type ride_segs: C{list} of L{Segment}

    @return: C{None}
    @rtype: C{None}
    """
    correction = 0.0
    for index in range(len(ride_segs)-1):
        usgs_rise = ride_segs[index+1].waypoints[0].usgs - \
            ride_segs[index].waypoints[-1].usgs
        ele_rise = ride_segs[index+1].waypoints[0].ele - \
            ride_segs[index].waypoints[-1].ele
        _correct_points(ride_segs[index].waypoints, correction)
        correction += usgs_rise - ele_rise
    _correct_points(ride_segs[-1].waypoints, correction)

def _connect_segments_to_following_segment(ride_segs):
    """
    Process the ride segments, connecting each to the successive segment by
    making the final point of each segment be the same as the first point of
    the following segment.

    @param ride_segs: C{list} of L{Segment} objects for the ride
    @type ride_segs: C{list} of L{Segment}

    @return: C{None}
    @rtype: C{None}
    """
    for index in range(len(ride_segs)-1):
        ride_segs[index].waypoints.append(
            ride_segs[index+1].waypoints[0].dup_point_data())

def _process_segment(seg, index, cum_distance):
    """
    Process a L{Segment}, adding pertinent calculated data.

    Calculated data includes:
      - length: of segment
      - distance: in ride of start of segment
      - start_dist: same as distance
      - end_dist: distance in ride of end of segment
      - mid_index: index of middle L{Waypoint}
      - lat: latitude of starting L{Waypoint}
      - lon: longitude of starting L{Waypoint}
      - mid_lat: latitude of middle L{Waypoint}
      - mid_lon: longitude of middle L{Waypoint}
      - index: index of segment in ride
      - bounds: bounding box for all L{Waypoint}s in the box

    @param seg: L{Segment} to process
    @type seg: L{Segment}
    @param index: index for this segment
    @type index: C{int}
    @param cum_distance: distance so far for this ride
    @type cum_distance: C{float}

    @return: C{None}
    @rtype: C{None}
    """
    seg.length = seg.calc_length()
    seg.distance = cum_distance
    seg.start_dist = cum_distance
    seg.end_dist = cum_distance + seg.length
    seg.comments = " ".join(seg.comments.split())

    mid_index = (len(seg.waypoints) - 1) / 2
    seg.lat = seg.waypoints[0].lat
    seg.lon = seg.waypoints[0].lon
    seg.mid_lat = seg.waypoints[mid_index].lat
    seg.mid_lon = seg.waypoints[mid_index].lon

    seg.index = index

    seg.bounds = Box()
    for pt in seg.waypoints:
        seg.bounds.expand_to_point(pt.lat, pt.lon)

def process_ride_segments(xml_ride, xml_segs, correct_ele=True):
    """
    Process the segment references for the given ride and generate a list of
    L{Segment} objects for it and the bounding box for all of the segments.

    @param xml_ride: C{Element} for a ride
    @type xml_ride: C{Element}
    @param xml_segs: C{list} of C{Element} segment objects for this rideset
    @type xml_segs: C{list} of C{Element}s
    @param correct_ele: make sure that the segment elevations match-up?
    @type correct_ele: C{boolean}

    @return: (C{list} of L{Segment},C{bounds})
    @rtype: (C{list},L{Box})
    """
    """ Process the segments in the ride. """
    cum_distance = 0.0
    bounds = Box()

    ride_segs = _get_ride_segs(xml_ride, xml_segs)
    if correct_ele:
        _correct_elevations(ride_segs)
    _connect_segments_to_following_segment(ride_segs)
    for index, seg in enumerate(ride_segs):
        _process_segment(seg, index, cum_distance)
        cum_distance += seg.length
        bounds.expand_to_box(seg.bounds)

    return ride_segs, bounds
