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
This package plots the elevation profiles for rides and their segments from an
SABX file.  The profiles are saved as PNG files.  It also provides the ability
to convert a PNG profile into a PDF file.

The entry points for the package are L{plot_all_rides} in the
L{sabx10.profiles.profiles} module and L{ride_profiles_to_pdfs} in the
L{sabx10.profiles.profiles_pdf} module.

For examples of what ride profiles look like, go to
U{SABikeRides.com<http://www.sabikerides.com/>}, which contains a bunch of
rides to choose from.

Copyright
=========

The sabx10.profiles package is part of sabx10.

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
from profiles import plot_all_rides
from profiles_pdf import ride_profiles_to_pdfs
