# -*- coding: utf-8 -*-

import numpy as np
from svgwrite.container import Group
from svgwrite.path import Path

from .color import ColorConverter
from .path_code import PathCode, Move, Line, QuadraticCurve, BezierCurve
from .text import Value, Annotation


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

    def flip(self, axis_x):
        flipped_codes = list()
        for code in self.codes:
            flipped_codes.append(code.flip(axis_x))
        return self.__class__(*flipped_codes, close=self.close)

    def translate(self, x, y):
        codes = [code.translate(x, y) for code in self.codes]
        return self.__class__(*codes, close=self.close)


class AnnotatedShape_(Group, Shape):

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
        annotation = Annotation(annotation_text, annotation_position, shape)
        self.add(shape.get_svg(fill=color)) 
        self.add(value)
        self.add(annotation)


class AnnotatedShape(AnnotatedShape_):

    axis = 270.312
    show_annotation = False
    _shape = None
    _annotation_text = ''
    _annotation_position = 'right'

    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        annotation_text = self._annotation_text if self.show_annotation else ''
        super().__init__(self._shape, annotation_text=annotation_text,
                         annotation_position=self._annotation_position,
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
