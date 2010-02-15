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
Generic framework for working with Jinja2 templates in command-line oriented
programs.
"""

import os.path
import sys
from optparse import OptionParser
from jinja2 import Environment, FileSystemLoader

class NotEnoughArgsException(Exception):
    """
    This exception is raised to indicate that not enough arguments were passed
    in to the program.
    """
    pass

class TemplateProcessor(object):
    """
    L{TemplateProcessor} provides an extendable framework for working with
    Jinja2 templates.  It allows for specifying a template file and an
    (optional) output file.  It sets up everything necessary for Jinja2 to
    function, then processes the template and handles its output.

    To use this class for your own purposes, just sub-class it and override the
    relevant functions.  The process method controls the general flow, and the
    other methods handle specific functions within the flow.

    Sample Code:::

      from sabx_templating import TemplateProcessor
      TemplateProcessor().process()

    Sample Usage:::

      $ sample.py -o sample.out sample.jinja2

    @ivar parser: the C{OptionParser} for handling command-line options
    @type parser: C{OptionParser}
    @ivar options: options specificed on the command-line
    @type options: C{options}
    @ivar args: non-optional arguments specified on the command-line
    @type args: C{list} of C{string}
    @ivar template_path: path for template file
    @type template_path: C{string}
    @ivar template_file: file name of template file
    @type template_file: C{string}
    @ivar out_file: handle to file to write processed template into
    @type out_file: C{file}
    @ivar template_data: data to be processed by the template
    @type template_data: C{dict}
    @ivar man: extended help information
    @type man: C{string}
    """

    def __init__(self, template_file=None, man=None):
        """
        Sets up handling for command-line options using the optparse module
        from the Python standard library.  Creates the option "-o" for
        specifying an output file and the "-m" option for printing the man-page
        type full help screen.

        @param template_file: (optional) path & file name of a template file
        @type template_file: C{string}
        @param man: (optional) extended program help information
        @type man: C{string}
        """
        if not template_file:
            usage = "usage: %prog [options] template_file"
        else:
            usage = "usage: %prog [options]"
        self.parser = OptionParser(usage=usage)
        self.parser.add_option("-o", "--outfile", dest="out_file",
                               help="output processed template to FILE", 
                               metavar="FILE")

        self.man = man
        if man:
            self.parser.add_option("-m", "--man-page", dest="man_page",
                                   action="store_true",
                                   help="display the man page and exit", 
                                   default=False, metavar="MANPAGE")

        if template_file:
            self.template_path, self.template_file = \
                os.path.split(template_file)
        else:
            self.template_path = self.template_file = None

        self.template_data = {}

    def process_options(self, arg_count=0):
        """
        Process the options passed in on the command line. Make sure that a
        template file name is provided, either on the command line or via the
        constructor.  If the template file is passed on the command line, it's
        expected to be the first non-optional argument.

        @param arg_count: count of non-optional command-line arguments expected
        @type arg_count: C{int}

        @raise NotEnoughArgsException: this exception is raised when there
        is no template file specified on the command-line
        """
        (self.options, self.args) = self.parser.parse_args()

        if self.man and self.options.man_page:
            print self.man
            sys.exit(0)

        if not self.template_file:
            arg_count += 1
        if len(self.args) < arg_count:
            raise NotEnoughArgsException("NOT ENOUGH ARGUMENTS PROVIDED")

        if not self.template_file:
            self.template_path, self.template_file = os.path.split(self.args[0])

    def get_template_data(self):
        """
        Initialize the data for the template.
        """
        pass

    def process_template(self):
        """
        Setup the output file, setup the environment, then process the template
        file.  Put the processed template into the output file.
        """
        if self.options.out_file:
            self.out_file = open(self.options.out_file, "w")
        else:
            self.out_file = sys.stdout

        env = Environment(loader=FileSystemLoader(self.template_path), 
                          trim_blocks=True)
        template = env.get_template(self.template_file)
        self.out_file.write(template.render(self.template_data))

    def process(self):
        """
        Setup for and process the template.
        """
        self.process_options()
        self.get_template_data()
        self.process_template()
