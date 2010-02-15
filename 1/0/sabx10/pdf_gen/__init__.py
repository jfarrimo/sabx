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
This package generates a PDF version of the ride route instructions for an SABX
file.  It generates a seperate PDF file for each ride in a rideset.  The PDF
file contains a table of data formatted as follows::

    +------------------------------------------------+
    | Landmark | Distance | Description     | Length |
    +----------+----------+-----------------+--------+
    | Parking  | 0.0      | This is parking | 3.2    |
    +----------+----------+-----------------+--------+
    | S - 1    | 1.2      | This is a stop  | store  |
    +----------+----------+-----------------+--------+
    | P - 1    | 2.2      | This is a POI   | POI    |
    +----------+----------+-----------------+--------+
    | T - 1    | 3.2      | This is a turn  | 4.4    |
    +----------+----------+-----------------+--------+

For more examples, go to U{SABikeRides.com<http://www.sabikerides.com/>}, which
contains a bunch of rides to choose from.

The entry point for this package is the function L{pdf_all_rides} in the
L{sabx10.pdf_gen.instructions} module.

Copyright
=========

The sabx10.pdf_gen package is part of sabx10.

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

from instructions import pdf_all_rides
