#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
sys.path.insert(0, '..')
import pandas as pd

from cerebellum_value_map.cerebellum import CerebellumValueMap

data = {'color':[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
        'disable':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
index = ['right_anterior_lobe', 'left_anterior_lobe',
         'right_superioer_posterior_lobe', 'left_superior_posterior_lobe',
         'right_inferior_posterior_lobe', 'left_inferior_posterior_lobe',
         'right_lobule_x', 'left_lobule_x', 'vermis', 'corpus_medullare']
df = pd.DataFrame(data, index=index)

CerebellumValueMap(df, 'test.svg', show_color=False)
