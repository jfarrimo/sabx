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
Miscellaneous utilities for use with templating.
"""

def strip_end_slash(path):
    """
    Make sure a path C{string} doesn't have an ending slash.

    We do this because jinja2 doesn't have os.path.join functionality

    @param path: path C{string} to check
    @type path: C{string}

    @return: path C{string} with no ending slash
    @rtype: C{string}
    """
    if path[-1] == '/':
        path = path[:-1]
    return path
