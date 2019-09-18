# -*- coding: utf-8 -*-

from svgwrite import Drawing

from .lobes import RightAnteriorLobe, RightSuperiorPosteriorLobe
from .lobes import RightInferiorPosteriorLobe, Vermis
from .lobes import LeftAnteriorLobe, LeftSuperiorPosteriorLobe
from .lobes import LeftInferiorPosteriorLobe
from .lobules import CorpusMedullare
from .lobules import RightLobulesI2III, LeftLobulesI2III
from .lobules import RightLobuleIV, LeftLobuleIV
from .lobules import RightLobuleV, LeftLobuleV
from .lobules import RightLobuleVI, LeftLobuleVI
from .lobules import RightCrusI, LeftCrusI
from .lobules import RightCrusII, LeftCrusII
from .lobules import RightLobuleVIIB, LeftLobuleVIIB
from .lobules import RightLobuleVIIIA, LeftLobuleVIIIA
from .lobules import RightLobuleVIIIB, LeftLobuleVIIIB
from .lobules import RightLobuleIX, LeftLobuleIX
from .lobules import RightLobuleX, LeftLobuleX
from .lobules import VermisVI
from .lobules import VermisVII
from .lobules import VermisVIII
from .lobules import VermisIX
from .lobules import VermisX


def create(name, coloring_value=0, disabling_value=float('-inf'),
           show_color=False):
    name = ''.join([n[0].upper()+n[1:].replace('-', '2')
                    for n in name.split('_')])
    region = eval(name)(coloring_value, disabling_value, show_color)
    return region


class CerebellumValueMap:

    def __init__(self, data, output_filename, show_color=False, font_size=12,
                 stroke='black', stroke_width=2, size=(550, 450)):
        self.data = data
        self.output_filename = output_filename
        self.show_color = show_color
        self.font_size = font_size
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.size = size
        self.drawing = None
        self.regions = self._get_regions()

    @property
    def size(self):
        return tuple(int(num) for num in self._size)

    @size.setter
    def size(self, size):
        self._size = tuple(str(num) for num in size)

    def _get_regions(self):
        regions = list()
        for index, values in self.data.iterrows():
            regions.append(create(index, coloring_value=values['color'],
                                  disabling_value=values['disable'],
                                  show_color=self.show_color))
        return regions

    def translate(self, x, y):
        self.regions = [r.translate(x, y) for r in self.regions]

    def scale(self, f):
        self.regions = [r.scale(f) for r in self.regions]

    @property
    def left(self):
        return min(region.left for region in self.regions)

    @property
    def right(self):
        return max(region.right for region in self.regions)

    @property
    def up(self):
        return min(region.up for region in self.regions)

    @property
    def bottom(self):
        return max(region.bottom for region in self.regions)

    def save(self):
        self.drawing = Drawing(self.output_filename,
                               size=self._size,
                               stroke=self.stroke,
                               stroke_width=self.stroke_width,
                               font_size=self.font_size)
        for region in self.regions:
            self.drawing.add(region.get_svg())
        self.drawing.save(pretty=True)
