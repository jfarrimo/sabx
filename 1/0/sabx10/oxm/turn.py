###############################################################################
#
# sabx10.oxm - an SABX file manipulation library
# Copyright (C) 2009, 2010 Jay Farrimond (jay@sabikerides.com)
#
# This file is part of sabx10.oxm.
#
# sabx10.oxm is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# sabx10.oxm is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with sabx10.oxm.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
"""
Turn handling.
"""
from geom import Point
from utils import get_from_id

############################################################
# XML
############################################################

class Turn(Point):
    """
    A C{Turn} object sub-classes L{Point} and adds fromto, cue, and comments to
    describe a turn.  Turns don't natively have C{lat} and C{lon} values set,
    since the SABX file doesn't have those for turns.  Those values typically
    get set when a turn is processed.

    @ivar fromto: from segment to segment
    @type fromto: C{string}
    @ivar cue: instructions for executing the turn
    @type cue: C{string}
    @ivar comments: additional info about the turn
    @type comments: C{string}
    """
    def __init__(self, id, fromto, cue, comments):
        """
        Save the passed-in data.

        @param id: id of the turn
        @type id: C{string}
        @param fromto: from segment to segment
        @type fromto: C{string}
        @param cue: instructions for executing the turn
        @type cue: C{string}
        @param comments: additional info about the turn
        @type comments: C{string}
        """
        Point.__init__(self, id=id)
        self.fromto = fromto
        self.cue = cue
        self.comments = comments

def _parse_turn_xml(xml_turn):
    """
    Take the C{Element} for a turn and turn it into a L{Turn} object.

    @param xml_turn: C{Element} for a turn
    @type xml_turn: C{Element}

    @return: L{Turn} object
    @rtype: L{Turn}
    """
    return Turn(id = xml_turn.attrib['id'],
                fromto = xml_turn.findtext('fromto'),
                cue = xml_turn.findtext('cue'),
                comments = xml_turn.findtext('comments'))

def parse_turns(xml_tree):
    """
    Get all the turn elements in the given C{Element} tree and create a list of
    them with L{Turn} objects.

    @param xml_tree: root of C{Element} tree that has turns in it
    @type xml_tree: C{Element} or C{ElementTree}

    @return: L{Turn}s in a list and a dictionary
    @rtype: (C{list} of L{Turn},C{dict} of L{Turn})
    """
    xml_turns = xml_tree.findall('turn')
    turn_list = []
    turn_dict = {}
    for xml_turn in xml_turns:
        new_turn = _parse_turn_xml(xml_turn)
        turn_list.append(new_turn)
        turn_dict[new_turn.id]= new_turn

    return turn_list, turn_dict

############################################################
# RIDE
############################################################

def process_ride_turns(ride_segs, xml_ride, xml_turns):
    """
    Process the turn references for the given ride and generate a list of
    L{Turn} objects for it.

    @param ride_segs: C{list} of L{Segment} objects for the ride
    @type ride_segs: C{list} of L{Segment} objects
    @param xml_ride: C{Element} root of ride data tree
    @type xml_ride: C{Element}
    @param xml_turns: C{list} of C{Element} turn objects
    @type xml_turns: C{list} of C{Element}s

    @return: C{list} of L{Turn}
    @rtype: C{list} of L{Turn}
    """
    ride_turns = [_parse_turn_xml(get_from_id(xml_turns, xml_turn.attrib['id']))
                  for xml_turn in xml_ride.findall('turn_ref')]

    # sanity check
    if len(ride_segs) != len(ride_turns):
        raise Exception('turn and seg counts do not match')

    # process segs
    for index, (turn, seg) in enumerate(zip(ride_turns, ride_segs)):
        turn.comments = " ".join(turn.comments.split())
        turn.distance = seg.start_dist
        turn.lat = seg.lat
        turn.lon = seg.lon
        turn.index = index

    return ride_turns
