# -*- coding: utf-8 -*-


class PathCode:
    command = ''

    def __init__(self, *points):
        self.points = points

    def __repr__(self):
        pattern = '%s(' + ', '.join(['(%.3f, %.3f)'] * len(self.points)) + ')'
        return pattern % (self.command, *[c for p in self.points for c in p])

    def __str__(self):
        pattern = '%s ' + ' '.join(['%.3f, %.3f'] * len(self.points))
        return pattern % (self.command, *[c for p in self.points for c in p])

    def flip(self, axis):
        points = [(2 * axis - p[0], p[1]) for p in self.points]
        return self.__class__(*points)

    def translate(self, x, y):
        points = [(p[0] + x, p[1] + y)  for p in self.points]
        return self.__class__(*points)

    def scale(self, f):
        points = [(p[0] * f, p[1] * f) for p in self.points]
        return self.__class__(*points)


class Move(PathCode):
    command = 'M'


class Line(PathCode):
    command = 'L'


class QuadraticCurve(PathCode):
    command = 'Q'


class BezierCurve(PathCode):
    command = 'C'
