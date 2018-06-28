# -*- coding: utf-8 -*-

from svgwrite.text import Text


class Anotation(Text):
    def __init__(self, text, position, shape):
        self.shape = shape
        super().__init__(text, **self._get_prop(position), stroke='none')

    def _get_prop(self, position):
        if position == 'right':
            prop = self._put_right()
        if position == 'left':
            prop = self._put_left()
        if position == 'up':
            prop = self._put_up()
        if position == 'bottom':
            prop = self._put_bottom()
        return prop

    def _put_right(self):
        prop = dict(x=[self.shape.right],
                    y=[self.shape.v_center],
                    text_anchor='start',
                    alignment_baseline='middle')
        return prop

    def _put_left(self):
        prop = dict(x=[self.shape.right],
                    y=[self.shape.v_center],
                    text_anchor='end',
                    alignment_baseline='middle')
        return prop

    def _put_up(self):
        prop = dict(x=[self.shape.h_center],
                    y=[self.shape.up],
                    text_anchor='middle',
                    alignment_baseline='baseline')
        return prop

    def _put_bottom(self):
        prop = dict(x=[self.shape.h_center],
                    y=[self.shape.bottom],
                    text_anchor='middle',
                    alignment_baseline='hanging')
        return prop


class Value(Text):
    def __init__(self, value, shape):
        super().__init__(str(value), stroke='none', 
                         x=[shape.h_center], y=[shape.v_center],
                         alignment_baseline='middle', text_anchor='middle')
