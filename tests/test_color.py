#!/usr/bin/env python


from cerebellum_value_map.colors import CerebellumLabelColors


def test_colors():
    colors = CerebellumLabelColors()
    assert colors.get_color(77) == 'rgb(193, 8, 12)'
    assert colors.get_color_from_name('Right I-III') == 'rgb(53, 55, 143)'

if __name__ == '__main__':
    test_colors()
    print('success')
