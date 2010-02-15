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
Analyze the elevations for an SABX 1.0 file.
"""

from sabx10.oxm import mile_feet, meter_feet

def get_ride_ele_bounds(ride):
    """
    Get the bounds of the elevation range for the ride.

    @param ride: ride to analyze
    @type ride: SABX 1.0 L{Ride}

    @return: lowest elevation, highest elevation
    @rtype: (C{float},C{float})
    """
    lowest = 100000.0
    highest = 0.0
    for seg in ride.segs:
        l, h = seg.find_lowest_highest()
        lowest = min(lowest, l)
        highest = max(highest, h)
    return lowest, highest

def analyze_ride(ride, lowest, highest):
    """
    Analyze the elevations for the ride.  Specifically, check the differences
    in the elevations between the end of each segment and the start of the next
    segment in the ride.  Check this for the ele and the usgs values.  When the
    ele and usgs changes fall outside the acceptable range, graph them.  The
    acceptable range is defined as a percentage of the difference between the
    lowest and highest elevations.

    @param ride: ride to check
    @type ride: SABX 1.0 L{Ride}
    @param lowest: lowest elevation for the ride
    @type lowest: C{float}
    @param highest: highest elevation for the ride
    @type highest: C{float}
    """
    diff = (highest - lowest) * 0.03
    for seg in ride.segs:
        print "segment %s (%s)" % (seg.id, seg.road)

        if seg.waypoints[-1].ele and seg.waypoints[-2].usgs:
            rise_ele = run_ele = grade_ele = 0.0
            rise_ele = (seg.waypoints[-1].ele - seg.waypoints[-2].ele)
            rise_ele *= meter_feet
            run_ele = seg.waypoints[-1].calculate_distance(seg.waypoints[-2])
            run_ele *= mile_feet
            if run_ele != 0.0:
                grade_ele = (rise_ele / run_ele) * 100.0
            
            rise_usgs = run_usgs = grade_usgs = 0.0
            rise_usgs = (seg.waypoints[-1].usgs - seg.waypoints[-2].usgs)
            rise_usgs *= meter_feet
            run_usgs = seg.waypoints[-1].calculate_distance(seg.waypoints[-2])
            run_usgs *= mile_feet
            if run_usgs != 0.0:
                grade_usgs = (rise_usgs / run_usgs) * 100.0

            #if abs(rise_ele) > diff or abs(rise_usgs) > diff:
            if abs(rise_ele - rise_usgs) > diff:
                print "| %s %s, %s" % ("*"*(abs(int(grade_ele))), 
                                       rise_ele, run_ele)
                print "| %s %s, %s" % ("*"*(abs(int(grade_usgs))), 
                                       rise_usgs, run_usgs)
        else:
            print "NO USGS"

def analyze_all_rides(rides):
    """
    Analyze all the rides in the ride list.
    """
    for ride in rides:
        l, h = get_ride_ele_bounds(ride)
        print ""
        print "======="
        print "RIDE %s" % ride.id
        print "======="
        print "range: %s, %s, %s" % (l, h, h-l)
        analyze_ride(ride, l, h)
