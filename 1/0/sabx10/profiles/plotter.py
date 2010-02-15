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
Handle the plotting of profile data and saving the profile to a file.
"""
import math
import os.path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from sabx10.oxm import mile_feet

from consts import SMALL_WIDTH, SMALL_HEIGHT, LARGE_WIDTH, LARGE_HEIGHT, \
    FONT_POINTS_PER_INCH, FONT_NAME, LABEL_FONT_SIZE, ANNO_FONT_SIZE

def _poly_gen(distances, elevations):
    """
    Generator to provide the plot fill data for a graph based on a list of
    distances (X axis) and elevations (Y axis).  Fill data is a grade-dependant
    color and x and y co-ordinates needed to specify a polygon on the graph so
    it can be filled in with the proper color.

    @param distances: C{list} of distances for points in segment being plotted
    @type distances: C{list} of C{float}
    @param elevations: C{list} of elevations for point in segment being plotted
    @type elevations: C{list} of C{float}

    @return: (x1, x2), (y1, y2), color
    @rtype: (C{float},C{float}), (C{float},C{float}), C{string}
    """
    colors = {0: '1.0',
              1: '0.9',
              2: '0.8',
              3: '0.7',
              4: '0.6',
              5: '0.5',
              6: '0.4',
              7: '0.3',
              8: '0.2',
              9: '0.1',
              10: '0.0'}

    for x in range(len(distances)-1):
        if distances[x+1]-distances[x] == 0:
            grade = 0;
        else:
            grade = ((elevations[x+1]-elevations[x])/
                     ((distances[x+1]-distances[x]) * mile_feet)) * 100.0
        grade = math.trunc(grade)
        grade = max(0, grade)
        grade = min(10, grade)

        yield (distances[x], distances[x+1]), \
            (elevations[x], elevations[x+1]), \
            colors[grade]

class ProfilePlotter(object):
    """
    Generates a profile file.

    @ivar ride: L{Ride} to process
    @type ride: L{Ride}
    @ivar graph_filebase: base name for profile files
    @type graph_filebase: C{string}
    @ivar graph_dir: directory to write profile files into
    @type graph_dir: C{string}
    @ivar dpi: resolution of profile file
    @type dpi: C{int}
    @ivar min_anno_dist: minimum distance between annotations
    @type min_anno_dist: C{float}
    @ivar longest: length of longest segment
    @type longest: C{float}
    @ivar lowest: lowest elevation
    @type lowest: C{float}
    @ivar highest: highest elevation
    @type highest: C{float}
    """
    ### initialize ###
    def _calc_most_least(self):
        """
        Go through the segments for the ride and find the longest segment, the
        lowest elevation, and the highest elevation.
        """
        self.longest = 0.0
        self.lowest = 20000.0
        self.highest = 0.0

        for seg in self.ride.segs:
            seg_lowest, seg_highest = seg.find_lowest_highest()
            self.lowest = min(self.lowest, seg_lowest)
            self.highest = max(self.highest, seg_highest)
            self.longest = max(self.longest, seg.length)

    def __init__(self, ride, graph_filebase, graph_dir, dpi):
        """
        Save the passed-in data and generate calculated instance data.

        @param ride: L{Ride} to process
        @type ride: L{Ride}
        @param graph_filebase: base name for profile files
        @type graph_filebase: C{string}
        @param graph_dir: directory to write profile files into
        @type graph_dir: C{string}
        @param dpi: resolution of profile file
        @type dpi: C{int}
        """
        self.ride = ride
        self.graph_filebase = graph_filebase
        self.graph_dir = graph_dir
        self.dpi = dpi
        self.min_anno_dist = self.ride.distance / 50.0
        self._calc_most_least()

    def _set_min_anno_dist(self, inch_width):
        """
        Calculate and set the min_ann_dist for the plot.  This is how far apart
        annotations need to be before they overlap.

        @param inch_width: width of profile, in inches
        @type inch_width: C{float}
        """
        plot_inch_width = inch_width * 0.7
        label_inch_width = (float(ANNO_FONT_SIZE) / float(FONT_POINTS_PER_INCH))
        miles_per_inch = self.ride.distance / plot_inch_width
        miles_per_label = miles_per_inch * label_inch_width
        self.min_anno_dist = miles_per_label * 1.1

    def _normalize_elevation(self, elevation):
        """
        Normalize an elevation in relation to the lowest elevation in the ride,
        such that the lowest elevation in the ride will be at an elevation of
        zero.

        @param elevation: elevation to normalize
        @type elevation: C{float}

        @return: normalized elevation
        @rtype: C{float}
        """
        return elevation - self.lowest

    def _normalize_elevations(self, elevations):
        """
        Normalize all the elevations in the list.

        @param elevations: C{list} of elevations to normalize
        @type elevations: C{list} of C{float}
        """
        return [self._normalize_elevation(ele) for ele in elevations]

    def _plot_graph(self, distances, elevations, length):
        """
        Plot the graph of the distances and elevations.  Fill-in under the
        graph based on the grade between points.

        @param distances: C{list} of distances to plot
        @type distances: C{list} of C{float}
        @param elevations: C{list} of elevations corresponding to the distances
        @type elevations: C{list} of C{float}
        @param length: length of set of points being plotted
        @type length: C{float}
        """
        elevations = self._normalize_elevations(elevations)
        for x, y, color in _poly_gen(distances, elevations):
            plt.fill_between(x, y, color=color, edgecolor=color)
        plt.plot(distances, elevations, scalex=False, scaley=False)
        plt.axis([0.0, max(length, 1.0), 0.0, self.highest - self.lowest])

    def _filter_annotations(self, annotations):
        """
        Take the annotation list and remove annotations that are too close to
        the ones next to it, to prevent overlap.

        @param annotations: list of annotations to filter
        @type annotations: C{list} of L{Annotation}
        """
        prev_dist = 0.0
        ann_dist = 0.0
        filtered = []

        for anno in annotations:
            ann_dist += anno.dist - prev_dist
            prev_dist = anno.dist
            if ann_dist >= self.min_anno_dist:
                filtered.append(anno)
                ann_dist = 0.0

        return filtered

    def _normalize_annotations(self, annotations):
        """
        Normalize the elevations of the annotation points.

        @param annotations: list of annotations to filter
        @type annotations: C{list} of L{Annotation}

        @return: list of filtered annotations
        @rtype: C{list} of L{Annotation}
        """
        for anno in annotations:
            anno.ele = self._normalize_elevation(anno.ele)
        return annotations

    def _plot_annotations(self, annotations):
        """
        Add the annotations to the current plot (if there are any). Filter and
        normalize them first.

        @param annotations: list of annotations to filter
        @type annotations: C{list} of L{Annotation}
        """
        if annotations is None:
            return

        annotations = self._filter_annotations(annotations)
        annotations = self._normalize_annotations(annotations)
        for anno in annotations:
            plt.annotate(anno.text, (anno.dist, anno.ele), xytext=(-4,20), 
                         textcoords='offset points',
                         arrowprops=dict(arrowstyle="->", relpos=(0.5,0.0)),
                         rotation='vertical', 
                         fontname=FONT_NAME, fontsize=ANNO_FONT_SIZE)

    def _plot_profile(self, distances, elevations, length, annotations):
        """
        Graph the distances, elevations, and annotations on the current plot.

        @param distances: list of distances for the plot
        @type distances: C{list} of C{float}
        @param elevations: list of elevations for the plot
        @type elevations: C{list} of C{float}
        @param length: overall length of plot
        @type length: C{float}
        @param annotations: annotations for the plot
        @type annotations: C{list} of L{Annotation}
        """
        plt.grid(False)
        self._plot_graph(distances, elevations, length)
        self._plot_annotations(annotations)

    def _save_profile(self, seg_index, size_name):
        """
        Save the current plot to a file.

        @param seg_index: index of segment being plotted
        @type seg_index: C{int}
        @param size_name: size name being plotted
        @type size_name: C{string}
        """
        file_name = '%s_prof_%s_%s_%s.png' % (self.graph_filebase, size_name,
                                              self.ride.index, seg_index)
        plt.savefig(os.path.join(self.graph_dir, file_name), dpi=self.dpi) 
        plt.close()

    def plot_small_profile(self, distances, elevations, length, 
                           seg_index='all', annotations=None):
        """
        Plot a small sized profile.

        @param distances: list of distances for the plot
        @type distances: C{list} of C{float}
        @param elevations: list of elevations for the plot
        @type elevations: C{list} of C{float}
        @param length: overall length of plot
        @type length: C{float}
        @param seg_index: index of segment being plotted
        @type seg_index: C{int}
        @param annotations: annotations for the plot
        @type annotations: C{list} of L{Annotation}
        """
        self._set_min_anno_dist(SMALL_WIDTH)
        plt.figure(1, figsize=(SMALL_WIDTH, SMALL_HEIGHT))

        self._plot_profile(distances, elevations, length, annotations)
        self._save_profile(seg_index, 'small')

    def plot_large_profile(self, distances, elevations, length, 
                           seg_index='all', annotations=None):
        """
        Plot a large sized profile.

        @param distances: list of distances for the plot
        @type distances: C{list} of C{float}
        @param elevations: list of elevations for the plot
        @type elevations: C{list} of C{float}
        @param length: overall length of plot
        @type length: C{float}
        @param seg_index: index of segment being plotted
        @type seg_index: C{int}
        @param annotations: annotations for the plot
        @type annotations: C{list} of L{Annotation}
        """
        self._set_min_anno_dist(LARGE_WIDTH)
        plt.figure(1, figsize=(LARGE_WIDTH, LARGE_HEIGHT))
        plt.xlabel('Distance (miles)', fontname=FONT_NAME, fontsize=LABEL_FONT_SIZE)
        plt.ylabel('Elevation (feet)', fontname=FONT_NAME, fontsize=LABEL_FONT_SIZE)
        if annotations is None:
            plt.title('Profile', fontname=FONT_NAME, fontsize=LABEL_FONT_SIZE)
        else:
            plt.box(False)
            plt.axhline(y=0.001, color='black')
            plt.axvline(color='black')

        self._plot_profile(distances, elevations, length, annotations)
        self._save_profile(seg_index, 'large')
