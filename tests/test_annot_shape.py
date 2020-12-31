#!/usr/bin/env python3

from xml.etree import ElementTree

from cerebellum_value_map.path_code import Line, Move
from cerebellum_value_map.shape import AnnotatedShape, PathShape
from cerebellum_value_map.colors import DiscreteColors


def test_annot_shape():
    colors = DiscreteColors()
    annot_txt = 'text'
    annot_pos = 'right'

    shape = PathShape(Move([100, 100]), Line([100, 200]),
                      Line([200, 200]), Line([200, 100]))
    assert str(shape) == ('M 100.000, 100.000 L 100.000, 200.000 '
                          'L 200.000, 200.000 L 200.000, 100.000 Z')

    shape = AnnotatedShape(shape, value=1, annot_txt=annot_txt,
                           annot_pos=annot_pos, show_annot=True)

    print(ElementTree.tostring(shape.get_svg().get_xml()).decode())
    assert ElementTree.tostring(shape.get_svg().get_xml()).decode() \
        == ('<g><path d="M 100.000, 100.000 L 100.000, 200.000 '
            'L 200.000, 200.000 L 200.000, 100.000 Z" '
            'fill="rgb(255, 225, 25)" /><text alignment-baseline="middle" '
            'stroke="none" text-anchor="start" '
            'x="200" y="150.0">text</text></g>')


if __name__ == '__main__':
    test_annot_shape()
    print('success')
