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

    def left_right_flip(self, axis_x):
        raise NotImplementedError

    def translate(self, x, y):
        raise NotImplementedError


class AnotatedShape(Group, Shape):

    def __init__(self, shape, anotation_text='', anotation_position='right',
                 coloring_value=0, disabling_value=-float('inf')):
        super().__init__()
        self.shape = shape
        self.anotation_text = anotation_text
        self.anotation_position = anotation_position
        self.coloring_value = coloring_value
        self.disabling_value = disabling_value

        color_converter = ColorConverter()
        color = color_converter.convert(coloring_value, disabling_value)
        value = Value(coloring_value, shape)
        anotation = Anotation(anotation_text, anotation_position, shape)
        self.add(shape.get_svg(fill=color)) 
        self.add(value)
        self.add(anotation)

    def left_right_flip(self, axis_x):
        flipped_shape = self.shape.left_right_flip(axis_x)
        return AnotatedShape(flipped_shape, self.anotation_text,
                             self.anotation_position, self.coloring_value,
                             self.disabling_value)

    def translate(self, x, y):
        shape = self.shape.translate(x, y)
        return AnotatedShape(shape, self.anotation_text,
                             self.anotation_position, self.coloring_value,
                             self.disabling_value)


class Polygon(Shape):
    def __init__(self, points):
        self._points = points

    @property
    def points(self):
        return np.array(self._points)

    def get_svg(self, **kwargs):
        return PolygonSVG(self._points, **kwargs)
