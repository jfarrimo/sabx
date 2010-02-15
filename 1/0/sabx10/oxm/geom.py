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
All the geometric objects needed to represent an SABX file.
"""
from utils import calculate_distance, pt_dist_from_pt, meter_feet

class Point(object):
    """ 
    A C{Point} object is a (C{lat},C{lon}) pair that can optionally have 
    elevations and an id.

    @ivar id: id of point
    @type id: C{string}
    @ivar lat: decimal degrees
    @type lat: C{float}
    @ivar lon: decimal degrees (west is negative)
    @type lon: C{float}
    @ivar usgs: USGS elevation for this point (meters above see level)
    @type usgs: C{float}
    @ivar ele: observed elevation for this point (meters above see level)
    @type ele: C{float}
    """

    def __init__(self, lat=0.0, lon=0.0, ele=None, usgs=None, id=None):
        """ 
        Save the passed-in data and make sure elevations are filled-in
        properly.

        This class is agnostic about what units C{ele} and C{usgs} are supplied
        in, but SABX specifies them as meters.

        @param id: id of point
        @type id: C{string}
        @param lat: degrees
        @type lat: C{float}
        @param lon: degrees (west is negative)
        @type lon: C{float}
        @param usgs: USGS elevation for this point (meters above see level)
        @type usgs: C{float}
        @param ele: observed elevation for this point (meters above see level)
        @type ele: C{float}
        """
        self.id = id
        if lat:
            self.lat = float(lat)
        else:
            self.lat = 0.0
        if lon:
            self.lon = float(lon)
        else:
            self.lon = 0.0

        self.usgs = None
        self.ele = None
        if usgs is not None:
            self.usgs = float(usgs)
            self.ele = self.usgs
        if ele is not None:
            self.ele = float(ele)

    def calculate_distance(self, point):
        """ 
        Calculate the distance from this point to the given point,
        in statue miles. 

        @param point: point to calculate distance to
        @type point: L{Point}

        @return: distance in statute miles
        @rtype: C{float}
        """
        if point is self:
            return 0.0

        return calculate_distance(self.lat, self.lon, point.lat, point.lon)

    def pt_dist_from(self, distance, true_course):
        """ 
        Calculate a point C{distance} statute miles from this point
        along a course C{true_course} degrees

        Some useful C{true_course} values:
          - 0.0 - north
          - 90.0 - east
          - 180.0 - south
          - 270.0 - west

        @param distance: distance from this point in statute miles
        @type distance: C{float}
        @param true_course: true course from this point in degrees
        @type true_course: C{float}

        @return: Point object representing calculated point
        @rtype: L{Point}
        """
        return pt_dist_from_pt(self.lat, self.lon, distance, true_course)

def _pt_pairs(pts):
    pt_from = pts[0]
    for pt_to in pts[1:]:
        yield pt_from, pt_to
        pt_from = pt_to

class Line(object):
    """ 
    A C{Line} object is an ordered set of L{Point} objects 
    representing a line.

    @ivar waypoints: list of L{Point} objects
    @type waypoints: C{list}
    """

    def __init__(self, waypoints):
        """
        Save the passed-in data.

        @param waypoints: list of L{Point} objects
        @type waypoints: C{list}
        """
        self.waypoints = waypoints

    def calc_length(self):
        """ 
        Calculate the length of this C{line} in statue miles.

        @return: length in statute miles
        @rtype: C{float}
        """
        length = 0.0
        for pt_from, pt_to in _pt_pairs(self.waypoints):
            length += pt_from.calculate_distance(pt_to)
        return length

    def find_lowest_highest(self):
        """ 
        Discover the lowest and highest elevations of this C{line}.

        @return: (C{lowest},C{highest}) in feet
        @rtype: (C{float},C{float})
        """
        highest = 0.0
        lowest = 20000.0
        for point in self.waypoints:
            highest = max(highest, point.ele)
            lowest = min(lowest, point.ele)
        return lowest * meter_feet, highest * meter_feet

def _between(check, left, right):
    if (check > left and check < right) or \
            (check > right and check < left):
        return True
    return False

class Box(object):
    """ 
    A rectangle, represented by bottom left and top right corners.

    @ivar min_lat: minimum latitude (bottom edge in northern hemisphere)
    @type min_lat: C{float}
    @ivar min_lon: minimum longitude (left edge in western hemisphere)
    @type min_lon: C{float}
    @ivar max_lat: maximum latitude (top edge in northern hemisphere)
    @type max_lat: C{float}
    @ivar max_lon: maximum longitude (right edge in western hemisphere)
    @type max_lon: C{float}
    """

    def __init__(self, min_lat=200.0, min_lon=200.0, 
                 max_lat=-200.0, max_lon=-200.0):
        """
        Save the passed-in data.

        @param min_lat: minimum latitude (bottom edge in northern hemisphere)
        @type min_lat: C{float}
        @param min_lon: minimum longitude (left edge in western hemisphere)
        @type min_lon: C{float}
        @param max_lat: maximum latitude (top edge in northern hemisphere)
        @type max_lat: C{float}
        @param max_lon: maximum longitude (right edge in western hemisphere)
        @type max_lon: C{float}
        """
        self.min_lat = float(min_lat)
        self.min_lon = float(min_lon)
        self.max_lat = float(max_lat)
        self.max_lon = float(max_lon)

    def width(self):
        """ 
        Calculate the width, in statue miles.

        @return: width, in statute miles
        @rtype: C{float}
        """
        return calculate_distance(self.min_lat, self.min_lon, 
                                  self.min_lat, self.max_lon)

    def height(self):
        """ 
        Calculate the height, in statue miles.

        @return: height, in statute miles
        @rtype: C{float}
        """
        return calculate_distance(self.min_lat, self.min_lon,
                                  self.max_lat, self.min_lon)

    def area(self):
        """ 
        Calculate the area, in square statue miles.

        @return: area, in square miles
        @rtype: C{float}
        """
        return self.width() * self.height()

    def is_pt_in_box(self, lat, lon):
        """ 
        Is the point (C{lat},C{lon}) in this box? 

        @param lat: latitude
        @type lat: C{float}
        @param lon: longitude
        @type lon: C{float}

        @return: C{True} or C{False}
        @rtype: C{boolean}
        """
        lat = float(lat)
        lon = float(lon)
        if _between(lat, self.min_lat, self.max_lat) and \
                _between(lon, self.min_lon, self.max_lon):
            return True
        return False

    def resize(self, new_width, new_height):
        """ 
        Redo the corner points of this box to reflect new C{width} and 
        C{height}, maintaining the same center point as this box currently 
        has.

        @param new_width: new width of box
        @type new_width: C{float}
        @param new_height: new height of box
        @type new_height: C{float}
        """
        mid_lat = (self.min_lat + self.max_lat) / 2.0
        mid_lon = (self.min_lon + self.max_lon) / 2.0
        
        dist = new_height / 2.0
        self.min_lat, lon = pt_dist_from_pt(mid_lat, mid_lon, dist, 180) # down
        self.max_lat, lon = pt_dist_from_pt(mid_lat, mid_lon, dist, 0) # up

        dist = new_width / 2.0
        lat, self.min_lon = pt_dist_from_pt(mid_lat, mid_lon, dist, 270) # left
        lat, self.max_lon = pt_dist_from_pt(mid_lat, mid_lon, dist, 90) # right

    def expand_to_point(self, lat, lon):
        """ 
        Expand this box to include the point (C{lat},C{lon}).

        @param lat: latitude of point to include
        @type lat: C{float}
        @param lon: longitude of point to include
        @type lon: C{float}
        """
        lat = float(lat)
        lon = float(lon)
        self.min_lat = min(self.min_lat, lat)
        self.min_lon = min(self.min_lon, lon)
        self.max_lat = max(self.max_lat, lat)
        self.max_lon = max(self.max_lon, lon)

    def expand_to_box(self, box):
        """ 
        Expand this box to include the corners of the given box.

        @param box: box to expand to
        @type box: L{Box}
        """
        self.min_lat = min(self.min_lat, box.min_lat)
        self.min_lon = min(self.min_lon, box.min_lon)
        self.max_lat = max(self.max_lat, box.max_lat)
        self.max_lon = max(self.max_lon, box.max_lon)
