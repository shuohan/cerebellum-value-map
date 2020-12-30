#!/usr/bin/env python


import pandas as pd

from cerebellum_value_map.utils import convert_pvals


def test_pvals():
    df = pd.DataFrame([['A', 0.2, 1],
                       ['B', 0.015, -1],
                       ['C', 0.005, -1],
                       ['D', 0.0001, 1]])
    df.columns = ['name', 'pval', 'sign']
    df = df.set_index('name')
    df = convert_pvals(df)

    ref = pd.DataFrame([['A', 0],
                        ['B', -1],
                        ['C', -2],
                        ['D', 3]])
    ref.columns = ['name', 'value']
    ref = ref.set_index('name')
    assert ref.equals(df)

    df = pd.DataFrame([['A', 0.2],
                       ['B', 0.015],
                       ['C', 0.005],
                       ['D', 0.0001]])
    df.columns = ['name', 'pval']
    df = df.set_index('name')
    df = convert_pvals(df)

    ref = pd.DataFrame([['A', 0],
                        ['B', 1],
                        ['C', 2],
                        ['D', 3]])
    ref.columns = ['name', 'value']
    ref = ref.set_index('name')
    assert ref.equals(df)

if __name__ == '__main__':
    test_pvals()
    print('success')
