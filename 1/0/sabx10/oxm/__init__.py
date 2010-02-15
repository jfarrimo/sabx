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
Overview
========

The C{oxm} package reads and manipulates data from files in the SABX 1.0 file
format.  It makes very heavy use of the C{ElementTree} XML handling library to
do this.  C{ElementTree} is part of Python's Standard Library and is documented
there.

The SABX 1.0 file format is described at
U{http://www.sabikerides.com/sabx/1/0/}. One thing to notice is the distinction
between ride and rideset.  A rideset is comprised of one or more rides, usually
in the same geographic area.  It may be easier to think of a ride as a route,
and remember that a you can have different routes through an area.

There are two main ways to use this package.  The first is to take a file
containing SABX data and parse it into an object hierarchy that closely
resembles the SABX XML file.  This is useful when you're manipulating the XML
files themselves.  I use this for doing things like re-numbering id's, adding
USGS elevations to a file, converting to a different format, etc...  All the
functions with "parse" in their names are primarily used for this.  The
L{sabx10.oxm.parse} module explains this more fully.

The second way to use the package is to take a file containing SABX data and
process it into a ride-centric hierarchy that gives all the pertinent
information for each ride, fleshing-out the stop, POI, turn, segment, and
parking information that is a simple reference in the file.  This way you can
very easily access the SABX data in an object hierarchy that is not as memory
efficient as the native SABX file, but which is much more logically attuned to
how you would use it for presentation.  The functions with "process" in their
names work together to accomplish this.  The L{sabx10.oxm.ride} module goes
into more detail about this.

There are also a host of auxiliary uses for this library, and the functions it
contains can typically be mixed-and-matched as necessary.  Still, by thinking
of things as "parse" vs. "process", you'll be in tune with how the library
usage has evolved over time.

It's important to know that all of the functions in this library expect
C{ElementTree} C{Element}s that have been stripped of their default namespace
information. This way they don't have to specify the whole namespace string
when querying for elements in the tree.  The function
L{sabx10.oxm.utils.parse_no_def_namespaces} handles this and should always be
used to create C{Element} representations of SABX files.

Also, make note of the fact that this library has been designed without any
consideration to memory usage or speed.  It is generally used in scripts that
are run as part of a build process and has been optimized for usability over
efficiency.  Beware of this.

By the way, the name C{oxm} is my lame attempt at humour.  I like to think of
the parsing portion of this package as an "object-XML mapper", kind of like the
"object-relational mapper (orm)" concept from the database world.  Therefore, I
coined the name C{oxm} as a take-off on the acronym C{orm}.

Copyright
=========

The sabx10.oxm package constitutes sabx10.oxm.

sabx10.oxm - an SABX file manipulation library
Copyright (C) 2009, 2010 Jay Farrimond (jay@sabikerides.com)

sabx10.oxm is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

sabx10.oxm is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
details.

You should have received a copy of the GNU Lesser General Public License along
with sabx10.oxm.  If not, see U{http://www.gnu.org/licenses/}.
"""
from geom import Point, Box
from parking import Parking
from parse import parse_tree, parse_top_level, parse_history, parse_photos
from poi import Poi
from ride import process_rides, Ride
from segment import parse_segments, Segment
from stop import Stop
from turn import Turn
from utils import meter_feet, mile_feet, pt_dist_from_pt, VersionException, \
    parse_no_def_namespaces
