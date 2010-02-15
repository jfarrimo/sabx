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
This module provides all the functionality needed to create web-based maps from
SABX files. These maps use Google Maps for display.  Instead of trying to
describe them, I'll just refer you to
U{SABikeRides.com<http://www.sabikerides.com/>} where you can see maps that
have been created by this module.  Note that this module and its templates just
create the map page itself.  The profiles and printable pdf versions of the
maps are created by the L{sabx10.osm}, L{sabx10.pdf_gen}, and
L{sabx10.profiles} packages.

The main entry point for this package is the L{SabxProcessor} class in the
L{sabx10.map.map} module.

Copyright
=========

The sabx10.map package is part of sabx10.

sabx10 - an SABX file manipulation library
Copyright (C) 2009, 2010 Jay Farrimond (jay@sabikerides.com)

sabx10 is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

sabx10 is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
details.

You should have received a copy of the GNU Lesser General Public License along
with sabx10.  If not, see U{http://www.gnu.org/licenses/}.
"""

from consts import BORDER
from map import SabxProcessor
from utils import determine_path
