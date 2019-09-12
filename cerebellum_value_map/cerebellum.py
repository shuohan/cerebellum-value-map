# -*- coding: utf-8 -*-

from svgwrite import Drawing

from .lobes import RightAnteriorLobe, RightSuperiorPosteriorLobe
from .lobes import RightInferiorPosteriorLobe, Vermis
from .lobes import LeftAnteriorLobe, LeftSuperiorPosteriorLobe
from .lobes import LeftInferiorPosteriorLobe
from .lobules import CorpusMedullare
from .lobules import RightLobuleI2III, LeftLobuleI2III
from .lobules import RightLobuleIV, LeftLobuleIV
from .lobules import RightLobuleV, LeftLobuleV
from .lobules import RightLobuleVI, LeftLobuleVI
from .lobules import RightLobuleCrusI, LeftLobuleCrusI
from .lobules import RightLobuleCrusII, LeftLobuleCrusII
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

# from .color import Stripe


class CerebellumValueMap:

    regions = dict()

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


class CerebellumValueMapLobe(CerebellumValueMap):

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


class CerebellumValueMapLobule(CerebellumValueMap):

    regions = {'Right_Lobules_I-III': RightLobuleI2III,
               'Left_Lobules_I-III': LeftLobuleI2III,
               'Right_Lobule_IV': RightLobuleIV,
               'Left_Lobule_IV': LeftLobuleIV,
               'Right_Lobule_V': RightLobuleV,
               'Left_Lobule_V': LeftLobuleV,
               'Right_Lobule_VI': RightLobuleVI,
               'Left_Lobule_VI': LeftLobuleVI,
               'Right_Crus_I': RightLobuleCrusI,
               'Left_Crus_I': LeftLobuleCrusI,
               'Right_Crus_II': RightLobuleCrusII,
               'Left_Crus_II': LeftLobuleCrusII,
               'Right_Lobule_VIIB': RightLobuleVIIB,
               'Left_Lobule_VIIB': LeftLobuleVIIB,
               'Right_Lobule_VIIIA': RightLobuleVIIIA,
               'Left_Lobule_VIIIA': LeftLobuleVIIIA,
               'Right_Lobule_VIIIB': RightLobuleVIIIB,
               'Left_Lobule_VIIIB': LeftLobuleVIIIB,
               'Right_Lobule_IX': RightLobuleIX,
               'Left_Lobule_IX': LeftLobuleIX,
               'Right_Lobule_X': RightLobuleX,
               'Left_Lobule_X': LeftLobuleX,
               'Vermis_VI': VermisVI,
               'Vermis_VII': VermisVII,
               'Vermis_VIII': VermisVIII,
               'Vermis_IX': VermisIX,
               'Vermis_X': VermisX,
               'Corpus_medullare': CorpusMedullare}
