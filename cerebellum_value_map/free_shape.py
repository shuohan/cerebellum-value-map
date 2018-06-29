# -*- coding: utf-8 -*-

import numpy as np
from svgwrite.path import Path

from .shape import Shape
from .color import ColorConverter
from .text import Anotation, Value


class PathCode:
    def __init__(self, end_point):
        self.end_point = end_point

    def get_path_code(self):
        raise NotImplementedError

    def flip(self, axis_x):
        end_point = self._flip_point(self.end_point, axis_x)
        return self.__class__(end_point)

    def _flip_point(self, point, axis_x):
        return (2 * axis_x - point[0], point[1])

    def __str__(self):
        raise NotImplementedError


class Move(PathCode):
    def get_path_code(self):
        return 'M %.3f,%.3f' % tuple(self.end_point)
    def __str__(self):
        return 'M((%.3f, %.3f))' % tuple(self.end_point)

class Line(PathCode):
    def get_path_code(self):
        return 'L %.3f,%.3f' % tuple(self.end_point)
    def __str__(self):
        return 'L((%.3f, %.3f))' % tuple(self.end_point)


class QuadraticCurve(PathCode):
    def __init__(self, handle, end_point):
        self.handle = handle
        super().__init__(end_point)

    def get_path_code(self):
        return 'Q %.3f,%.3f %.3f,%.3f' % (*self.handle, *self.end_point)

    def flip(self, axis_x):
        handle = self._flip_point(self.handle, axis_x)
        end_point = self._flip_point(self.end_point, axis_x)
        return self.__class__(handle, end_point)

    def __str__(self):
        return 'Q((%.3f, %.3f), (%.3f, %.3f))' % (*self.handle, *self.end_point)


class BezierCurve(PathCode):
    def __init__(self, start_handle, end_handle, end_point):
        self.start_handle = start_handle
        self.end_handle = end_handle
        super().__init__(end_point)

    def get_path_code(self):
        return 'C %.3f,%.3f %.3f,%.3f %.3f,%.3f' % (*self.start_handle,
                                                    *self.end_handle,
                                                    *self.end_point)

    def flip(self, axis_x):
        start_handle = self._flip_point(self.start_handle, axis_x)
        end_handle = self._flip_point(self.end_handle, axis_x)
        end_point = self._flip_point(self.end_point, axis_x)
        return self.__class__(start_handle, end_handle, end_point)

    def __str__(self):
        result = 'C((%.3f, %.3f), (%.3f, %.3f), (%.3f, %.3f))'
        return result % (*self.start_handle, *self.end_handle, *self.end_point)


class FreeShape(Shape, PathCode):

    def __init__(self, move, *codes, close=True):
        self.codes = [move] + list(codes)
        self.close = True

    def get_path_code(self):
        path_codes = [c.get_path_code() for c in self.codes]
        if self.close:
            path_codes.append('Z')
        return ' '.join(path_codes)

    def get_svg(self, **kwargs):
        path = Path([self.get_path_code()], **kwargs)
        return path

    def left_right_flip(self, axis_x):
        flipped_codes = list()
        for code in self.codes:
            flipped_codes.append(code.flip(axis_x))
        return FreeShape(*flipped_codes, close=self.close)

    def __str__(self):
        return '\n'.join([code.__str__() for code in self.codes])

    @property
    def points(self):
        return np.array([code.end_point for code in self.codes])
