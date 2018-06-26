#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')
from xml.etree import ElementTree

from cerebellum_value_map.cerebellum_map import AnotatedPolygon, ColorConverter
from cerebellum_value_map.cerebellum_map import Anotation


points = [(100, 100), (100, 200), (200, 200), (200, 100)]
value = 0.5
anot = dict(text='test', position='right')
cc = ColorConverter()
polygon = AnotatedPolygon(points, value, anot, cc)
print(ElementTree.tostring(polygon.get_xml()))
