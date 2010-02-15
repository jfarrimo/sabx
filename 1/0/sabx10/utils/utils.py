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
