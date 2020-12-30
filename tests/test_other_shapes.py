#!/usr/bin/env python

import pandas as pd
from cerebellum_value_map import CerebellumValueMap
from cerebellum_value_map import AnnotatedShape, PathShape
from cerebellum_value_map import create_annot_region
from cerebellum_value_map.path_code import Move, Line


def test_other_shapes():

    def create_shape(name, value, colors=None, show_annot=False, show_value_txt=False):
        if name == 'triangle':
            shape = PathShape(Move([0, 0]), Line([100, 0]), Line([50, 50]))
            return AnnotatedShape(shape, value)
        elif name == 'rectangle':
            shape = PathShape(Move([100, 100]), Line([150, 100]),
                              Line([150, 150]), Line([100, 150]))
            return AnnotatedShape(shape, value)
        else:
            return create_annot_region(name, value)

    data = pd.DataFrame([['triangle', 1], ['rectangle', 2], ['Right Anterior', 3]])
    data.columns = ['name', 'value']
    data = data.set_index('name')
    print(data)
    drawing = CerebellumValueMap(data, 'results/other_shapes.svg',
                                 create=create_shape)
    drawing.save()

if __name__ == '__main__':
    test_other_shapes()
