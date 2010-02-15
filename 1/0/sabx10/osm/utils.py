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
Utility routines.
"""

import os, sys

class BaseId(object):
    """
    Generate sequential, unique ids.

    @ivar next_id: next id to return
    @type next_id: C{int}
    """
    def __init__(self, start_id=1):
        """
        Save the starting id.

        @param start_id: starting id
        @type start_id: C{int}
        """
        self.next_id = start_id

    def next(self):
        """
        Get the next id in the sequence and increment it.

        @return: next id
        @rtype: C{int}
        """
        ret_val = self.next_id
        self.next_id += 1
        return ret_val

class NodeId(BaseId):
    """
    A L{BaseId} modification that starts numbering after the ids in the
    waypoints for a given segment list.
    """

    def __init__(self, seg_list):
        """
        Get the max id in the segment list and start at the next highest one.

        @param seg_list: C{list} of L{Segment}s to check against
        @type seg_list: C{list} of L{Segment}
        """
        start_id = max([max([int(pt.id) for pt in seg.waypoints])
                        for seg in seg_list]) + 1
        BaseId.__init__(self, start_id)

def determine_path():
    """
    Determine the path to the file containing this routine.  This is handy for
    getting the directory a package is located in.  Obviously, this works best
    when all the files for a package are in the same directory and not split
    into sub-directories.

    This is based on code found in the distutils tutorial at
    U{http://wiki.python.org/moin/Distutils/Tutorial}.  Apparently the tutorial
    author found it in wxglade.py.

    @return: directory part of path this file is in
    @rtype: C{string}
    """
    root = __file__
    if os.path.islink (root):
        root = os.path.realpath (root)
    return os.path.dirname (os.path.abspath (root))
