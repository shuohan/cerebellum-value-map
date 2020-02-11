#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')
from svgwrite import Drawing
from xml.etree import ElementTree

from cerebellum_value_map.free_shape import FreeShape
from cerebellum_value_map.free_shape import Move as M
from cerebellum_value_map.free_shape import QuadraticCurve as Q
from cerebellum_value_map.free_shape import BezierCurve as C


shape = FreeShape(M((69.23, 236.913)),
                  C((73.394, 238.949), (80.57, 242.234), (87.667, 248)),
                  C((98.333, 256.667), (99.877, 272.283), (117, 279.333)),
                  Q((128.333, 284), (135.367, 283.327)),
                  Q((146.338, 279.313), (151.356, 282.002)),
                  C((157.424, 285.255), (160.303, 292.054), (158.473, 298.686)),
                  C((156.439, 306.059), (147.397, 309.103), (141.64, 309.103)),
                  C((127.629, 309.103), (120.949, 305.77), (115.228, 301.578)),
                  C((110.928, 298.427), (107.169, 294.79), (101.245, 291.718)),
                  C((92.759, 287.318), (84.271, 285.559), (74.655, 286.093)),
                  C((60.849, 286.86), (59.315, 293.507), (57.88, 292.523)),
                  C((63.406, 287.904), (66.03, 277.828), (67.17, 272.885)),
                  C((69.198, 264.095), (69.699, 252.623), (69.23, 236.913)),
                  close=True)
shape_svg = shape.get_svg()
drawing = Drawing('test.svg', size=('600', '400'), stroke_width=0.2,
                  font_size=12, stroke='black')
drawing.add(shape_svg)
drawing.save(pretty=True)
