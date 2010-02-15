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
Provide the tools to generate style sheets used by Mapnik for rendering maps.
"""
import os.path

from sabx10.templating import TemplateProcessor, SabxProcessor, \
    strip_end_slash

from consts import PIX_SCALE_FACTOR

class StyleProcessor(SabxProcessor):
    """
    Handle the processing of a style template.  This will generate the style
    sheet necessary for Mapnik to know how to generate a map.
    """
    def __init__(self, template_file=None, man=None):
        """
        Add support for an OSM data file and a logo directory.

        @param template_file: name of template file to use
        @type template_file: C{string}
        @param man: text for man page
        @type man: C{string}
        """
        SabxProcessor.__init__(self, template_file, man)

        self.parser.add_option("-d", "--datafile", dest="data_file",
                               help="osm data FILE name", 
                               metavar="FILE")
        self.parser.add_option("-l", "--logodir", dest="logo_dir",
                               help="osm logo directory", 
                               metavar="LOGO")

        self.template_data['PIX_SCALE_FACTOR'] = PIX_SCALE_FACTOR

    def process_options(self):
        """
        Process the OSM data file file and logo directory.
        """
        SabxProcessor.process_options(self)

        base_path, base_file = os.path.split(self.options.out_file)
        self.template_data['osm_data'] = \
            os.path.abspath(os.path.join(base_path, "map.osm"))
        self.template_data['logo_dir'] = strip_end_slash(self.options.logo_dir)

    def process_template(self):
        """
        Generate a template file for each ride in the rideset.
        """
        out_base = self.options.out_file
        for index in range(len(self.template_data['ride_list'])):
            self.template_data['route_index'] = index
            self.options.out_file = "%s_%s.xml" % (out_base, index)
            TemplateProcessor.process_template(self)
