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
This package provides all the functionality needed to create PDF maps from SABX
files. The main code will do all the work to prepare data for rendering the
maps.  The render script generated from the render template handles the actual
rendering of the PNG maps and turning them into PDF files.

The entry point for this package is the L{SabxProcessor} class in the
L{sabx10.osm.osm} module.

Copyright
=========

The sabx10.osm package is part of sabx10.

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

from osm import SabxProcessor
from styles import StyleProcessor
from utils import determine_path
