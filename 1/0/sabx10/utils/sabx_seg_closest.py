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
Find the closest point in a segment.
"""

from sabx10.oxm import Point

def search_seg(sabx, seg_id, lat, lon):
    """
    Search the indicated segment and find which waypoint is closest to the
    given (lat,lon) point.  Print the result.
    """
    search_pt = Point(lat, lon)
    shortest = 10000.0
    for pt in sabx['seg_dict'][seg_id].waypoints:
        dist = search_pt.calculate_distance(pt)
        if dist < shortest:
            shortest = dist
            id = pt.id

    print "id= %s   distant = %s" % (id, shortest)
