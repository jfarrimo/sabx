###############################################################################
#
# sabx10 - an SABX file manipulation library
# Copyright (C) 2009, 2010 Jay Farrimond (jay@sabikerides.com)
#
# This file is part of sabx10.
#
# sabx10 is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# sabx10 is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# sabx10.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
"""
Process elevation data for an SABX ride.
"""
import math

from sabx10.oxm import mile_feet, meter_feet

from consts import CLIMB_COUNT

def _filter_climbs(climbs, count):
    """
    Takes a raw list of climbs, filters out climbs that are only downhill, then
    sorts by length and returns the top "count" climbs. The returned list is
    sorted by steepness. Each climb in the list is a tuple of (grade,length).

    @param climbs: list of climbs to process
    @type climbs: C{list}
    @param count: how many climbs to return
    @type count: C{int}

    @return: top 'count' climbs
    @rtype: C{list}
    """
    climbs = [climb for climb in climbs if climb[0] > 0.0]
    climbs.sort(key=lambda x: x[1], reverse=True)
    climbs = climbs[:count]
    climbs.sort(key=lambda x: x[0], reverse=True)

    return climbs

def _calc_rise_fall_grades(rise_height, rise_dist, fall_height, fall_dist):
    """
    Calculate the rising and falling grades for a set of data.

    @param rise_height: rising height
    @type rise_height: C{float}
    @param rise_dist: rising distance
    @type rise_dist: C{float}
    @param fall_height: falling height
    @type fall_height: C{float}
    @param fall_dist: falling distance
    @type fall_dist: C{float}

    @return: rising grade, falling grade
    @rtype: (C{float},C{float})
    """
    rise_grade = 0.0
    if rise_dist > 0.0:
        rise_grade = (rise_height / (rise_dist * mile_feet)) * 100.0
    fall_grade = 0.0
    if fall_dist > 0.0:
        fall_grade = (fall_height / (fall_dist * mile_feet)) * 100.0
    return rise_grade, fall_grade

######## PROCESS WAYPOINTS ########

class PointsProcessor(object):
    """
    Encapsulates a set of points representing a line and all the operations we
    might want to do on it.

    @ivar intras: intra-point values used for all our calculations, in the form
    of a list of (length,rise) tuples
    @type intras: C{list} of (C{float},C{float})
    """

    def __init__(self, points):
        """
        Calculate and store the distance and rise between each pair of points
        in the list. This list will be used by all the other methods on this
        object.
        
        @param points: list of waypoints
        @type points: C{list} of L{Point} objects
        """
        self.intras = [
            (points[index].calculate_distance(points[index+1]),
            (points[index+1].ele - points[index].ele) * meter_feet)
            for index in range(len(points)-1)]

    def calc_points_distance(self):
        """
        Calculate the length of the line.  This is the distance along the set
        of waypoints.

        @return: length of line
        @rtype: C{float}
        """
        return sum([length for length, rise in self.intras])

    def calc_points_rise(self):
        """
        Calculate the cumulative rise for the line.  This is the rise height
        for every intra-point value that rises.

        @return: rise height, rise distance
        @rtype: (C{float},C{float})
        """
        rise_height = sum([rise for length, rise in self.intras if rise > 0.0])
        rise_dist = sum([length for length, rise in self.intras if rise > 0.0])
        return rise_height, rise_dist

    def calc_points_fall(self):
        """
        Calculate the cumulative fall for the line. This is the rise height for
        every intra-point value that falls.

        @return: fall height, fall distance
        @rtype: (C{float},C{float})
        """
        fall_height = sum([rise for length, rise in self.intras if rise <= 0.0])
        fall_dist = sum([length for length, rise in self.intras if rise <= 0.0])
        return fall_height, fall_dist

    def calc_points_climbs(self):
        """
        Create a list of climbs in the line.  Ignore single-point declines
        during a climb, since this seems to give more realistic climbs than if
        single "bumps" cause climbs to restart.

        @return: list of climbs with (grade,distance)
        @rtype: C{list} of (C{float},C{float})
        """
        climb_height = 0.0
        climb_dist = 0.0
        climbs = []
        in_climb = -1

        for length, rise in self.intras:
            if rise > 0.0:
                in_climb = 1
                climb_height += rise
                climb_dist += length
            else:
                if in_climb == 0:
                    if climb_dist > 0.0:
                        climbs.append( (
                                (climb_height / (climb_dist * mile_feet)) * 100.0, 
                                climb_dist) )
                    climb_height = 0.0
                    climb_dist = 0.0
                elif in_climb > 0:
                    climb_height += rise # remember, it's negative
                    climb_dist += length
                in_climb -= 1

        return climbs

