# -*- coding: utf-8 -*-

from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from py_singleton import Singleton
from svgwrite.container import Defs
from svgwrite.path import Path
from svgwrite.pattern import Pattern
from svgwrite.shapes import Rect


class ColorConverter(metaclass=Singleton):

    def __init__(self, min_color_value=-1, max_color_value=1, colormap='RdBu_r',
                 max_disabling_value=0.05, pattern_name='stripe'):
        self.max_disabling_value = max_disabling_value
        self.pattern_name = pattern_name
        norm = Normalize(vmin=min_color_value, vmax=max_color_value)
        self.colormap = ScalarMappable(norm, cmap=colormap)

    def convert(self, color_value, disabling_value=-float('inf')):
        if  disabling_value <= self.max_disabling_value:
            color = self.colormap.to_rgba(color_value, bytes=True)[:3]
            result = 'rgb(%s)' % ', '.join([str(c) for c in color])
        else:
            result = "url(#%s)" % (self.pattern_name)
        return result


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
