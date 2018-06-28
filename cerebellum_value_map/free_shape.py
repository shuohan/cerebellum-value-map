# -*- coding: utf-8 -*-

from svgwrite.path import Path

from .shape import Shape
from .color import ColorConverter
from .text import Anotation, Value


class PathCode:
    def __init__(self, end_point):
        self.end_point = end_point

    def get_path_code(self):
        raise NotImplementedError


class Move(PathCode):
    def get_path_code(self):
        return 'M %.3f,%.3f' % tuple(self.end_point)


class Line(PathCode):
    def get_path_code(self):
        return 'L %.3f,%.3f' % tuple(self.end_point)


class QuadraticCurve(PathCode):
    def __init__(self, handle, end_point):
        self.handle = handle
        super().__init__(end_point)

    def get_path_code(self):
        return 'Q %.3f,%.3f %.3f,%.3f' % (*self.handle, *self.end_point)


class BezierCurve(PathCode):
    def __init__(self, start_handle, end_handle, end_point):
        self.start_handle = start_handle
        self.end_handle = end_handle
        super().__init__(end_point)

    def get_path_code(self):
        return 'C %.3f,%.3f %.3f,%.3f %.3f,%.3f' % (*self.start_handle,
                                                    *self.end_handle,
                                                    *self.end_point)


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

    @property
    def points(self):
        return np.array([code.end_point for code in self.codes])
