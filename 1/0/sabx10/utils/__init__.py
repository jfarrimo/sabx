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
The C{utils} package contains the guts of all the SABX file manipulation
utilities.  The scripts for the utilities are just simple shells that import
the guts and call them.  A few of the utilities don't depend on
L{sabx10.templating.generic.TemplateProcessor} or
L{sabx10.templating.sabx.SabxProcessor}, so they have some code to handle their
command-line arguments, but in general the utilities are mere husks calling
into the modules in this package.

Copyright
=========

The sabx10.utils package is part of sabx10.

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
from gpx2sabx import GpxProcessor
from sabx2html import HtmlProcessor
from sabx_cleanup import CleanupProcessor
from sabx_csv import CsvProcessor
from sabx_ele_analyze import analyze_all_rides
from sabx_number import NumProcessor
from sabx_seg_closest import search_seg
from sabx_seg_reverse import RevProcessor
from sabx_usgs import UsgsProcessor
from tcx2sabx import TcxProcessor
from utils import determine_path
