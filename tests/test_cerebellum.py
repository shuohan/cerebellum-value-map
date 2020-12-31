#!/usr/bin/env python3

import pandas as pd
from pathlib import Path

from cerebellum_value_map.cerebellum import CerebellumValueMap
from cerebellum_value_map.cerebellum import CerebellumLabelMap


dirname = Path('results')
dirname.mkdir(exist_ok=True)

def test_value_map():
    data = pd.DataFrame([['Right Anterior', 1], ['Vermis', -2]])
    data.columns = ['name', 'value']
    data = data.set_index('name')
    filename = dirname.joinpath('value_map.svg')
    vmap = CerebellumValueMap(data, filename, show_annot=True,
                              show_value_txt=True)
    vmap.save()

def test_label_map():
    filename = dirname.joinpath('label_map.svg')
    names = ['Right I-III', 'Left VI']
    lmap = CerebellumLabelMap(names, filename, show_annot=False)
    lmap.save()

if __name__ == '__main__':
    test_value_map()
    test_label_map()
