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
Use Reportlab and the Image library to convert a profile PNG file into a PDF
file.  We only bother with the large profiles.
"""
import os.path

import Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from sabx10.map import BORDER
from sabx10.oxm import process_rides, parse_top_level

from consts import LARGE_WIDTH, LARGE_HEIGHT

def _large_profile_to_pdf(title, ride, in_dir, in_base, out_dir, out_base, 
                          seg_index='all',):
    """
    Take the large PNG profile for a ride and convert it to a PDF file with the
    image embedded in it.

    @param title: title base for PDF file
    @type title: C{string}
    @param ride: L{Ride} object to generate PDF for
    @type ride: L{Ride} object
    @param in_dir: directory to find PNG file in
    @type in_dir: C{string}
    @param in_base: base of name for PNG file
    @type in_base: C{string}
    @param out_dir: directory to put PDF file in
    @type out_dir: C{string}
    @param out_base: base of name for PDF file
    @type out_base: C{string}
    @param seg_index: index of segment in ride to generate PDF for 
    (default to all)
    @type seg_index: C{string}
    """
    profile_name = os.path.join(in_dir, '%s_prof_large_%s_%s.png' % 
                                (in_base, ride.index, seg_index))
    im = Image.open(profile_name)
    im = im.rotate(90)

    pdf_file_name = os.path.join(out_dir, "%s_prof_%s.pdf" % 
                                 (out_base, ride.index))
    page_width, page_height = letter
    c = canvas.Canvas(pdf_file_name, pagesize=letter)
    c.drawInlineImage(im, BORDER * inch, BORDER * inch, 
                      LARGE_HEIGHT * inch, LARGE_WIDTH * inch)
    c.rect(BORDER * inch, BORDER * inch, LARGE_HEIGHT * inch, LARGE_WIDTH * inch, 
           stroke=1, fill=0)
    c.setTitle('%s - %.1f' % (title, ride.distance))
    c.setAuthor('SABikeRides.com')
    c.save()

def ride_profiles_to_pdfs(xml_tree, prof_dir, prof_base, out_dir, out_base):
    """
    Convert the large overall profile for each ride in a rideset into a PDF
    file.

    @param xml_tree: C{ElementTree} representation of a rideset
    @type xml_tree: C{ElementTree} stuff
    @param prof_dir: directory containing the profile PNG files
    @type prof_dir: C{string}
    @param prof_base: base name for profile PNG file names
    @type prof_base: C{string}
    @param out_dir: directory to put PDF files into
    @type out_dir: C{string}
    @param out_base: base name for PDF files
    @type out_base: C{string}
    """
    sabx = parse_top_level(xml_tree)
    ride_list, bounds = process_rides(xml_tree)
    for ride in ride_list:
        _large_profile_to_pdf(sabx['title'], ride,
                              prof_dir, prof_base, out_dir, out_base)
