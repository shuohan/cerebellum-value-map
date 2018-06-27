#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')
from xml.etree import ElementTree

from cerebellum_value_map.polygon import AnotatedPolygon
from cerebellum_value_map.color import ColorConverter, Stripe


points = [(100, 100), (100, 200), (200, 200), (200, 100)]
value = dict(color=0.5, disabling=0.1)
anot = dict(text='test', position='right')
cc = ColorConverter()
polygon = AnotatedPolygon(points, value, anot)
stripe = Stripe()
print(ElementTree.tostring(polygon.get_xml()))
print(ElementTree.tostring(stripe.get_xml()))
