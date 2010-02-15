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
Handle reversing segments in SABX files.
"""

from sabx10.templating import SabxProcessor

class RevProcessor(SabxProcessor):
    """
    Process an SABX 1.0 file and reverse the order of the waypoints in a
    segment.

    @ivar seg: id of segment to reverse
    @type seg: C{string}
    """

    def __init__(self, template_file=None, man=None):
        """
        Add C{optparse} options for the usage.

        @param template_file: (optional) file name of template file
        @type template_file: C{string}
        @param man: (optional) extended program help
        @type man: C{string}
        """
        SabxProcessor.__init__(self, template_file, man)
        self.parser.usage = "%s seg_id" % self.parser.usage

    def process_options(self):
        """
        Get the seg id.  It's expected to be the last command-line argument.
        """
        SabxProcessor.process_options(self, 1)
        self.seg = self.args[-1]

    def get_template_data(self):
        """
        Reverse the waypoints of the designated segment.
        """
        SabxProcessor.get_template_data(self)
        self.template_data['seg_dict'][self.seg].waypoints.reverse()
