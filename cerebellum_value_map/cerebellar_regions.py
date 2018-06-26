# -*- coding: utf-8 -*-

from .polygon import AnotatedPolygon


class RightX(AnotatedPolygon):
    def __init__(self, value):
        points = [(327, 270), (350, 285), (392, 290), (392, 279), (357, 276),
                  (327, 254)]
        super().__init__(points, value, {'text':'R X', 'position':'right'})


class RightIX(AnotatedPolygon):
    def __init__(self, value):
        points = [(327, 230), (327, 254), (354, 276), (392, 272), (358, 222)]
        super().__init__(points, value, {'text':'R IX', 'position':'right'})


class RightVIII(AnotatedPolygon):
    def __init__(self, value):
        points = [(327, 230), (327, 206), (356, 200), (356, 230)]
        super().__init__(points, value, {'text':'R VIII', 'position':'right'})


class RightVIIB(AnotatedPolygon):
    def __init__(self, value):
        points = [(356, 205.194), (327, 206), (327, 196), (356, 192.133)]
        super().__init__(points, value, {'text':'R VIIB', 'position':'right'})

class RightCrusII(AnotatedPolygon):
    def __init__(self, value):
        points = [(356, 181.387), (356, 194.682), (327, 196), (327, 181)]
        super().__init__(points, value, {'text':'R Crus II', 'position':'right'})


class RightCrusI(AnotatedPolygon):
    def __init__(self, value):
        points = [(356, 163.098), (356, 184.085), (327, 181), (327, 173)]
        super().__init__(points, value, {'text':'R Crus I', 'position':'right'})


class RightVI(AnotatedPolygon):
    def __init__(self, value):
        points = [(354.614, 135), (356, 135), (356, 169.617), (327, 173),
                  (327, 150)]
        super().__init__(points, value, {'text':'R VI', 'position':'right'})


class RightIV(AnotatedPolygon):
    def __init__(self, value):
        points = [(300, 90), (356, 98.296), (356, 147.149), (300, 153)]
        super().__init__(points, value, {'text':'R IV', 'position':'right'})


class VermisX(AnotatedPolygon):
    def __init__(self, value):
        points = [(300, 254), (300, 270), (327, 270), (327, 254)]
        super().__init__(points, value, {'text':'Vermis', 'position':'bottom'})


class VermisIX(AnotatedPolygon):
    def __init__(self, value):
        points = [(300, 230), (300, 254), (327, 254), (327, 230)]
        super().__init__(points, value, {'text':'', 'position':'bottom'})


class VermisVIII(AnotatedPolygon):
    def __init__(self, value):
        points = [(300, 206), (300, 230), (327, 230), (327, 206)]
        super().__init__(points, value, {'text':'', 'position':'bottom'})


class VermisVII(AnotatedPolygon):
    def __init__(self, value):
        points = [(300, 173), (300, 206), (327, 206), (327, 173)]
        super().__init__(points, value, {'text':'', 'position':'bottom'})


class VermisVI(AnotatedPolygon):
    def __init__(self, value):
        points = [(300, 153), (300, 173), (327, 173), (327, 150)]
        super().__init__(points, value, {'text':'', 'position':'bottom'})

#     lob_path_codes['right VIII medial zone'] = 
#     lob_path_codes['right VIII lateral zone 1'] = "M 451 253 L 392 272 L 356 230 L 356 200 L 363 197.2 Z"
#     lob_path_codes['right VIIB medial zone'] = 
#     lob_path_codes['right VIIB lateral zone 1'] = "M 462 230 L 451 253 L 363 205 L 356 205.194 L 356 192.133 L 372 190 Z"
#     lob_path_codes['right VII Crus II medial zone'] = 
#     lob_path_codes['right VII Crus II lateral zone 1'] = "M 356 194.682 L 356 181.387 L 416 182.187 L 416 211.802 L 371 194 Z"
#     lob_path_codes['right VII Crus II lateral zone 2'] = "M 416 182.19 L 477 183.003 L 462 230.003 L 416 211.805 Z"
#     lob_path_codes['right VII Crus I medial zone'] = 
#     lob_path_codes['right VII Crus I lateral zone 1'] = "M 416 142.61 L 416 184.777 L 374 186 L 356 184.085 L 356 163.098 Z"
#     lob_path_codes['right VII Crus I lateral zone 2'] = "M 450 131 L 477 183 L 416 184.777 L 416 142.61 Z"
#     lob_path_codes['right VI medial zone'] = 
#     lob_path_codes['right VI lateral zone 1'] = "M 408 106 L 450 131 L 387 166 L 356 169.617 L 356 134.247 Z"
#     lob_path_codes['right anterior lobe medial zone'] = 
#     lob_path_codes['right anterior lobe lateral zone 1'] = "M 356 147.149 L 356 98.296 L 408 106 L 367 146 Z"
#     lob_path_codes['vermis X right zone'] = 
#     lob_path_codes['vermis IX right zone'] = 
#     lob_path_codes['vermis VIII right zone'] = 
#     lob_path_codes['vermis VII right zone'] = "
#     lob_path_codes['vermis VI right zone'] = 
