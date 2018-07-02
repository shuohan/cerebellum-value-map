# -*- coding: utf-8 -*-

from .free_shape import FreeShape as FS
from .free_shape import Move as M
from .free_shape import Line as L
from .free_shape import BezierCurve as C
from .free_shape import QuadraticCurve as Q
from .shape import AnotatedShape


class CerebellarRegion(AnotatedShape):
    def left_right_flip(self, coloring_value=0,
                            disabling_value=-float('inf')):
        flipped = self.shape.left_right_flip(270.312)
        anotation_text = self.anotation_text
        anotation_position = self.anotation_position
        if 'R' in anotation_text:
            anotation_text = anotation_text.replace('R', 'L')
        elif 'L' in self.anotation_text:
            anotation_text = anotation_text.replace('L', 'R')
        if 'right' in anotation_position:
            anotation_position = 'left'
        elif 'left' in anotation_position:
            anotation_position = 'right'
        return AnotatedShape(flipped, anotation_text=anotation_text,
                             anotation_position=anotation_position,
                             coloring_value=coloring_value,
                             disabling_value=disabling_value)


class RightLobuleI2III(CerebellarRegion):
    _shape = FS(M((270.312, 20.869)),
                Q((274.155, 14.277), (278.375, 11.375)),
                C((290.669, 2.918), (307.091, 0.685), (319.875, 6.125)),
                Q((323.261, 7.566), (328.125, 13.125)),
                Q((322.173, 26.358), (317.575, 31.694)),
                C((311.572, 38.661), (304.230, 43.927), (296.446, 46.707)),
                Q((287.669, 49.841), (270.312, 47.819)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='R I-III',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleIV(CerebellarRegion):
    _shape = FS(M((270.312, 47.819)),
                Q((287.669, 49.841), (296.446, 46.707)),
                C((304.230, 43.927), (311.572, 38.661), (317.575, 31.694)),
                Q((322.173, 26.358), (328.125, 13.125)),
                Q((331.406, 5.304), (335.654, 4.348)),
                C((338.351, 3.742), (341.246, 3.606), (343.176, 5.759)),
                Q((344.213, 6.915), (344.779, 9.782)),
                Q((343.040, 27.802), (338.036, 37.254)),
                C((334.798, 43.371), (331.535, 47.957), (326.360, 52.267)),
                C((319.403, 58.060), (311.974, 61.902), (303.006, 62.276)),
                Q((289.661, 62.832), (270.312, 62.276)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='R IV',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleV(CerebellarRegion):
    _shape = FS(M((270.312, 62.276)),
                Q((289.661, 62.832), (303.006, 62.276)),
                C((311.974, 61.902), (319.403, 58.060), (326.360, 52.267)),
                C((331.535, 47.957), (334.798, 43.371), (338.036, 37.254)),
                Q((343.040, 27.802), (344.779, 9.782)),
                Q((347.331, 7.258), (349.165, 6.734)),
                Q((354.215, 5.291), (359.126, 10.434)),
                Q((358.167, 25.500), (355.167, 41.500)),
                C((352.819, 54.022), (346.692, 63.906), (337.500, 72.833)),
                C((326.737, 83.287), (315.500, 90.500), (299.500, 90.500)),
                Q((289.500, 90.500), (270.312, 90.500)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='R V',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleVI(CerebellarRegion):
    _shape = FS(M((300.365, 90.509)),
                C((315.500, 90.500), (326.737, 83.287), (337.500, 72.833)),
                C((346.692, 63.906), (352.819, 54.022), (355.167, 41.500)),
                Q((358.167, 25.500), (358.500, 11.167)),
                Q((365.019, 7.163), (368.049, 7.985)),
                C((372.865, 9.292), (376.924, 11.298), (381.576, 17.713)),
                C((384.250, 21.400), (389.063, 27.520), (390.432, 33.974)),
                C((391.306, 38.090), (390.749, 43.433), (390.723, 45.879)),
                Q((390.702, 47.769), (389.561, 51.106)),
                Q((374.821, 80.602), (360.732, 93.544)),
                C((352.967, 100.677), (345.537, 107.448), (333.210, 111.073)),
                C((316.500, 115.988), (303.721, 115.333), (298.479, 115.333)),
                Q((301.619, 107.830), (302.041, 104.400)),
                Q((302.648, 99.473), (300.365, 90.509)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='R VI',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleCrusI(CerebellarRegion):
    _shape = FS(M((299.230, 113.775)),
                C((303.721, 115.333), (316.500, 115.988), (333.210, 111.073)),
                C((345.537, 107.448), (352.967, 100.677), (360.732, 93.544)),
                Q((374.821, 80.602), (389.238, 51.277)),
                Q((393.364, 45.964), (400.683, 47.428)),
                C((415.842, 50.460), (425.291, 64.140), (431.000, 76.875)),
                C((437.547, 91.481), (446.067, 107.860), (444.250, 124.000)),
                Q((443.479, 130.846), (435.250, 131.500)),
                Q((415.374, 133.842), (400.344, 133.842)),
                C((385.671, 133.842), (357.758, 127.758), (331.634, 129.189)),
                C((320.189, 129.816), (302.647, 136.347), (296.742, 136.347)),
                Q((301.154, 132.519), (301.701, 129.606)),
                Q((302.722, 124.156), (299.230, 113.775)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='R Crus I',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)


class RightLobuleCrusII(CerebellarRegion):
    _shape = FS(M((296.960, 136.473)),
                C((302.647, 136.347), (320.189, 129.816), (331.634, 129.189)),
                C((357.758, 127.758), (385.671, 133.842), (400.344, 133.842)),
                Q((415.374, 133.842), (435.250, 131.500)),
                Q((441.827, 134.889), (442.750, 137.000)),
                C((446.250, 145.000), (448.564, 161.972), (447.250, 171.500)),
                Q((445.250, 186.000), (430.250, 186.500)),
                C((411.000, 184.667), (396.530, 171.110), (377.000, 167.333)),
                C((359.903, 164.027), (335.000, 166.000), (327.667, 165.333)),
                Q((302.655, 163.060), (298.095, 160.306)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='R Crus II',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)


class RightLobuleVIIB(CerebellarRegion):
    _shape = FS(M((298.095, 160.306)),
                Q((302.655, 163.060), (327.667, 165.333)),
                C((335.000, 166.000), (359.903, 164.027), (377.000, 167.333)),
                C((396.530, 171.110), (411.000, 184.667), (429.667, 187.333)),
                C((438.162, 187.161), (443.593, 187.177), (446.515, 186.516)),
                C((450.218, 185.679), (451.913, 190.005), (452.336, 195.035)),
                C((452.610, 198.300), (452.348, 201.862), (451.750, 204.500)),
                C((450.830, 208.557), (447.975, 212.993), (443.750, 215.500)),
                Q((439.833, 217.824), (431.250, 217.500)),
                L((425.331, 216.551)),
                Q((404.333, 203.333), (375.000, 192.667)),
                C((358.161, 186.543), (345.424, 184.789), (329.000, 182.667)),
                Q((308.746, 180.050), (298.662, 180.735)),
                Q((301.302, 176.059), (301.701, 173.206)),
                Q((302.370, 168.411), (298.095, 160.306)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='R VIIB',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleVIIIA(CerebellarRegion):
    _shape = FS(M((298.662, 180.735)),
                Q((308.746, 180.050), (329.000, 182.667)),
                C((345.424, 184.789), (358.161, 186.543), (375.000, 192.667)),
                Q((404.333, 203.333), (424.333, 217.333)),
                Q((425.741, 224.893), (422.774, 228.823)),
                Q((420.122, 232.335), (407.945, 237.005)),
                Q((401.927, 234.722), (399.667, 232.667)),
                C((392.333, 226.000), (379.175, 209.450), (373.000, 205.333)),
                C((360.885, 197.257), (348.065, 195.185), (333.667, 193.333)),
                Q((322.717, 191.925), (298.662, 193.786)),
                Q((300.564, 190.080), (300.679, 187.852)),
                Q((300.815, 185.209), (298.662, 180.735)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='R VIIIA',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleVIIIB(CerebellarRegion):
    _shape = FS(M((298.662, 193.786)),
                Q((322.717, 191.925), (333.667, 193.333)),
                C((348.065, 195.185), (360.885, 197.257), (373.000, 205.333)),
                C((379.175, 209.450), (392.333, 226.000), (399.667, 232.667)),
                Q((401.927, 234.722), (407.000, 237.333)),
                Q((408.802, 242.724), (407.945, 245.697)),
                C((406.962, 249.108), (405.231, 251.825), (402.320, 253.879)),
                Q((398.626, 256.486), (390.048, 255.924)),
                Q((382.742, 250.066), (377.409, 236.066)),
                C((373.133, 224.843), (368.354, 219.836), (358.354, 213.836)),
                C((348.984, 208.214), (346.710, 205.367), (327.126, 205.367)),
                C((320.046, 205.367), (313.698, 207.933), (302.634, 207.973)),
                Q((303.638, 203.404), (303.105, 200.959)),
                Q((302.461, 198.006), (298.662, 193.786)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='R VIIIB',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleIX(CerebellarRegion):
    _shape = FS(M((302.634, 207.973)),
                C((313.698, 207.933), (320.046, 205.367), (327.126, 205.367)),
                C((346.710, 205.367), (348.984, 208.214), (358.354, 213.836)),
                C((368.354, 219.836), (373.133, 224.843), (377.409, 236.066)),
                Q((382.742, 250.066), (390.333, 256.667)),
                Q((387.321, 259.803), (385.446, 261.549)),
                C((381.696, 265.042), (375.127, 265.528), (372.663, 268.196)),
                Q((368.086, 273.153), (366.016, 283.025)),
                Q((358.333, 284.000), (347.000, 279.333)),
                C((329.877, 272.283), (328.333, 256.667), (317.667, 248.000)),
                C((310.570, 242.234), (303.394, 238.949), (299.230, 236.913)),
                Q((301.774, 231.783), (302.630, 228.808)),
                Q((304.682, 221.680), (302.634, 207.973)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='R IX',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleX(CerebellarRegion):
    _shape = FS(M((299.230, 236.913)),
                C((303.394, 238.949), (310.570, 242.234), (317.667, 248.000)),
                C((328.333, 256.667), (329.877, 272.283), (347.000, 279.333)),
                Q((358.333, 284.000), (365.367, 283.327)),
                Q((376.338, 279.313), (381.356, 282.002)),
                C((387.424, 285.255), (390.303, 292.054), (388.473, 298.686)),
                C((386.439, 306.059), (377.397, 309.103), (371.640, 309.103)),
                C((357.629, 309.103), (350.949, 305.770), (345.228, 301.578)),
                C((340.928, 298.427), (337.169, 294.790), (331.245, 291.718)),
                C((322.759, 287.318), (314.271, 285.559), (304.655, 286.093)),
                C((290.849, 286.860), (289.315, 293.507), (287.880, 292.523)),
                C((293.406, 287.904), (296.030, 277.828), (297.170, 272.885)),
                C((299.198, 264.095), (299.699, 252.623), (299.230, 236.913)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='R X',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class VermisVI(CerebellarRegion):
    _shape = FS(M((270.312, 90.500)),
                Q((289.500, 90.500), (300.365, 90.509)),
                Q((302.648, 99.473), (302.041, 104.400)),
                Q((301.619, 107.830), (299.230, 113.775)),
                Q((288.569, 115.333), (270.312, 115.333)),
                Q((252.055, 115.333), (241.394, 113.775)),
                Q((239.005, 107.830), (238.583, 104.400)),
                Q((237.976, 99.473), (240.259, 90.509)),
                Q((251.124, 90.500), (270.312, 90.500)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class VermisVII(CerebellarRegion):
    _shape = FS(M((270.312, 115.333)),
                Q((288.569, 115.333), (299.230, 113.775)),
                Q((302.722, 124.156), (301.701, 129.606)),
                Q((301.154, 132.519), (296.960, 136.473)),
                Q((301.701, 146.637), (301.019, 152.768)),
                Q((300.704, 155.610), (298.095, 160.306)),
                Q((302.370, 168.411), (301.701, 173.206)),
                Q((301.302, 176.059), (298.662, 180.735)),
                L((241.962, 181.333)),
                Q((239.322, 176.059), (238.923, 173.206)),
                Q((238.254, 168.411), (242.529, 160.306)),
                Q((239.920, 155.610), (239.605, 152.768)),
                Q((238.923, 146.637), (243.664, 136.473)),
                Q((239.470, 132.519), (238.923, 129.606)),
                Q((237.902, 124.156), (241.394, 113.775)),
                Q((252.055, 115.333), (270.312, 115.333)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class VermisVIII(CerebellarRegion):
    _shape = FS(M((270.312, 181.333)),
                L((298.662, 180.735)),
                Q((300.815, 185.209), (300.679, 187.852)),
                Q((300.564, 190.080), (298.662, 193.786)),
                Q((302.461, 198.006), (303.105, 200.959)),
                Q((303.638, 203.404), (302.634, 207.973)),
                Q((293.726, 209.923), (270.312, 208.667)),
                Q((246.898, 209.923), (237.990, 207.973)),
                Q((236.986, 203.404), (237.519, 200.959)),
                Q((238.163, 198.006), (241.962, 193.786)),
                Q((240.060, 190.080), (239.945, 187.852)),
                Q((239.809, 185.209), (241.962, 180.735)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class VermisIX(CerebellarRegion):
    _shape = FS(M((270.312, 208.667)),
                Q((293.726, 209.923), (302.634, 207.973)),
                Q((304.682, 221.680), (302.630, 228.808)),
                Q((301.774, 231.783), (299.230, 236.913)),
                Q((285.519, 231.250), (270.312, 233.155)),
                Q((255.105, 231.250), (241.394, 236.913)),
                Q((238.850, 231.783), (237.994, 228.808)),
                Q((235.942, 221.680), (237.990, 207.973)),
                Q((246.898, 209.923), (270.312, 208.667)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class VermisX(CerebellarRegion):
    _shape = FS(M((270.312, 233.155)),
                C((280.450, 231.885), (290.089, 233.138), (299.230, 236.913)),
                C((299.699, 252.623), (299.198, 264.095), (297.170, 272.885)),
                C((296.030, 277.828), (293.406, 287.904), (287.880, 292.523)),
                C((283.269, 296.377), (274.064, 296.759), (270.312, 296.575)),
                C((266.560, 296.759), (257.355, 296.377), (252.744, 292.523)),
                C((247.218, 287.904), (244.594, 277.828), (243.454, 272.885)),
                C((241.426, 264.095), (240.925, 252.623), (241.394, 236.913)),
                C((250.535, 233.138), (260.174, 231.885), (270.312, 233.155)))
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        super().__init__(self._shape, anotation_text='V X',
                         anotation_position='bottom',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
