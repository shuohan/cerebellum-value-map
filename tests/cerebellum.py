#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')
from xml.etree import ElementTree

from cerebellum_value_map.cerebellum import *

from svgwrite import Drawing
from svgwrite.container import Group


drawing = Drawing('test.svg', size=('600', '400'), stroke_width=2,
                  font_size=12, stroke='black')

right_i2iii = RightLobuleI2III(0.3)
right_iv = RightLobuleIV(0.4)
right_v = RightLobuleV(0.5)
right_vi = RightLobuleVI(0.6)
right_crusi = RightLobuleCrusI(0.72)
right_crusii = RightLobuleCrusII(0.74)
right_viib = RightLobuleVIIB(0.76)
right_viiia = RightLobuleVIIIA(0.83)
right_viiib = RightLobuleVIIIB(0.86)
right_ix = RightLobuleIX(0.9)
right_x = RightLobuleX(1)

vermis_vi = VermisVI()
vermis_vii = VermisVII()
vermis_viii = VermisVIII()
vermis_ix = VermisIX()
vermis_x = VermisX()

drawing.add(right_i2iii)
drawing.add(right_iv)
drawing.add(right_v)
drawing.add(right_vi)
drawing.add(right_crusi)
drawing.add(right_crusii)
drawing.add(right_viib)
drawing.add(right_viiia)
drawing.add(right_viiib)
drawing.add(right_ix)
drawing.add(right_x)
drawing.add(vermis_vi)
drawing.add(vermis_vii)
drawing.add(vermis_viii)
drawing.add(vermis_ix)
drawing.add(vermis_x)

drawing.save(pretty=True)
