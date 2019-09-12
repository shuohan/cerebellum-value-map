# -*- coding: utf-8 -*-

from svgwrite import Drawing

from .lobes import RightAnteriorLobe, RightSuperiorPosteriorLobe
from .lobes import RightInferiorPosteriorLobe, Vermis
from .lobes import LeftAnteriorLobe, LeftSuperiorPosteriorLobe
from .lobes import LeftInferiorPosteriorLobe
from .lobules import RightLobuleX, LeftLobuleX, CorpusMedullare
from .color import Stripe


class CerebellumValueMap:

    regions = {'right_anterior_lobe': RightAnteriorLobe,
               'left_anterior_lobe': LeftAnteriorLobe,
               'right_superior_posterior_lobe': RightSuperiorPosteriorLobe,
               'left_superior_posterior_lobe': LeftSuperiorPosteriorLobe,
               'right_inferior_posterior_lobe': RightInferiorPosteriorLobe,
               'left_inferior_posterior_lobe': LeftInferiorPosteriorLobe,
               'right_lobule_x': RightLobuleX,
               'left_lobule_x': LeftLobuleX,
               'vermis': Vermis,
               'corpus_medullare': CorpusMedullare}

    def __init__(self, data, output_filename, show_color=False,
                 font_size=12, stroke='black', stroke_width=2, size=(550, 450)):
        drawing = Drawing(output_filename, size=[str(num) for num in size],
                          stroke=stroke, stroke_width=stroke_width,
                          font_size=font_size)
        for index, values in data.iterrows():
            region = self.regions[index](coloring_value=values['color'],
                                         disabling_value=values['disable'],
                                         show_color=show_color)
            drawing.add(region.get_svg())
        drawing.save(pretty=True)
