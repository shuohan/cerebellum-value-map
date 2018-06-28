# -*- coding: utf-8 -*-

from .free_shape import FreeShape as FS
from .free_shape import Move as M
from .free_shape import Line as L
from .free_shape import BezierCurve as C
from .free_shape import QuadraticCurve as Q
from .shape import AnotatedShape


class RightLobuleI2III(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((40.312, 20.869)),
                Q((44.155, 14.277), (48.375, 11.375)),
                C((60.669, 2.918), (77.091, 0.685), (89.875, 6.125)),
                Q((93.261, 7.566), (98.125, 13.125)),
                Q((92.173, 26.358), (87.575, 31.694)),
                C((81.572, 38.661), (74.23, 43.927), (66.446, 46.707)),
                Q((57.669, 49.841), (40.312, 47.819)))
        super().__init__(fs, anotation_text='R I-III',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleIV(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((40.312, 47.819)),
                Q((57.669, 49.841), (66.446, 46.707)),
                C((74.23, 43.927), (81.572, 38.661), (87.575, 31.694)),
                Q((92.173, 26.358), (98.125, 13.125)),
                Q((101.406, 5.304), (105.654, 4.348)),
                C((108.351, 3.742), (111.246, 3.606), (113.176, 5.759)),
                Q((114.213, 6.915), (114.779, 9.782)),
                Q((113.04, 27.802), (108.036, 37.254)),
                C((104.798, 43.371), (101.535, 47.957), (96.36, 52.267)),
                C((89.403, 58.06), (81.974, 61.902), (73.006, 62.276)),
                Q((59.661, 62.832), (40.312, 62.276)))
        super().__init__(fs, anotation_text='R IV',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleV(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((40.312, 62.276)),
                Q((59.661, 62.832), (73.006, 62.276)),
                C((81.974, 61.902), (89.403, 58.06), (96.36, 52.267)),
                C((101.535, 47.957), (104.798, 43.371), (108.036, 37.254)),
                Q((113.04, 27.802), (114.779, 9.782)),
                Q((117.331, 7.258), (119.165, 6.734)),
                Q((124.215, 5.291), (129.126, 10.434)),
                Q((128.167, 25.5), (125.167, 41.5)),
                C((122.819, 54.022), (116.692, 63.906), (107.5, 72.833)),
                C((96.737, 83.287), (85.5, 90.5), (69.5, 90.5)),
                Q((59.5, 90.5), (40.312, 90.5)))
        super().__init__(fs, anotation_text='R V',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleVI(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((70.365, 90.509)),
                C((85.5, 90.5), (96.737, 83.287), (107.5, 72.833)),
                C((116.692, 63.906), (122.819, 54.022), (125.167, 41.5)),
                Q((128.167, 25.5), (128.5, 11.167)),
                Q((135.019, 7.163), (138.049, 7.985)),
                C((142.865, 9.292), (146.924, 11.298), (151.576, 17.713)),
                C((154.25, 21.4), (159.063, 27.52), (160.432, 33.974)),
                C((161.306, 38.09), (160.749, 43.433), (160.723, 45.879)),
                Q((160.702, 47.769), (159.561, 51.106)),
                Q((144.821, 80.602), (130.732, 93.544)),
                C((122.967, 100.677), (115.537, 107.448), (103.21, 111.073)),
                C((86.5, 115.988), (73.721, 115.333), (68.479, 115.333)),
                Q((71.619, 107.83), (72.041, 104.4)),
                Q((72.648, 99.473), (70.365, 90.509)))
        super().__init__(fs, anotation_text='R VI',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleCrusI(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((69.23, 113.775)),
                C((73.721, 115.333), (86.5, 115.988), (103.21, 111.073)),
                C((115.537, 107.448), (122.967, 100.677), (130.732, 93.544)),
                Q((144.821, 80.602), (159.238, 51.277)),
                Q((163.364, 45.964), (170.683, 47.428)),
                C((185.842, 50.46), (195.291, 64.14), (201, 76.875)),
                C((207.547, 91.481), (216.067, 107.86), (214.25, 124)),
                Q((213.479, 130.846), (205.25, 131.5)),
                Q((185.374, 133.842), (170.344, 133.842)),
                C((155.671, 133.842), (127.758, 127.758), (101.634, 129.189)),
                C((90.189, 129.816), (72.647, 136.347), (66.742, 136.347)),
                Q((71.154, 132.519), (71.701, 129.606)),
                Q((72.722, 124.156), (69.23, 113.775)))
        super().__init__(fs, anotation_text='R Crus I',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)


class RightLobuleCrusII(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((66.96, 136.473)),
                C((72.647, 136.347), (90.189, 129.816), (101.634, 129.189)),
                C((127.758, 127.758), (155.671, 133.842), (170.344, 133.842)),
                Q((185.374, 133.842), (205.25, 131.5)),
                Q((211.827, 134.889), (212.75, 137)),
                C((216.25, 145), (218.564, 161.972), (217.25, 171.5)),
                Q((215.25, 186), (200.25, 186.5)),
                C((181, 184.667), (166.53, 171.11), (147, 167.333)),
                C((129.903, 164.027), (105, 166), (97.667, 165.333)),
                Q((72.655, 163.06), (68.095, 160.306)))
        super().__init__(fs, anotation_text='R Crus II',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)


class RightLobuleVIIB(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((68.095, 160.306)),
                Q((72.655, 163.06), (97.667, 165.333)),
                C((105, 166), (129.903, 164.027), (147, 167.333)),
                C((166.53, 171.11), (181, 184.667), (199.667, 187.333)),
                C((208.162, 187.161), (213.593, 187.177), (216.515, 186.516)),
                C((220.218, 185.679), (221.913, 190.005), (222.336, 195.035)),
                C((222.61, 198.3), (222.348, 201.862), (221.75, 204.5)),
                C((220.83, 208.557), (217.975, 212.993), (213.75, 215.5)),
                Q((209.833, 217.824), (201.25, 217.5)),
                L((195.331, 216.551)),
                Q((174.333, 203.333), (145, 192.667)),
                C((128.161, 186.543), (115.424, 184.789), (99, 182.667)),
                Q((78.746, 180.05), (68.662, 180.735)),
                Q((71.302, 176.059), (71.701, 173.206)),
                Q((72.37, 168.411), (68.095, 160.306)))
        super().__init__(fs, anotation_text='R VIIB',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleVIIIA(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((68.662, 180.735)),
                Q((78.746, 180.05), (99, 182.667)),
                C((115.424, 184.789), (128.161, 186.543), (145, 192.667)),
                Q((174.333, 203.333), (194.333, 217.333)),
                Q((195.741, 224.893), (192.774, 228.823)),
                Q((190.122, 232.335), (177.945, 237.005)),
                Q((171.927, 234.722), (169.667, 232.667)),
                C((162.333, 226), (149.175, 209.45), (143, 205.333)),
                C((130.885, 197.257), (118.065, 195.185), (103.667, 193.333)),
                Q((92.717, 191.925), (68.662, 193.786)),
                Q((70.564, 190.08), (70.679, 187.852)),
                Q((70.815, 185.209), (68.662, 180.735)))
        super().__init__(fs, anotation_text='R VIIIA',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleVIIIB(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((68.662, 193.786)),
                Q((92.717, 191.925), (103.667, 193.333)),
                C((118.065, 195.185), (130.885, 197.257), (143, 205.333)),
                C((149.175, 209.45), (162.333, 226), (169.667, 232.667)),
                Q((171.927, 234.722), (177, 237.333)),
                Q((178.802, 242.724), (177.945, 245.697)),
                C((176.962, 249.108), (175.231, 251.825), (172.32, 253.879)),
                Q((168.626, 256.486), (160.048, 255.924)),
                Q((152.742, 250.066), (147.409, 236.066)),
                C((143.133, 224.843), (138.354, 219.836), (128.354, 213.836)),
                C((118.984, 208.214), (116.71, 205.367), (97.126, 205.367)),
                C((90.046, 205.367), (83.698, 207.933), (72.634, 207.973)),
                Q((73.638, 203.404), (73.105, 200.959)),
                Q((72.461, 198.006), (68.662, 193.786)))
        super().__init__(fs, anotation_text='R VIIIB',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleIX(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((72.634, 207.973)),
                C((83.698, 207.933), (90.046, 205.367), (97.126, 205.367)),
                C((116.71, 205.367), (118.984, 208.214), (128.354, 213.836)),
                C((138.354, 219.836), (143.133, 224.843), (147.409, 236.066)),
                Q((152.742, 250.066), (160.333, 256.667)),
                Q((157.321, 259.803), (155.446, 261.549)),
                C((151.696, 265.042), (145.127, 265.528), (142.663, 268.196)),
                Q((138.086, 273.153), (136.016, 283.025)),
                Q((128.333, 284), (117, 279.333)),
                C((99.877, 272.283), (98.333, 256.667), (87.667, 248)),
                C((80.57, 242.234), (73.394, 238.949), (69.23, 236.913)),
                Q((71.774, 231.783), (72.63, 228.808)),
                Q((74.682, 221.68), (72.634, 207.973)))
        super().__init__(fs, anotation_text='R IX',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class RightLobuleX(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((69.23, 236.913)),
                C((73.394, 238.949), (80.57, 242.234), (87.667, 248)),
                C((98.333, 256.667), (99.877, 272.283), (117, 279.333)),
                Q((128.333, 284), (135.367, 283.327)),
                Q((146.338, 279.313), (151.356, 282.002)),
                C((157.424, 285.255), (160.303, 292.054), (158.473, 298.686)),
                C((156.439, 306.059), (147.397, 309.103), (141.64, 309.103)),
                C((127.629, 309.103), (120.949, 305.77), (115.228, 301.578)),
                C((110.928, 298.427), (107.169, 294.79), (101.245, 291.718)),
                C((92.759, 287.318), (84.271, 285.559), (74.655, 286.093)),
                C((60.849, 286.86), (59.315, 293.507), (57.88, 292.523)),
                C((63.406, 287.904), (66.03, 277.828), (67.17, 272.885)),
                C((69.198, 264.095), (69.699, 252.623), (69.23, 236.913)))
        super().__init__(fs, anotation_text='R X',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class VermisVI(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((40.312, 90.5)),
                Q((59.5, 90.5), (70.365, 90.509)),
                Q((72.648, 99.473), (72.041, 104.4)),
                Q((71.619, 107.83), (69.23, 113.775)),
                Q((58.569, 115.333), (40.312, 115.333)))
        super().__init__(fs, anotation_text='',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class VermisVII(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((40.312, 115.333)),
                Q((58.569, 115.333), (69.23, 113.775)),
                Q((72.722, 124.156), (71.701, 129.606)),
                Q((71.154, 132.519), (66.96, 136.473)),
                Q((71.701, 146.637), (71.019, 152.768)),
                Q((70.704, 155.61), (68.095, 160.306)),
                Q((72.37, 168.411), (71.701, 173.206)),
                Q((71.302, 176.059), (68.662, 180.735)),
                L((40.312, 181.333)))
        super().__init__(fs, anotation_text='',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class VermisVIII(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((40.312, 181.333)),
                L((68.662, 180.735)),
                Q((70.815, 185.209), (70.679, 187.852)),
                Q((70.564, 190.08), (68.662, 193.786)),
                Q((72.461, 198.006), (73.105, 200.959)),
                Q((73.638, 203.404), (72.634, 207.973)),
                Q((63.726, 209.923), (40.312, 208.667)))
        super().__init__(fs, anotation_text='',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class VermisIX(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((40.312, 208.667)),
                Q((63.726, 209.923), (72.634, 207.973)),
                Q((74.682, 221.68), (72.63, 228.808)),
                Q((71.774, 231.783), (69.23, 236.913)),
                Q((55.519, 231.25), (40.312, 233.155)))
        super().__init__(fs, anotation_text='',
                         anotation_position='right',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
    

class VermisX(AnotatedShape):
    def __init__(self, coloring_value=0, disabling_value=-float('inf')):
        fs = FS(M((40.312, 233.155)),
                C((50.45, 231.885), (60.089, 233.138), (69.23, 236.913)),
                C((69.699, 252.623), (69.198, 264.095), (67.17, 272.885)),
                C((66.03, 277.828), (63.406, 287.904), (57.88, 292.523)),
                C((53.269, 296.377), (44.064, 296.759), (40.312, 296.575)))
        super().__init__(fs, anotation_text='V X',
                         anotation_position='bottom',
                         coloring_value=coloring_value,
                         disabling_value=disabling_value)