class SegmentProcessor(PointsProcessor):
    """
    Hold all the values we are interested in for a ride segment and create a
    dictionary to present them.

    @ivar seg: segment we are processing
    @type seg: C{Segment}
    @ivar start_dist: distance into ride for first point of segment
    @type start_dist: C{float}
    @ivar length: length of the segment
    @type length: C{float}
    @ivar rise_height: cumulative height of ascent in this segment
    @type rise_height: C{float}
    @ivar rise_dist: length of the part of the segment going up
    @type rise_dist: C{float}
    @ivar fall_height: cumulative height of descent in this segment
    @type fall_height: C{float}
    @ivar fall_dist: length of the part of the segment going down
    @type fall_dist: C{float}
    @ivar rise_grade: average climbing grade of segment
    @type rise_grade: C{float}
    @ivar fall_grade: average descending grade of segment
    @type fall_grade: C{float}
    @ivar climbs: list of "top" climbs for the segment
    @type climbs: C{list}
    """

    def __init__(self, seg, accum):
        """
        Initialize and calculate all values for the segment.

        @param seg: segment to analyze
        @type seg: L{Segment}
        @param accum: segment accumulator
        @type accum: L{SegmentAccumulator}
        """
        PointsProcessor.__init__(self, seg.waypoints)
        self.seg = seg
        self.start_dist = accum.length
        self.length = self.calc_points_distance()
        self.rise_height, self.rise_dist = self.calc_points_rise()
        self.fall_height, self.fall_dist = self.calc_points_fall()
        self.rise_grade, self.fall_grade = _calc_rise_fall_grades(
            self.rise_height, self.rise_dist, self.fall_height, self.fall_dist)
        climbs = self.calc_points_climbs()
        self.climbs = _filter_climbs(climbs, CLIMB_COUNT)

    def create_element(self):
        """
        Create a dictionary that can be used by Jinja2 to present this data.

        The dictionary contains the following:
          - id: id of segment
          - start_dist: distance in ride for starting point
          - end_dist: distance in ride for ending point
          - length: length of ride
          - net_height: net change in elevation over segment
          - rise_height: height of climbing in segment
          - rise_dist: distance spent climbing in segment
          - rise_grade: average grade of climbing in segment
          - fall_height:  height of descending in segment
          - fall_dist: distance spent descending in segment
          - fall_grade: average grade of descending in segment
          - gradients: table containing gradients and how much time spent in them
          - climbs: list with climbs, their grades, and their lengths in segment

        @return: presentable data
        @rtype: C{dict}
        """
        return {'id': self.seg.id,
                'start_dist': self.start_dist,
                'end_dist': self.start_dist + self.length,
                'length': self.length,
                'net_height': self.rise_height - self.fall_height,
                'rise_height': self.rise_height,
                'rise_dist': self.rise_dist,
                'rise_grade': self.rise_grade,
                'fall_height': self.fall_height,
                'fall_dist': self.fall_dist,
                'fall_grade': self.fall_grade,
                'climbs': self.climbs
                }

