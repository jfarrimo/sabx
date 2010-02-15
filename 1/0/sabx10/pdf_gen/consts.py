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
Constant values used by the PDF generator package.

@var COL_WIDTH_1: width of first column in PDF table
@type COL_WIDTH_1: C{float}
@var COL_WIDTH_2: width of second column in PDF table
@type COL_WIDTH_2: C{float}
@var COL_WIDTH_4: width of fourth column in PDF table
@type COL_WIDTH_4: C{float}
@var COL_WIDTH_ALL: width of first, second, and fourth columns combined 
in PDF table
@type COL_WIDTH_ALL: C{float}
"""
COL_WIDTH_1 = 0.9
COL_WIDTH_2 = 0.8
COL_WIDTH_4 = 0.8
COL_WIDTH_ALL = COL_WIDTH_1 + COL_WIDTH_2 + COL_WIDTH_4
