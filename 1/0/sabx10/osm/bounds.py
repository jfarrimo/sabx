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
Pixel-size aware bounding box and its derivatives.
"""
import math

from sabx10.oxm import Box, Point

from consts import HEIGHT, WIDTH, PPI

class Bounds(Box):
    """
    Bounding box that understands pixel sizes in addition to the basic lat/lon
    sizes.  You need this because a Mapnik map is rendered into a PNG file,
    which has its size defined in terms of pixels, while the map data is
    represented in terms of lat/lon co-ordinates.

    @ivar pix_width: width of box in pixels
    @type pix_width: C{float}
    @ivar pix_height: height of box in pixels
    @type pix_height: C{float}
    """
    def __init__(self, min_lat=200.0, min_lon=200.0, 
                 max_lat=-200.0, max_lon=-200.0, box=None):
        """
        Initialize the bounds, either from explicit lat/lon coordinates, or
        based on the size of a given Box.

        @param min_lat: minimum latitude of box
        @type min_lat: C{float}
        @param min_lon: minimum longitude of box
        @type min_lon: C{float}
        @param max_lat: maximum latitude of box
        @type max_lat: C{float}
        @param max_lon: maximum longitude of box
        @type max_lon: C{float}
        @param box: example box to base this one on
        @type box: L{Box}
        """
        if box is not None:
            Box.__init__(self, box.min_lat, box.min_lon, 
                         box.max_lat, box.max_lon)
        else:
            Box.__init__(self, min_lat, min_lon, max_lat, max_lon)
        self.pix_width = 0
        self.pix_height = 0

    def expand_to_good_size(self, perc):
        """
        Resize the bounding box so that the width and height have the correct
        aspect ratio, and so that the box is a certain percent bigger than the
        map indicates.  This way any icons and street names drawn near the edge
        of the map won't get clipped.

        @param perc: percentage to expand map (0.xx format)
        @type perc: C{float}
        """
        width = self.width()
        height = self.height()

        if (self.pix_height / self.pix_width) > (height / width):
            height = (self.pix_height / self.pix_width) * width
        elif (self.pix_width / self.pix_height) > (width / height):
            width = (self.pix_width / self.pix_height) * height

        height *= 1.0 + perc
        width *= 1.0 + perc

        self.resize(width, height)

    def set_pixel_size(self):
        """
        Set the pixel width and height of this box to the desired width and
        height based on whether the map is taller that it's wide, or wider than
        it's tall.
        """
        if self.width() > self.height():
            self.pix_width = HEIGHT * PPI
            self.pix_height = WIDTH * PPI
        else:
            self.pix_width = WIDTH * PPI
            self.pix_height = HEIGHT * PPI

    def calc_sep_dist(self, pix_icon_width, pix_icon_height):
        """
        Calculate how far apart two points in this bounding box need to be so
        that their icons won't overlap.

        @param pix_icon_width: pixel width of icon being considered
        @type pix_icon_width: C{float}
        @param pix_icon_height: pixel height of icon being considered
        @type pix_icon_height: C{float}

        @return: distance apart, in statute miles, the icons must be
        @rtype: C{float}
        """
        buf_width = (self.width() / self.pix_width) * pix_icon_width
        buf_height = (self.height() / self.pix_height) * pix_icon_height
        buf_dist = math.hypot(buf_width, buf_height)

        return buf_dist

class Cluster(Bounds, Point):
    """
    Keeps track of a cluster of points and the bounding box surrounding them.

    @ivar center: L{Point} denoting center of the box
    @type center: L{Point}
    @ivar point_count: how many points this box encompasses
    @type point_count: C{int}
    @ivar index: index of this Cluster
    @type index: C{int}
    """
    def __init__(self, lat, lon): 
        """
        The bounding box starts out as just a single point.

        @param lat: latitude of starting point
        @type lat: C{float}
        @param lon: longitude of starting point
        @type lon: C{float}
        """
        Bounds.__init__(self, lat, lon, lat, lon)
        Point.__init__(self, lat, lon)
        self.point_count = 1
        self.index = 0

    def expand_to_point(self, lat, lon):
        """
        Expand the bounding box to include the given point, and include the new
        point in the point count.

        @param lat: latitude of new point
        @type lat: C{float}
        @param lon: longitude of new point
        @type lon: C{float}
        """
        Box.expand_to_point(self, lat, lon)
        self.lat = (self.min_lat + self.max_lat) / 2.0
        self.lon = (self.min_lon + self.max_lon) / 2.0
        self.point_count += 1

    def distance_from(self, pt):
        """
        How far away from the center of this box is the given point?

        @param pt: L{Point} to check against
        @type pt: L{Point}
        """
        return self.calculate_distance(pt)

    def set_pixel_size(self):
        """
        Adjust the size of the cluster's bounding box and update it's center
        point to reflect this.  A L{Cluster}'s bounding box size is simply half
        the width and half the height of the overall desired width and height.
        This is because clustered points are drawn as simple PNGs that should
        fit four on a page in a grid, and half width and half height yield a
        quarter of the area of the full page.
        """
        self.pix_width = int((WIDTH * PPI) / 2)
        self.pix_height = int((HEIGHT * PPI) / 2)
