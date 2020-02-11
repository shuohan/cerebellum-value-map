#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')
from xml.etree import ElementTree

from cerebellum_value_map.shape import AnotatedShape, Polygon
from cerebellum_value_map.color import ColorConverter, Stripe


cc = ColorConverter()
stripe = Stripe()

points = [(100, 100), (100, 200), (200, 200), (200, 100)]
coloring_value = 0.5
disabling_value = 0.1
anotation_text = 'test'
anotation_position = 'right'

polygon = Polygon(points)
polygon = AnotatedShape(polygon, coloring_value=coloring_value,
                        disabling_value=disabling_value,
                        anotation_text=anotation_text,
                        anotation_position=anotation_position)

print(ElementTree.tostring(stripe.get_xml()))
print(ElementTree.tostring(polygon.get_xml()))
