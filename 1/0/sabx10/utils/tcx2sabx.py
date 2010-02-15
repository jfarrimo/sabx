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
Handle converting TCX files to SABX 1.0 files.
"""

import os.path
import sys
import uuid

from sabx10.oxm import parse_no_def_namespaces
from sabx10.templating import TemplateProcessor

class TcxProcessor(TemplateProcessor):
    """
    Process a TCX file, pulling out all its point data for processing.  Add in
    a uuid and title, then process it all through a jinja2 template.  This
    class sub-classes L{TemplateProcessor} to do most of the grunt work in
    handling command-line options and processing the jinja2 template.
    """

    def __init__(self, template_file=None, man=None):
        """
        Add C{optparse} options for the infile and the index.  Seed
        template_data with uuid.

        @param template_file: (optional) file name of template file
        @type template_file: C{string}
        @param man: (optional) extended program help
        @type man: C{string}
        """
        TemplateProcessor.__init__(self, template_file, man)

        self.parser.add_option("-i", "--infile", dest="in_file",
                               help="input tcx data from FILE", 
                               metavar="FILE")
        self.parser.add_option("-n", "--index", dest="start_index",
                               type="int", default=1, 
                               help="starting point index")

        self.template_data['uuid'] = uuid.uuid4()

    def get_template_data(self):
        """
        Get the point data from the TCX file and save it in template_data.
        """
        if self.options.in_file:
            self.in_file = open(self.options.in_file, "r")
            self.template_data['title'] = \
                os.path.basename(self.options.in_file)
        else:
            self.in_file = sys.stdin
            self.template_data['title'] = "stdin"

        tree = parse_no_def_namespaces(self.in_file)
        count = self.options.start_index
        laps = tree.findall('Activities/Activity/Lap')
        points = []
        for lap in laps:
            pts = lap.findall('Track/Trackpoint')
            for pt in pts:
                if pt.find('Position') and \
                        pt.findtext('AltitudeMeters'):
                    points.append( {'index': count, 
                                    'lat': pt.findtext(
                                'Position/LatitudeDegrees'),
                                    'lon': pt.findtext(
                                'Position/LongitudeDegrees'),
                                    'ele': pt.findtext(
                                'AltitudeMeters')} )
                    count += 1
        self.template_data['points'] = points
