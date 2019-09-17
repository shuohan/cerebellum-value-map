#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Show cerebellum value map')
parser.add_argument('-i', '--input-data')
parser.add_argument('-o', '--output-svg')
parser.add_argument('-p', '--is-pvalue-mode', default=False,
                    action='store_true')

args = parser.parse_args()

import sys
import pandas as pd
import numpy as np

from cerebellum_value_map.color import ColorConverter
from cerebellum_value_map.cerebellum import CerebellumValueMap


# def convert_pval(pval, sign, rev=True):
#     if pval > 0.05:
#         result = 0
#     elif pval > 0.01:
#         result = 1
#     elif pval > 0.001:
#         result = 2
#     else:
#         result = 3
#     result *= np.sign(sign)
#     if rev:
#         result *= -1
#     return result

def convert_pval(pval, sign, rev=True):
    if pval > 0.01:
        result = 0
    elif pval > 0.001:
        result = 1
    else:
        result = 2
    # elif pval > 0.001:
    #     result = 2
    # else:
    #     result = 3
    result *= np.sign(sign)
    if rev:
        result *= -1
    return result
    
data = pd.read_csv(args.input_data, index_col=0)
if args.is_pvalue_mode:
    cc = ColorConverter(min_color_value=-4, max_color_value=4)
    for index, row in data.iterrows():
        data.at[index, 'color'] = convert_pval(data.at[index, 'color'],
                                               data.at[index, 'sign'])

map = CerebellumValueMap(data, args.output_svg, stroke_width=1)
map.size = (373, 366)
map.translate(-84, -50)
print(map.left)
print(map.right)
print(map.up)
print(map.bottom)
map.save()
