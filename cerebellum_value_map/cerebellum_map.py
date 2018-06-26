#!/usr/bin/env python
# -*- coding: utf-8 -*-

import svgwrite
from svgwrite.path import Path
from svgwrite.shapes import Polygon
from svgwrite.text import Text
from svgwrite.container import Group
from itertools import count

from collections import OrderedDict, defaultdict
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

import numpy as np


class Anotation:
    def __init__(self, text, position):
        self.text = text
        self.position = position


class AnotatedPolygon(Group):

    _num_ids = count(0)

    def __init__(self, points, value, anat, color_converter, **kwargs):
        super().__init__(**kwargs)
        self._id = str(next(self._num_ids))
        self.color_converter = color_converter
        self.polygon = self._build_polygon(points, value)
        self.value = self._build_value(points, value)
        self.anat = self._build_anat(points, anat)
        self.add(self.polygon)
        self.add(self.value)
        self.add(self.anat)

    def _build_polygon(self, points, value):
        color = self.color_converter.convert(value)
        id = self._calcualte_id('polygon')
        polygon = Polygon(points=points, fill=color, id=id)
        return polygon

    def _convert_points(self, points):
        result = list()
        for point in points:
            result.append('%f,%f' % point)
        return result

    def _calcualte_id(self, text):
        id = '_'.join([self.__class__.__name__, text, self._id])
        return id

    def _build_value(self, points, value):
        left, right, bottom, up = self._calculate_bbox(points)
        x = (left + right) / 2
        y = (bottom + up) / 2
        text = Text(str(value), stroke='none', x=[x], y=[y],
                    alignment_baseline='middle', text_anchor='middle')
        return text

    def _calculate_bbox(self, points):
        points = np.array(points)
        left = np.min(points[:, 0])
        right = np.max(points[:, 0])
        bottom = np.min(points[:, 1])
        up = np.max(points[:, 1])
        return left, right, bottom, up

    def _build_anat(self, points, anat):
        left, right, bottom, up = self._calculate_bbox(points)
        if anat.position == 'right':
            x = right
            y = (bottom + up) / 2
            text_anchor = 'start'
            alignment_baseline = 'middle'
        if anat.position == 'left':
            x = right 
            y = (bottom + up) / 2
            text_anchor = 'end'
            alignment_baseline = 'middle'
        if anat.position == 'up':
            x = (right + left) / 2
            y = up
            text_anchor = 'middle'
            alignment_baseline = 'baseline'
        if anat.position == 'bottom':
            x = (right + left) / 2
            y = bottom
            text_anchor = 'middle'
            alignment_baseline = 'hanging'
        text = Text(anat.text, stroke='none', text_anchor=text_anchor,
                    alignment_baseline=alignment_baseline)
        return text


class ColorConverter:
    def __init__(self, min_value=-1, max_value=1, colormap='RdBu_r'):
        norm = Normalize(vmin=min_value, vmax=max_value)
        self.colormap = ScalarMappable(norm, cmap='RdBu_r')
    def convert(self, num):
        color = self.colormap.to_rgba(num, bytes=True)[:3]
        color_string = 'rgb(%s)' % ', '.join([str(c) for c in color])
        return color_string


def create_strip_pattern():
    # from https://philiprogers.com/svgpatterns/#thinstripes
    defs = svgwrite.container.Defs()
    rect = svgwrite.shapes.Rect(insert=(0, 0), size=(5, 5), fill='#9e9e9e')
    path = Path('M0 5L5 0ZM6 4L4 6ZM-1 1L1 -1Z', stroke='#888', stroke_width=1)
    pattern = svgwrite.pattern.Pattern(id="stripe", patternUnits="userSpaceOnUse", 
                                       size=(5, 5), stroke="none")
    pattern.add(rect)
    pattern.add(path)
    defs.add(pattern)
    return defs


