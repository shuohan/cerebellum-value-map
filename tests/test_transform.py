#!/usr/bin/env python3

from svgwrite import Drawing
from xml.etree import ElementTree
from pathlib import Path

from cerebellum_value_map.shape import PathShape
from cerebellum_value_map.path_code import Move, Line


dirname = Path('results')
dirname.mkdir(exist_ok=True)
shape = PathShape(Move([100, 100]), Line([120, 140]), Line([160, 100]))
drawing_orig = Drawing(dirname.joinpath('shape.svg'),
                       size=(200, 200), stroke='black', stroke_width=1)
drawing_orig.add(shape.get_svg())
drawing_orig.save()


def test_flip():
    flip = shape.flip(90)
    xml = ElementTree.tostring(flip.get_svg().get_xml()).decode()
    assert xml == ('<path d="M 80.000, 100.000 L 60.000, 140.000 '
                   'L 20.000, 100.000 Z" />')
    drawing_flip = Drawing(dirname.joinpath('flip.svg'),
                           size=(200, 200), stroke='black', stroke_width=1)
    drawing_flip.add(flip.get_svg())
    drawing_flip.save()


def test_scale():
    scale = shape.scale(0.5)
    xml = ElementTree.tostring(scale.get_svg().get_xml()).decode()
    assert xml == ('<path d="M 50.000, 50.000 L 60.000, 70.000 '
                   'L 80.000, 50.000 Z" />')
    drawing_scale = Drawing(dirname.joinpath('scale.svg'),
                           size=(200, 200), stroke='black', stroke_width=1)
    drawing_scale.add(scale.get_svg())
    drawing_scale.save()


def test_translate():
    translate = shape.translate(-50, -50)
    xml = ElementTree.tostring(translate.get_svg().get_xml()).decode()
    assert xml == ('<path d="M 50.000, 50.000 L 70.000, 90.000 '
                   'L 110.000, 50.000 Z" />')
    drawing_translate = Drawing(dirname.joinpath('translate.svg'),
                           size=(200, 200), stroke='black', stroke_width=1)
    drawing_translate.add(translate.get_svg())
    drawing_translate.save()


if __name__ == '__main__':
    test_flip()
    test_scale()
    test_translate()
    print('success')
