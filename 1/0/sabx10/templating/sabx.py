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
Framework for processing SABX 1.0 files with Jinja2 templates using
command-line programs.
"""

import sys, os
from generic import TemplateProcessor
from sabx10.oxm import parse_no_def_namespaces, parse_tree

class SabxProcessor(TemplateProcessor):
    """
    The C{SabxProcessor} sub-classes the L{TemplateProcessor} class.  It
    provides an extendable framework for processing SABX 1.0 files with Jinja2
    templates.  It builds on the generic L{TemplateProcessor} by adding an
    "infile" option to specify the SABX 1.0 file and by providing a routine for
    parsing the SABX 1.0 data.

    Sample Code:::

      from sabx10.templating import SabxProcessor
      SabxProcessor().process()

    Sample Usage:::
    
      $ sample.py -i sample.sabx -o sample.out sample.jinja2

    @ivar in_file: handle to file to read SABX 1.0 data from
    @type in_file: C{file}
    @ivar sabx: C{dic} holding all the data for the given SABX 1.0 file
    @type sabx: C{dict}
    """
    def __init__(self, template_file=None, man=None):
        """
        Adds the "infile" command-line option specifying the SABX 1.0 file to
        read from to the options specified in the base class.

        @param template_file: (optional) path & file name of a template file
        @type template_file: C{string}
        @param man: (optional) extended program help information
        @type man: C{string}
        """
        TemplateProcessor.__init__(self, template_file, man)

        self.parser.add_option("-i", "--infile", dest="in_file",
                               help="input sabx data from FILE", 
                               metavar="FILE")

    def get_template_data(self):
        """
        Parse the specified SABX 1.0 file and save its object representation.
        Over-ride this in sub-classes to modify the SABX data before passing it
        to the template.
        """
        if self.options.in_file:
            self.in_file = open(self.options.in_file, "r")
        else:
            self.in_file = sys.stdin

        tree = parse_no_def_namespaces(self.in_file)
        self.template_data.update(parse_tree(tree))

        self.in_file.close()

    def process_template(self):
        """
        Process the SABX 1.0 data into the template. First, delete the input
        file if it is the same as the output file.  This way you can read an
        SABX 1.0 file and write the template output to the same file name,
        effectively over-writing the file.
        """
        if self.options.in_file == self.options.out_file:
            os.unlink(self.options.in_file)

        TemplateProcessor.process_template(self)