# def draw_colormap(colormap, insert, size, color_step=10, font_size=10):
# 
#     colormap_group = svgwrite.container.Group()
# 
#     lg = svgwrite.gradients.LinearGradient(id='lg', start=(0,1), end=(0,0))
#     for i in list(range(color_step)) + [color_step]:
#         stop = i if i == 0 else float(i) / color_step
#         color = colormap.to_rgba(stop, bytes=True, norm=False)[:3]
#         color_string = 'rgb(%s)' % ', '.join([str(c) for c in color])
#         lg.add_stop_color(offset=stop, color=color_string)
# 
#     rect = svgwrite.shapes.Rect(insert=insert, size=size, fill='url(#lg)')
# 
#     dx = size[0] + font_size
#     vmax_text = Text(str(colormap.norm.vmax), x=[insert[0]], y=[insert[1]], 
#                      stroke='none', dx=[dx], font_size=font_size,
#                      alignment_baseline='hanging')
#     vmin_text = Text(str(colormap.norm.vmin), x=[insert[0]],
#                      y=[insert[1]+size[1]], stroke='none', dx=[dx], 
#                      alignment_baseline='middle', font_size=font_size)
#     zero_x = vmin_text.attribs['x']
#     zero_y = (float(vmin_text.attribs['y']) + float(vmax_text.attribs['y'])) / 2
#     vzero_text = Text(str(0), x=[zero_x], y=[zero_y], stroke='none', dx=[dx], 
#                       font_size=font_size, alignment_baseline='middle')
# 
#     colormap_group.add(lg)
#     colormap_group.add(rect)
#     colormap_group.add(vmin_text)
#     colormap_group.add(vmax_text)
#     colormap_group.add(vzero_text)
# 
#     return colormap_group
# 
# 
# def get_fill(color, pval):
#     if pval <= 0.05:
#         color = colormap.to_rgba(num, alpha=False, bytes=True)[:3]
#         fill = 'rgb(%s)' % ', '.join([str(c) for c in color])
#     else:
#         fill = "url(#%s)" % (pattern_name)
#     return fill
# 
# 
# def draw_cerebellum(corr_vals, p_vals, output_filename='cerebellum.svg', 
#                     vmax=1, vmin=-1):
# 
#     """
#     - corr_vals: dict, each value of the dict contains a list with the pearson
#       correaltion and the corresponding p value
#     """
# 
#     label_font_size = 10
#     default_font_size = 6
#     pattern_name = 'stripe'
# 
#     colormap = ScalarMappable(Normalize(vmin=vmin, vmax=vmax), cmap='RdBu_r')
# 
#     val_positions = dict()
# 
#     val_positions['left X total'] = dict(x=352, y=284)
#     val_positions['left IX total'] = dict(x=340, y=252)
#     val_positions['left VIII medial zone'] = dict(x=329, y=220)
#     val_positions['left VIII lateral zone 1'] = dict(x=390, y=252)
#     val_positions['left VIIB medial zone'] = dict(x=329, y=203)
#     val_positions['left VIIB lateral zone 1'] = dict(x=418, y=230)
#     val_positions['left VII Crus II medial zone'] = dict(x=329, y=191)
#     val_positions['left VII Crus II lateral zone 1'] = dict(x=380, y=195)
#     val_positions['left VII Crus II lateral zone 2'] = dict(x=435, y=205)
#     val_positions['left VII Crus I medial zone'] = dict(x=329, y=179)
#     val_positions['left VII Crus I lateral zone 1'] = dict(x=380, y=180)
#     val_positions['left VII Crus I lateral zone 2'] = dict(x=430, y=170)
#     val_positions['left VI medial zone'] = dict(x=329, y=162)
#     val_positions['left VI lateral zone 1'] = dict(x=390, y=142)
#     val_positions['left anterior lobe medial zone'] = dict(x=315, y=125)
#     val_positions['left anterior lobe lateral zone 1'] = dict(x=365, y=120)
# 
#     val_positions['right X total'] = dict(x=223, y=284)
#     val_positions['right IX total'] = dict(x=235, y=252)
#     val_positions['right VIII medial zone'] = dict(x=246, y=220)
#     val_positions['right VIII lateral zone 1'] = dict(x=185, y=252)
#     val_positions['right VIIB medial zone'] = dict(x=246, y=203)
#     val_positions['right VIIB lateral zone 1'] = dict(x=157, y=230)
#     val_positions['right VII Crus II medial zone'] = dict(x=246, y=191)
#     val_positions['right VII Crus II lateral zone 1'] = dict(x=195, y=195)
#     val_positions['right VII Crus II lateral zone 2'] = dict(x=140, y=205)
#     val_positions['right VII Crus I medial zone'] = dict(x=246, y=179)
#     val_positions['right VII Crus I lateral zone 1'] = dict(x=195, y=180)
#     val_positions['right VII Crus I lateral zone 2'] = dict(x=145, y=170)
#     val_positions['right VI medial zone'] = dict(x=246, y=162)
#     val_positions['right VI lateral zone 1'] = dict(x=185, y=142)
#     val_positions['right anterior lobe medial zone'] = dict(x=260, y=125)
#     val_positions['right anterior lobe lateral zone 1'] = dict(x=210, y=120)
# 
#     val_positions['vermis X left zone'] = dict(x=302, y=264)
#     val_positions['vermis IX left zone'] = dict(x=302, y=245)
#     val_positions['vermis VIII left zone'] = dict(x=302, y=220)
#     val_positions['vermis VII left zone'] = dict(x=302, y=191)
#     val_positions['vermis VI left zone'] = dict(x=302, y=165)
# 
#     val_positions['vermis X right zone'] = dict(x=275, y=264)
#     val_positions['vermis IX right zone'] = dict(x=275, y=245)
#     val_positions['vermis VIII right zone'] = dict(x=275, y=220)
#     val_positions['vermis VII right zone'] = dict(x=275, y=191)
#     val_positions['vermis VI right zone'] = dict(x=275, y=165)
# 
#     lob_path_codes = OrderedDict()
# 
#     lob_path_codes['right X total'] = "M 327 270 L 350 285 L 392 290 L 392 279 L 357 276 L 327 254 Z"
#     lob_path_codes['right IX total'] = "M 327 230 L 327 254 L 354 276 L 392 272 L 358 222 Z"
#     lob_path_codes['right VIII medial zone'] = "M 327 230 L 327 206 L 356 200 L 356 230 Z"
#     lob_path_codes['right VIII lateral zone 1'] = "M 451 253 L 392 272 L 356 230 L 356 200 L 363 197.2 Z"
#     lob_path_codes['right VIIB medial zone'] = "M 356 205.194 L 327 206 L 327 196 L 356 192.133 Z"
#     lob_path_codes['right VIIB lateral zone 1'] = "M 462 230 L 451 253 L 363 205 L 356 205.194 L 356 192.133 L 372 190 Z"
#     lob_path_codes['right VII Crus II medial zone'] = "M 356 181.387 L 356 194.682 L 327 196 L 327 181 Z"
#     lob_path_codes['right VII Crus II lateral zone 1'] = "M 356 194.682 L 356 181.387 L 416 182.187 L 416 211.802 L 371 194 Z"
#     lob_path_codes['right VII Crus II lateral zone 2'] = "M 416 182.19 L 477 183.003 L 462 230.003 L 416 211.805 Z"
#     lob_path_codes['right VII Crus I medial zone'] = "M 356 163.098 L 356 184.085 L 327 181 L 327 173 Z"
#     lob_path_codes['right VII Crus I lateral zone 1'] = "M 416 142.61 L 416 184.777 L 374 186 L 356 184.085 L 356 163.098 Z"
#     lob_path_codes['right VII Crus I lateral zone 2'] = "M 450 131 L 477 183 L 416 184.777 L 416 142.61 Z"
#     lob_path_codes['right VI medial zone'] = "M 354.614 135 L 356 135 L 356 169.617 L 327 173 L 327 150 Z"
#     lob_path_codes['right VI lateral zone 1'] = "M 408 106 L 450 131 L 387 166 L 356 169.617 L 356 134.247 Z"
#     lob_path_codes['right anterior lobe medial zone'] = "M 300 90 L 356 98.296 L 356 147.149 L 300 153 Z"
#     lob_path_codes['right anterior lobe lateral zone 1'] = "M 356 147.149 L 356 98.296 L 408 106 L 367 146 Z"
#     lob_path_codes['vermis X right zone'] = "M 300 254 L 300 270 L 327 270 L 327 254 Z"
#     lob_path_codes['vermis IX right zone'] = "M 300 230 L 300 254 L 327 254 L 327 230 Z"
#     lob_path_codes['vermis VIII right zone'] = "M 300 206 L 300 230 L 327 230 L 327 206 Z"
#     lob_path_codes['vermis VII right zone'] = "M 300 173 L 300 206 L 327 206 L 327 173 Z"
#     lob_path_codes['vermis VI right zone'] = "M 300 153 L 300 173 L 327 173 L 327 150 Z"
# 
#     lob_path_codes['left X total'] = lob_path_codes['right X total']
#     lob_path_codes['left IX total'] = lob_path_codes['right IX total']
#     lob_path_codes['left VIII medial zone'] = lob_path_codes['right VIII medial zone']
#     lob_path_codes['left VIII lateral zone 1'] = lob_path_codes['right VIII lateral zone 1']
#     lob_path_codes['left VIIB medial zone'] = lob_path_codes['right VIIB medial zone']
#     lob_path_codes['left VIIB lateral zone 1'] = lob_path_codes['right VIIB lateral zone 1']
#     lob_path_codes['left VII Crus II medial zone'] = lob_path_codes['right VII Crus II medial zone']
#     lob_path_codes['left VII Crus II lateral zone 1'] = lob_path_codes['right VII Crus II lateral zone 1']
#     lob_path_codes['left VII Crus II lateral zone 2'] = lob_path_codes['right VII Crus II lateral zone 2']
#     lob_path_codes['left VII Crus I medial zone'] = lob_path_codes['right VII Crus I medial zone']
#     lob_path_codes['left VII Crus I lateral zone 1'] = lob_path_codes['right VII Crus I lateral zone 1']
#     lob_path_codes['left VII Crus I lateral zone 2'] = lob_path_codes['right VII Crus I lateral zone 2']
#     lob_path_codes['left VI medial zone'] = lob_path_codes['right VI medial zone']
#     lob_path_codes['left VI lateral zone 1'] = lob_path_codes['right VI lateral zone 1']
#     lob_path_codes['left anterior lobe medial zone'] = lob_path_codes['right anterior lobe medial zone']
#     lob_path_codes['left anterior lobe lateral zone 1'] = lob_path_codes['right anterior lobe lateral zone 1']
#     lob_path_codes['vermis X left zone'] = lob_path_codes['vermis X right zone']
#     lob_path_codes['vermis IX left zone'] = lob_path_codes['vermis IX right zone']
#     lob_path_codes['vermis VIII left zone'] = lob_path_codes['vermis VIII right zone']
#     lob_path_codes['vermis VII left zone'] = lob_path_codes['vermis VII right zone']
#     lob_path_codes['vermis VI left zone'] = lob_path_codes['vermis VI right zone']
# 
#     labels = svgwrite.container.Group(font_size=label_font_size, stroke='none')
#     labels.add(Text('X', x=[220], y=[300]))
#     labels.add(Text('IX', x=[190], y=[280]))
#     labels.add(Text('VIII', x=[160], y=[275]))
#     labels.add(Text('VIIB', x=[115], y=[245]))
#     labels.add(Text('VII Crus II', x=[75], y=[210]))
#     labels.add(Text('VII Crus I', x=[90], y=[160]))
#     labels.add(Text('VI', x=[160], y=[110]))
#     labels.add(Text('Anterior', x=[220], y=[90]))
#     labels.add(Text('Vermis', x=[300], y=[285], text_anchor='middle'))
#     labels.add(Text('--> left', x=[80], y=[320], font_size=15))
# 
#     right_side = svgwrite.container.Group(transform="matrix(-1, 0, 0, 1, 600, 0)")
#     left_side = svgwrite.container.Group()
#     for k, v in lob_path_codes.items():
#         if p_vals[k] <= 0.05 :
#             fill = get_color(colormap, corr_vals[k])
#         else:
#             fill = "url(#%s)" % (pattern_name)
#         p = Path(v, id=k.replace(' ', '_'), fill=fill)
#         if 'right' in k:
#             right_side.add(p)
#         else:
#             left_side.add(p)
# 
#     val_texts = svgwrite.container.Group()
#     for k, v in corr_vals.items():
#         text = "%.2f, %.2f" % (v, p_vals[k])
#         x = val_positions[k]['x']
#         y = val_positions[k]['y']
#         if abs(v) > 0.25 * (vmax - vmin) and p_vals[k] <= 0.05:
#             color = 'white'
#         else:
#             color = 'black'
#         val_texts.add(Text(text, x=[x], y=[y], stroke='none', fill=color))
# 
#     colormap_group = draw_colormap(colormap, (550, 100), (10, 200), font_size=12) 
# 
#     drawing = svgwrite.Drawing(output_filename, size=('600', '400'), 
#                           stroke_width=0.2, font_size=default_font_size, 
#                           stroke='black')
#     pattern = get_pattern(pattern_name)
#     drawing.add(pattern)
#     drawing.add(right_side)
#     drawing.add(left_side)
#     drawing.add(labels)
#     drawing.add(val_texts)
#     drawing.add(colormap_group)
# 
#     drawing.save(pretty=True)
# 
# 
# def main():
# 
#     output_filename = "test.svg"
#     default_val = 0.015 
# 
#     vals = dict()
# 
#     vals['left X total'] = default_val
#     vals['left IX total'] = default_val
#     vals['left VIII medial zone'] = default_val
#     vals['left VIII lateral zone 1'] = default_val
#     vals['left VIIB medial zone'] = default_val
#     vals['left VIIB lateral zone 1'] = default_val
#     vals['left VII Crus II medial zone'] = default_val
#     vals['left VII Crus II lateral zone 1'] = default_val
#     vals['left VII Crus II lateral zone 2'] = default_val
#     vals['left VII Crus I medial zone'] = default_val
#     vals['left VII Crus I lateral zone 1'] = default_val
#     vals['left VII Crus I lateral zone 2'] = default_val
#     vals['left VI medial zone'] = default_val
#     vals['left VI lateral zone 1'] = default_val
#     vals['left anterior lobe medial zone'] = default_val
#     vals['left anterior lobe lateral zone 1'] = default_val
# 
#     vals['right X total'] = default_val
#     vals['right IX total'] = default_val
#     vals['right VIII medial zone'] = default_val
#     vals['right VIII lateral zone 1'] = default_val
#     vals['right VIIB medial zone'] = default_val
#     vals['right VIIB lateral zone 1'] = default_val
#     vals['right VII Crus II medial zone'] = default_val
#     vals['right VII Crus II lateral zone 1'] = default_val
#     vals['right VII Crus II lateral zone 2'] = default_val
#     vals['right VII Crus I medial zone'] = default_val
#     vals['right VII Crus I lateral zone 1'] = default_val
#     vals['right VII Crus I lateral zone 2'] = default_val
#     vals['right VI medial zone'] = default_val
#     vals['right VI lateral zone 1'] = default_val
#     vals['right anterior lobe medial zone'] = default_val
#     vals['right anterior lobe lateral zone 1'] = default_val
# 
#     vals['vermis X left zone'] = default_val
#     vals['vermis IX left zone'] = default_val
#     vals['vermis VIII left zone'] = default_val
#     vals['vermis VII left zone'] = default_val
#     vals['vermis VI left zone'] = default_val
# 
#     vals['vermis VI right zone'] = default_val
#     vals['vermis VII right zone'] = default_val
#     vals['vermis VIII right zone'] = default_val
#     vals['vermis IX right zone'] = default_val
#     vals['vermis X right zone'] = default_val
# 
#     draw_cerebellum(vals, vals, output_filename=output_filename)
# 
# 
# if __name__ == '__main__':
#     main()
