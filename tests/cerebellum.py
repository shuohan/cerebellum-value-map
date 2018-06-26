#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')
from xml.etree import ElementTree

from cerebellum_value_map.cerebellar_regions import *

from svgwrite import Drawing
from svgwrite.container import Group


drawing = Drawing('test.svg', size=('600', '400'), stroke_width=0.2,
                  font_size=12, stroke='black')

value = {'color':0, 'disabling':0}
right_x = RightX(value)
right_ix = RightIX(value)
right_viii = RightVIII(value)
right_viib = RightVIIB(value)
right_crus_ii = RightCrusII(value)
right_crus_i = RightCrusI(value)
right_vi = RightVI(value)
vermis_x = VermisX(value)
vermis_ix = VermisIX(value)
vermis_viii = VermisVIII(value)
vermis_vii = VermisVII(value)
vermis_vi = VermisVI(value)

drawing.add(right_x)
drawing.add(right_ix)
drawing.add(right_viii)
drawing.add(right_viib)
drawing.add(right_crus_ii)
drawing.add(right_crus_i)
drawing.add(right_vi)
drawing.add(vermis_x)
drawing.add(vermis_ix)
drawing.add(vermis_viii)
drawing.add(vermis_vii)
drawing.add(vermis_vi)

drawing.save(pretty=True)
