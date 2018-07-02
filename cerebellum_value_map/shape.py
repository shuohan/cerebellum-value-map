# -*- coding: utf-8 -*-

import numpy as np
from svgwrite.container import Group

from .color import ColorConverter
from .text import Value, Anotation


class Shape:
    
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

    def get_svg(self, **kwargs):
        raise NotImplementedError

    def flip(self, axis):
        raise NotImplementedError

    def translate(self, x, y):
        raise NotImplementedError


class AnnotatedShape(Group, Shape):

    def __init__(self, shape, annotation_text='', annotation_position='right',
                 coloring_value=0, disabling_value=-float('inf')):
        super().__init__()
        self.shape = shape
        self.annotation_text = annotation_text
        self.annotation_position = annotation_position
        self.coloring_value = coloring_value
        self.disabling_value = disabling_value

        color_converter = ColorConverter()
        color = color_converter.convert(coloring_value, disabling_value)
        value = Value(coloring_value, shape)
        annotation = Anotation(annotation_text, annotation_position, shape)
        self.add(shape.get_svg(fill=color)) 
        self.add(value)
        self.add(annotation)
