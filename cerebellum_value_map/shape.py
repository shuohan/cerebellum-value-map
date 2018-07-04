# -*- coding: utf-8 -*-

import numpy as np
from svgwrite.container import Group
from svgwrite.path import Path

from .color import ColorConverter
from .path_code import PathCode
from .text import Value, Annotation


class Shape:

    @property
    def points(self):
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

    def get_svg(self, **kwargs):
        raise NotImplementedError

    def flip(self, axis):
        raise NotImplementedError

    def translate(self, x, y):
        raise NotImplementedError


class PathShape(Shape, PathCode):

    def __init__(self, *codes, close=True):
        self.codes = list(codes)
        self.close = True

    def __repr__(self):
        return ',\n'.join([repr(code) for code in self.codes])

    def __str__(self):
        path_codes = [str(c) for c in self.codes]
        if self.close:
            path_codes.append('Z')
        return ' '.join(path_codes)

    @property
    def points(self):
        points = np.array([code.points[-1] for code in self.codes])
        return points

    def get_svg(self, **kwargs):
        path = Path([str(self)], **kwargs)
        return path

    def flip(self, axis):
        flipped_codes = list()
        for code in self.codes:
            flipped_codes.append(code.flip(axis))
        return self.__class__(*flipped_codes, close=self.close)

    def translate(self, x, y):
        codes = [code.translate(x, y) for code in self.codes]
        return self.__class__(*codes, close=self.close)


class AnnotatedShape_(Shape):

    def __init__(self, shape, annotation_text='', annotation_position='right',
                 coloring_value=0, disabling_value=-float('inf'),
                 show_color=False):
        super().__init__()
        color_converter = ColorConverter()
        self.shape = shape
        self.color = color_converter.convert(coloring_value, disabling_value)
        self.annotation_text = annotation_text
        self.annotation_position = annotation_position
        self.coloring_value = coloring_value
        self.show_color = show_color

    def get_svg(self, **kwargs):
        group = Group(**kwargs)
        group.add(self.shape.get_svg(fill=self.color))
        if len(self.annotation_text) > 0:
            group.add(Annotation(self.annotation_text, self.annotation_position,
                                 self.shape))
        if self.show_color:
            group.add(Value(self.coloring_value, self.shape))
        return group


class AnnotatedShape(AnnotatedShape_):

    _shape = None
    _annotation_text = ''
    _annotation_position = 'right'

    def __init__(self, coloring_value=0, disabling_value=-float('inf'),
                 show_color=False):
        super().__init__(self._shape, annotation_text=self._annotation_text,
                         annotation_position=self._annotation_position,
                         coloring_value=coloring_value,
                         disabling_value=disabling_value,
                         show_color=show_color)
