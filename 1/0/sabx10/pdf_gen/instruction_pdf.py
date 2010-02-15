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
Take table data and turn it into PDF files. Reportlab is used to generate the
PDF files.
"""
import os.path

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

from sabx10.map import BORDER

from consts import COL_WIDTH_1, COL_WIDTH_2, COL_WIDTH_4, COL_WIDTH_ALL

class InstructionPdfGenerator(object):
    def __init__(self, title, out_dir, out_base):
        """
        Save the title, out_dir, and out_base, then setup the style sheet and
        column widths.

        @param title: base title for the PDF file
        @type title: C{string}
        @param out_dir: directory to write the PDF files to
        @type out_dir: C{string}
        @param out_base: file name base for PDF files
        @type out_base: C{string}
        """
        self.title = title
        self.out_dir = out_dir
        self.out_base = out_base

        stylesheet = getSampleStyleSheet()
        self.normalStyle = stylesheet['Normal']
        self.headerStyle = stylesheet['Heading3']

        page_width, page_height = letter
        self.colWidths = [COL_WIDTH_1 * inch, 
                          COL_WIDTH_2 * inch, 
                          page_width - \
                              (BORDER * 2.0 * inch) - (COL_WIDTH_ALL * inch), 
                          COL_WIDTH_4 * inch]

    def _create_titles(self):
        """
        Create the column headers for the output table.

        @return: tuple of C{Paragraph}s containing ("Landmark", "Distance",
        "Description", "Length")
        @rtype: (C{Paragraph},C{Paragraph},C{Paragraph},C{Paragraph})
        """
        return (
            Paragraph("Landmark", self.headerStyle),
            Paragraph("Distance", self.headerStyle),
            Paragraph("Description", self.headerStyle),
            Paragraph("Length", self.headerStyle)
            )

    def _massage_table_data(self, table_data):
        """
        Turn the titles and generic table data into objects recognized and
        properly formatted by Reportlab.  Basically, turn the description field
        from a regular C{string} into a C{Paragraph} so it'll be wrapped
        properly.

        @param table_data: data to format
        @type table_data: C{list} of (C{string},C{string},C{string},C{string})

        @return: new C{list} with processed data
        @rtype: C{list} of (C{string},C{string},C{Paragraph},C{string})
        """
        processed = [self._create_titles()]
        for line in table_data:
            processed.append( (line[0], line[1], 
                               Paragraph(line[2], self.normalStyle), line[3]) )
        return processed

    def process_ride(self, index, distance, table_data):
        """
        Take table data for a ride and turn it into a PDF file containing the
        table.

        @param index: index of ride
        @type index: C{int}
        @param distance: length of ride
        @type distance: C{float}
        @param table_data: C{list} of (landmark, distance, description, length)
        @type table_data: C{list} of (C{string},C{string},C{string},C{string})
        """
        table_data = self._massage_table_data(table_data)
    
        tbl = Table(table_data, colWidths=self.colWidths, repeatRows=1)
        tbl.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'LEFT'),
                                 ('VALIGN', (0,0), (-1,-1), 'TOP'),
                                 ('GRID', (0,0), (-1,-1), 1, colors.black)]))
        doc_name = "%s_%s.pdf" % (self.out_base, index)
        doc_name = os.path.join(self.out_dir, doc_name)
        doc = SimpleDocTemplate(doc_name, 
                                title="%s - %.1f Miles" % (self.title, 
                                                           distance),
                                author="SABikeRides.com",
                                pagesize=letter,
                                leftMargin = BORDER * inch,
                                rightMargin = BORDER * inch,
                                topMargin = BORDER * inch,
                                bottomMargin = BORDER * inch)
        doc.build([tbl])
