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
Create the table data and orchestrate turning it into PDF files.
"""
from sabx10.oxm import process_rides, parse_top_level, Turn, Stop, Poi

from instruction_pdf import InstructionPdfGenerator

def _convert_turn(turn, segs):
    """
    Format a turn as a table item.

    Landmark is either "Parking" or "T - #", with # being the turn index.

    Distance is how far into the ride the turn occurs.

    Description is the turn cue.

    Length is the length of the segment turning on to, saying how long you stay
    on the road you're turning on to.

    @param turn: L{Turn} to process
    @type turn: L{Turn} object
    @param segs: segment list, to get Length from
    @type segs: C{list} of L{Segment}

    @return: tuple of (landmark, distance, description, length)
    @rtype: (C{string},C{string},C{string},C{string})
    """
    if turn.index == 0:
        landmark = "Parking"
    else:
        landmark = "T - %s" % turn.index
    distance = "%.2f" % turn.distance
    description = " ".join(turn.cue.split())
    length = "%.2f" % segs[turn.index].length

    return (landmark, distance, description, length)

def _convert_stop(stop):
    """
    Format a stop as a table item.

    Landmark is "S - #", with # being the stop index.

    Distance is how far into the ride the stop occurs.

    Description is the stop description.

    Length is filled with the stop type.

    @param stop: L{Stop} to process
    @type stop: L{Stop} object

    @return: tuple of (landmark, distance, description, length)
    @rtype: (C{string},C{string},C{string},C{string})
    """
    landmark = "S - %s" % stop.index
    if stop.off_route >= 0.1:
        distance = "%.1f + %.1f" % (stop.distance, stop.off_route)
    else:
        distance = "%.1f" % stop.distance
    if stop.off_route >= 0.1:
        description = "%s (%.1f  miles off route)" % (stop.description, 
                                                      stop.off_route)
        description = " ".join(description.split())
    else:
        description = " ".join(stop.description.split())
    length = stop.type

    return (landmark, distance, description, length)

def _convert_poi(poi):
    """
    Format a poi as a table item.

    Landmark is "P - #", with # being the poi index.

    Distance is how far into the ride the poi occurs.

    Description is the poi description.

    Length is filled with the string "POI".

    @param poi: L{Poi} to process
    @type poi: L{Poi} object

    @return: tuple of (landmark, distance, description, length)
    @rtype: (C{string},C{string},C{string},C{string})
    """
    landmark = "P - %s" % poi.index
    if poi.off_route >= 0.1:
        distance = "%.1f + %.1f" % (poi.distance, poi.off_route)
    else:
        distance = "%.1f" % poi.distance
    if poi.off_route >= 0.1:
        description = "%s (%.1f miles off route)" % (poi.description, 
                                                     poi.off_route)
        description = " ".join(description.split())
    else:
        description = " ".join(poi.description.split())
    length = "POI"

    return (landmark, distance, description, length)

def _create_table_data(ride):
    """
    Create a list of data lines to generate the PDF table from. The list is
    filled with the turns, stops, and pois for the given ride.

    @param ride: L{Ride} to process
    @type ride: L{Ride} object

    @return: C{list} of (landmark, distance, description, length)
    @rtype: C{list} of (C{string},C{string},C{string},C{string})
    """
    processed = []
    for item in ride.combined:
        if isinstance(item, Turn):
            processed.append(_convert_turn(item, ride.segs))
        elif isinstance(item, Stop):
            processed.append(_convert_stop(item))
        elif isinstance(item, Poi):
            processed.append(_convert_poi(item))

    processed.append( (
            "Finish",
            "%.2f" % ride.distance,
            "Arrive at finish!",
            "Finish"
            ))

    return processed

def pdf_all_rides(xml_tree, out_dir, out_base):
    """
    Generate instruction PDF files for each ride in a rideset.

    @param xml_tree: C{ElementTree} representation of a rideset
    @type xml_tree: C{ElementTree} stuff
    @param out_dir: directory to write the PDF files to
    @type out_dir: C{string}
    @param out_base: file name base for PDF files
    @type out_base: C{string}
    """
    sabx = parse_top_level(xml_tree)
    ride_list, bounds = process_rides(xml_tree)
    pdf_gen = InstructionPdfGenerator(sabx['title'], out_dir, out_base)
    for ride in ride_list:
        table_data = _create_table_data(ride)
        pdf_gen.process_ride(ride.index, ride.distance, table_data)
