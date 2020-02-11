# -*- coding: utf-8 -*-

from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from py_singleton import Singleton
from svgwrite.container import Defs
from svgwrite.path import Path
from svgwrite.pattern import Pattern
from svgwrite.shapes import Rect


class ColorConverter_(metaclass=Singleton):

    def __init__(self, min_color_value=-2, max_color_value=2, colormap='RdBu',
                 max_disabling_value=0.05, pattern_name='stripe'):
        self.max_disabling_value = max_disabling_value
        self.pattern_name = pattern_name
        norm = Normalize(vmin=min_color_value, vmax=max_color_value)
        self.colormap = ScalarMappable(norm, cmap=colormap)
        print(norm)

    def convert(self, color_value, disabling_value=-float('inf')):
        if disabling_value <= self.max_disabling_value:
            color = self.colormap.to_rgba(color_value, bytes=True)[:3]
            result = 'rgb(%s)' % ', '.join([str(c) for c in color])
        else:
            result = 'url(#%s)' % (self.pattern_name)
        return result


class ColorConverter():
    def convert(self, color_value, disabling_value=None):
        if color_value == 0:
            return 'rgb(255, 255, 255)'
        elif color_value == 1:
            return 'rgb(255, 225, 25)'
        elif color_value == 2:
            return 'rgb(245, 130, 49)'
        elif color_value == 3:
            return 'rgb(230, 25, 75)'
        elif color_value == -1:
            return 'rgb(66, 212, 244)'
        elif color_value == -2:
            return 'rgb(67, 99, 216)'
        elif color_value == -3:
            return 'rgb(70, 153, 144)'


class LabelColorConverter():
    def convert(self, label, disabling_value=None):
        if label == 0:
            return 'rgb(0, 0, 0)'
        elif label == 12:
            return 'rgb(255, 255, 150)'
        elif label == 33:
            return 'rgb( 88,  95, 255)'
        elif label == 36:
            return 'rgb( 53,  55, 143)'
        elif label == 43:
            return 'rgb(175,  52, 255)'
        elif label == 46:
            return 'rgb( 91,  33, 132)'
        elif label == 53:
            return 'rgb( 36, 140, 255)'
        elif label == 56:
            return 'rgb( 31,  91, 163)'
        elif label == 60:
            return 'rgb(255, 190,  10)'
        elif label == 63:
            return 'rgb(252,   0, 146)'
        elif label == 66:
            return 'rgb(185,   0, 106)'
        elif label == 70:
            return 'rgb(102, 204, 255)'
        elif label == 73:
            return 'rgb(255, 143,  13)'
        elif label == 74:
            return 'rgb(255,   1,  10)'
        elif label == 75:
            return 'rgb(255, 203,  22)'
        elif label == 76:
            return 'rgb(218, 108,  15)'
        elif label == 77:
            return 'rgb(193,   8,  12)'
        elif label == 78:
            return 'rgb(202, 150,  15)'
        elif label == 80:
            return 'rgb(125,  43, 183)'
        elif label == 83:
            return 'rgb( 13, 191, 108)'
        elif label == 84:
            return 'rgb(153, 238,  18)'
        elif label == 86:
            return 'rgb( 16, 127,  72)'
        elif label == 87:
            return 'rgb(108, 168,  13)'
        elif label == 90:
            return 'rgb(253,  74,   8)'
        elif label == 93:
            return 'rgb(  8, 237, 237)'
        elif label == 96:
            return 'rgb( 10, 160, 209)'
        elif label == 100:
            return 'rgb(123, 194,   5)'
        elif label == 103:
            return 'rgb(177, 131,   0)'
        elif label == 106:
            return 'rgb(122,  83,   0)'


class Stripe(Defs):
    def __init__(self):
        # from https://philiprogers.com/svgpatterns/#thinstripes
        super().__init__()
        rect = Rect(insert=(0, 0), size=(5, 5), fill='#9e9e9e')
        path = Path('M 0 5 L 5 0 Z M 6 4 L 4 6 Z M -1 1 L 1 -1 Z',
                    stroke='#888', stroke_width=1)
        pattern = Pattern(id=self.__class__.__name__.lower(),
                          patternUnits='userSpaceOnUse',
                          size=(5, 5), stroke='none')
        pattern.add(rect)
        pattern.add(path)
        self.add(pattern)
