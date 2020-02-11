#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')

from cerebellum_value_map.lobules import CorpusMedullare

cm = CorpusMedullare()
cm.shape = cm.shape.translate(-27.481, -230)
print(cm.shape.h_center)
print(cm.shape.points.shape)
print(cm.shape.points[:, 1])
