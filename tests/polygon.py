#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')
from xml.etree import ElementTree

from cerebellum_value_map.cerebellum_map import AnotatedPolygon, ColorConverter
from cerebellum_value_map.cerebellum_map import Anotation


points = [(100, 100), (100, 200), (200, 200), (200, 100)]
value = 0.5

cc = ColorConverter()
print(cc.convert(value))

anat = Anotation('rect', 'left')
polygon = AnotatedPolygon(points, value, anat, cc)
print(ElementTree.tostring(polygon.get_xml()))
