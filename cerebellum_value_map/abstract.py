# -*- coding: utf-8 -*-
from svgwrite.container import Group


class BoundingBox:
    @property
    def up(self):
        raise NotImplementedError
    @property
    def bottom(self):
        raise NotImplementedError
    @property
    def left(self):
        raise NotImplementedError
    @property
    def right(self):
        raise NotImplementedError
    @property
    def h_center(self):
        raise NotImplementedError
    @property
    def v_center(self):
        raise NotImplementedError


class AnotatedPart(Group):
    def __init__(self):
        super().__init__()
