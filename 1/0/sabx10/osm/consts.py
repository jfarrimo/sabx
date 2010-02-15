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
Various constants used in generating PDF maps.

@var PPI: desired points per inch for PNG Maps
@type PPI: C{float}
@var MAPNIK_PPI: points per inch Mapnik uses
@type MAPNIK_PPI: C{float}
@var PIX_SCALE_FACTOR: factor for scaling between Mapnik PPI and our PPI
@type PIX_SCALE_FACTOR: C{float}
@var LETTER_WIDTH: inch width of letter-sized page
@type LETTER_WIDTH: C{float}
@var LETTER_HEIGHT: inch height of letter-sized page
@type LETTER_HEIGHT: C{float}
@var LEGAL_WIDTH: inch width of legal-sized page
@type LEGAL_WIDTH: C{float}
@var LEGAL_HEIGHT: inch height of legal-sized page
@type LEGAL_HEIGHT: C{float}
@var WIDTH: inch width of page size we're using
@type WIDTH: C{float}
@var HEIGHT: inch height of page size we're using
@type HEIGHT: C{float}
"""
from sabx10.map import BORDER

PPI = 200.0
MAPNIK_PPI = 90.7
PIX_SCALE_FACTOR = PPI / MAPNIK_PPI

LETTER_WIDTH = 8.5
LETTER_HEIGHT = 11.0
LEGAL_WIDTH = 8.5
LEGAL_HEIGHT = 14.0

WIDTH = LETTER_WIDTH - (2.0 * BORDER)
HEIGHT = LETTER_HEIGHT - (2.0 * BORDER)
