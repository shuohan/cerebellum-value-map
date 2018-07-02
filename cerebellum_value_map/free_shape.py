# -*- coding: utf-8 -*-

import numpy as np
from svgwrite.path import Path

from .shape import Shape
from .color import ColorConverter
from .text import Anotation, Value


class PathCode:
    command = ''

    def __init__(self, *points):
        print(points)
        self.points = points

    def __str__(self):
        pattern = '%s ' + ' '.join(['%.3f, %.3f'] * len(self.points))
        return pattern % (self.command, *[c for p in self.points for c in p])

    def __repr__(self):
        print(self.points)
        pattern = '%s(' + ', '.join(['(%.3f, %.3f)'] * len(self.points)) + ')'
        return pattern % (self.command, *[c for p in self.points for c in p])

    def flip(self, axis):
        points = [(2 * axis - p[0], p[1]) for p in self.points]
        return self.__class__(*points)

    def translate(self, x, y):
        points = [(p[0] + x, p[1] + y)  for p in self.points]
        return self.__class__(*points)


class Move(PathCode):
    command = 'M'


class Line(PathCode):
    command = 'L'


class QuadraticCurve(PathCode):
    command = 'Q'


class BezierCurve(PathCode):
    command = 'C'


class FreeShape(Shape, PathCode):

    def __init__(self, move, *codes, close=True):
        self.codes = [move] + list(codes)
        self.close = True

    def __str__(self):
        path_codes = [str(c) for c in self.codes]
        if self.close:
            path_codes.append('Z')
        return ' '.join(path_codes)

    def get_svg(self, **kwargs):
        path = Path([str(self)], **kwargs)
        return path

    def flip(self, axis_x):
        flipped_codes = list()
        for code in self.codes:
            flipped_codes.append(code.flip(axis_x))
        print(flipped_codes)
        return FreeShape(*flipped_codes, close=self.close)

    def __repr__(self):
        return ',\n'.join([repr(code) for code in self.codes])

    @property
    def points(self):
        points = np.array([code.points[-1] for code in self.codes])
        print(points)
        return points

    def translate(self, x, y):
        codes = [code.translate(x, y) for code in self.codes]
        return FreeShape(*codes, close=self.close)
