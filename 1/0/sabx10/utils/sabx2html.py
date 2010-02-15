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
Handle converting SABX point data into a basic HTML file.
"""

from sabx10.oxm import parse_no_def_namespaces, parse_tree
from sabx10.templating import SabxProcessor

class HtmlProcessor(SabxProcessor):
    """
    Process an SABX 1.0 file, pulling out all its point data for processing.
    """

    def __init__(self, template_file=None, man=None):
        """
        Add C{optparse} options for the index.

        @param template_file: (optional) file name of template file
        @type template_file: C{string}
        @param man: (optional) extended program help
        @type man: C{string}
        """
        SabxProcessor.__init__(self, template_file, man)

        self.parser.add_option("-n", "--index", dest="ride_index",
                               default="1", 
                               help="ride index")

    def get_template_data(self):
        """
        Add the points to the SABX 1.0 data.
        """
        SabxProcessor.get_template_data(self)

        points = []
        for seg_id in \
                self.template_data['ride_dict'][self.options.ride_index].segs:
            for pt in self.template_data['seg_dict'][seg_id].waypoints:
                points.append( {'index': pt.id, 
                                'lat': pt.lat, 
                                'lon': pt.lon,
                                'ele': pt.ele} )
        self.template_data['points'] = points
