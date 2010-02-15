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
Handle adding USGS elevations to an SABX 1.0 file.
"""

import sys
import urllib

from sabx10.oxm import parse_no_def_namespaces
from sabx10.templating import SabxProcessor

def get_usgs(lat, lon):
    """
    Call the USGS web service to get the elevation for a point represented by
    the (lat,lon) pair.
    """
    first = False
    url = "http://gisdata.usgs.gov/" \
        "xmlwebservices2/elevation_service.asmx/getElevation" \
        "?X_Value=%s" \
        "&Y_Value=%s" \
        "&Elevation_Units=METERS" \
        "&Source_Layer=-1" \
        "&Elevation_Only=1" % (lon, lat)
    tree = parse_no_def_namespaces(urllib.urlopen(url))
    return tree.findtext("Elevation_Query/Elevation")

class UsgsProcessor(SabxProcessor):
    """
    Add USGS elevations to all the points in an SABX 1.0 file.
    """

    def get_template_data(self):
        """
        Add the USGS elevations to the template data.
        """
        SabxProcessor.get_template_data(self)

        count = 0
        for seg in self.template_data['seg_list']:
            for pt in seg.waypoints:
                pt.usgs = get_usgs(pt.lat, pt.lon)

                count += 1
                if count % 100 == 0:
                    sys.stderr.write("%s" % count)
                else:
                    sys.stderr.write(".")
                
        sys.stderr.write("\n")