class SegmentAccumulator(object):
    """
    Gather all the values we're interested in for a ride by extracting them
    from the processed segments and accumulating them.

    @ivar distance: length of the ride
    @type distance: C{float}
    @ivar rise_height: cumulative ascent in this ride
    @type rise_height: C{float}
    @ivar rise_dist: length of part of the ride ascending
    @type rise_dist: C{float}
    @ivar fall_height: cumulative descent in this ride
    @type fall_height: C{float}
    @ivar fall_dist: length of part of the ride descending
    @type fall_dist: C{float}
    @ivar climbs: list of "top" climbs for the ride
    @type climbs: C{list}
    """

    def __init__(self):
        """
        Initialize all values for the ride.
        """
        self.length = 0.0
        self.rise_height = 0.0
        self.rise_dist = 0.0
        self.fall_height = 0.0
        self.fall_dist = 0.0
        self.climbs = []

    def accumulate_segment(self, seg):
        """
        Extract all relevant values from the given segment processor and add
        them to the instance variables.

        @param seg: segment processor to get data from
        @type seg: L{SegmentProcessor}
        """
        self.length += seg.length
        self.rise_height += seg.rise_height
        self.rise_dist += seg.rise_dist
        self.fall_height += seg.fall_height
        self.fall_dist += seg.fall_dist
        self.climbs.extend(seg.climbs)

    def create_element(self):
        """
        Create a dictionary that can be used by Jinja2 to present this data.
        Calculate the values that haven't been accumulated.

        The dictionary contains the following data:
          - length: length of ride
          - net_height: net change in elevation over ride
          - rise_height: height of climbing in ride
          - rise_dist: distance spent climbing in ride
          - rise_grade: average grade of climbing in ride
          - fall_height:  height of descending in ride
          - fall_dist: distance spent descending in ride
          - fall_grade: average grade of descending in ride
          - climbs: list with climbs, their grades, and their lengths in ride

        @return: presentable data
        @rtype: C{dict}
        """
        rise_grade, fall_grade = _calc_rise_fall_grades(
            self.rise_height, self.rise_dist, 
            self.fall_height, self.fall_dist)
        climbs = _filter_climbs(self.climbs, CLIMB_COUNT)

        return {'length': self.length,
                'net_height': self.rise_height - self.fall_height,
                'rise_height': self.rise_height,
                'rise_dist': self.rise_dist,
                'rise_grade': rise_grade,
                'fall_height': self.fall_height,
                'fall_dist': self.fall_dist,
                'fall_grade': fall_grade,
                'climbs': climbs
                }

######## PROCESS RIDE ########

def process_elevations(ride):
    """
    This is the main entry point for this module.  It goes through the
    elevation data for a ride and creates lists of processed data. It returns
    the data as a single dictionary describing the overall ride and a list of
    dictionaries that each describe a segment of the ride.

    Each dictionary element in the segment list has the following information:
      - id: id of segment
      - start_dist: distance in ride for starting point
      - end_dist: distance in ride for ending point
      - length: length of ride
      - net_height: net change in elevation over segment
      - rise_height: height of climbing in segment
      - rise_dist: distance spent climbing in segment
      - rise_grade: average grade of climbing in segment
      - fall_height:  height of descending in segment
      - fall_dist: distance spent descending in segment
      - fall_grade: average grade of descending in segment
      - climbs: list with climbs, their grades, and their lengths in segment

    The overall ride data is a dictionary with the following data:
      - length: length of ride
      - net_height: net change in elevation over ride
      - rise_height: height of climbing in ride
      - rise_dist: distance spent climbing in ride
      - rise_grade: average grade of climbing in ride
      - fall_height:  height of descending in ride
      - fall_dist: distance spent descending in ride
      - fall_grade: average grade of descending in ride
      - climbs: list with climbs, their grades, and their lengths in ride
     
    @param ride: ride to process
    @type ride: L{Ride}

    @return: ride data, list of segment data
    @rtype: C{dict}, C{list} of C{dict}
    """
    ele_set = []
    accum = SegmentAccumulator()
    for seg in ride.segs:
        seg_proc = SegmentProcessor(seg, accum)
        ele_set.append(seg_proc.create_element())
        accum.accumulate_segment(seg_proc)

    return accum.create_element(), ele_set
