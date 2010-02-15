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
Constant values used by the profile generator package.

@var PROFILE_PPI: pixels per inch for screen-display resolution
@type PROFILE_PPI: C{int}
@var PROFILE_PDF_PPI: pixels per inch for PDF resolution
@type PROFILE_PDF_PPI: C{int}
@var SMALL_WIDTH: width of small profiles
@type SMALL_WIDTH: C{int}
@var SMALL_HEIGHT: height of small profiles
@type SMALL_HEIGHT: C{int}
@var LARGE_WIDTH: width of large profiles
@type LARGE_WIDTH: C{int}
@var LARGE_HEIGHT: height of large profiles
@type LARGE_HEIGHT: C{int}
@var FONT_POINTS_PER_INCH: PPI for fonts
@type FONT_POINTS_PER_INCH: C{int}
@var FONT_NAME: font to use in profile
@type FONT_NAME: C{string}
@var LABEL_FONT_SIZE: size of font for labels
@type LABEL_FONT_SIZE: C{int}
@var ANNO_FONT_SIZE: size of font for plot annotations
@type ANNO_FONT_SIZE: C{int}
"""
PROFILE_PPI = 75
PROFILE_PDF_PPI = 200
SMALL_WIDTH = 4 
SMALL_HEIGHT = 2
LARGE_WIDTH = 10
LARGE_HEIGHT = 5
FONT_POINTS_PER_INCH = 72
FONT_NAME = 'sans-serif'
LABEL_FONT_SIZE = 12
ANNO_FONT_SIZE = 8
