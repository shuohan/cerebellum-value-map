# -*- coding: utf-8 -*-

import numpy as np
from svgwrite.container import Group
from svgwrite.shapes import Polygon as PolygonSVG

from .color import ColorConverter
from .text import Value, Anotation


class Shape:

    def get_svg(self):
        raise NotImplementedError

    @property
    def left(self):
        return np.min(self.points[:, 0])

    @property
    def right(self):
        return np.max(self.points[:, 0])

    @property
    def bottom(self):
        return np.max(self.points[:, 1])

    @property
    def up(self):
        return np.min(self.points[:, 1])

    @property
    def h_center(self):
        return (self.left + self.right) / 2

    @property
    def v_center(self):
        return (self.up + self.bottom) / 2


class ShapeAnotator:

    @classmethod
    def anotate(self, shape, coloring_value=None, disabling_value=-float('inf'),
                anotation_text='', anotation_position='right'):
        color_converter = ColorConverter()
        color = color_converter.convert(coloring_value, disabling_value)
        value = Value(coloring_value, shape)
        anotation = Anotation(anotation_text, anotation_position, shape)
        group = Group()
        group.add(shape.get_svg(fill=color)) 
        group.add(value)
        group.add(anotation)
        return group


class Polygon(Shape):
    def __init__(self, points):
        self._points = points

    @property
    def points(self):
        return np.array(self._points)

    def get_svg(self, **kwargs):
        return PolygonSVG(self._points, **kwargs)
