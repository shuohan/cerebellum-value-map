#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')
from svgwrite import Drawing

from cerebellum_value_map.cerebellum import RightLobuleX

drawing = Drawing('test.svg', size=('600', '400'), stroke_width=2,
                  font_size=12, stroke='black')

right_x = RightLobuleX(1)
left_x = right_x.left_right_flip(0.5)

print(right_x.shape)
print(left_x.shape)

drawing.add(right_x)
drawing.add(left_x)

drawing.save(pretty=True)
