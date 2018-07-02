#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')
from xml.etree import ElementTree

from cerebellum_value_map.lobules import *

from svgwrite import Drawing
from svgwrite.container import Group


drawing = Drawing('test.svg', size=('600', '400'), stroke_width=2,
                  font_size=12, stroke='black')

# trans_x = 230
right_i2iii = RightLobuleI2III(0.3)
right_iv = RightLobuleIV(0.4)
right_v = RightLobuleV(0.5)
right_vi = RightLobuleVI(0.6)
right_crusi = RightLobuleCrusI(0.72)
right_crusii = RightLobuleCrusII(0.74)
right_viib = RightLobuleVIIB(0.76)
right_viiia = RightLobuleVIIIA(0.83)
right_viiib = RightLobuleVIIIB(0.86)
right_ix = RightLobuleIX(0.9)
right_x = RightLobuleX(1)

left_i2iii = LeftLobuleI2III(0.3)
left_iv = LeftLobuleIV(0.4)
left_v = LeftLobuleV(0.5)
left_vi = LeftLobuleVI(0.6)
left_crusi = LeftLobuleCrusI(0.72)
left_crusii = LeftLobuleCrusII(0.74)
left_viib = LeftLobuleVIIB(0.76)
left_viiia = LeftLobuleVIIIA(0.83)
left_viiib = LeftLobuleVIIIB(0.86)
left_ix = LeftLobuleIX(0.9)
left_x = LeftLobuleX(1)

# right_i2iii   =  right_i2iii.translate(trans_x, 0)   
# right_iv      =  right_iv.translate(trans_x, 0)      
# right_v       =  right_v.translate(trans_x, 0)       
# right_vi      =  right_vi.translate(trans_x, 0)      
# right_crusi   =  right_crusi.translate(trans_x, 0)   
# right_crusii  =  right_crusii.translate(trans_x, 0)     
# right_viib    =  right_viib.translate(trans_x, 0)       
# right_viiia   =  right_viiia.translate(trans_x, 0)      
# right_viiib   =  right_viiib.translate(trans_x, 0)      
# right_ix      =  right_ix.translate(trans_x, 0)         
# right_x       =  right_x.translate(trans_x, 0)          
# 
# left_i2iii   =  left_i2iii.translate(trans_x, 0)   
# left_iv      =  left_iv.translate(trans_x, 0)      
# left_v       =  left_v.translate(trans_x, 0)       
# left_vi      =  left_vi.translate(trans_x, 0)      
# left_crusi   =  left_crusi.translate(trans_x, 0)   
# left_crusii  =  left_crusii.translate(trans_x, 0)     
# left_viib    =  left_viib.translate(trans_x, 0)       
# left_viiia   =  left_viiia.translate(trans_x, 0)      
# left_viiib   =  left_viiib.translate(trans_x, 0)      
# left_ix      =  left_ix.translate(trans_x, 0)         
# left_x       =  left_x.translate(trans_x, 0)          
# 
# vermis_vi = VermisVI().translate(trans_x, 0)
# vermis_vii = VermisVII().translate(trans_x, 0)
# vermis_viii = VermisVIII().translate(trans_x, 0)
# vermis_ix = VermisIX().translate(trans_x, 0)
# vermis_x = VermisX().translate(trans_x, 0)

vermis_vi = VermisVI()
vermis_vii = VermisVII()
vermis_viii = VermisVIII()
vermis_ix = VermisIX()
vermis_x = VermisX()

print('left_i2iii\n' ,  left_i2iii.shape)
print('left_iv   \n' ,  left_iv.shape)
print('left_v    \n' ,  left_v.shape)
print('left_vi   \n' ,  left_vi.shape)
print('left_crusi\n' ,  left_crusi.shape)
print('left_crusii\n',  left_crusii.shape)
print('left_viib \n' ,  left_viib.shape)
print('left_viiia\n' ,  left_viiia.shape)
print('left_viiib\n' ,  left_viiib.shape)
print('left_ix   \n' ,  left_ix.shape)
print('left_x    \n' ,  left_x.shape)

print('right_i2iii\n' ,right_i2iii.shape)
print('right_iv   \n' ,right_iv.shape)
print('right_v    \n' ,right_v.shape)
print('right_vi   \n' ,right_vi.shape)
print('right_crusi\n' ,right_crusi.shape)
print('right_crusii\n',right_crusii.shape)
print('right_viib \n' ,right_viib.shape)
print('right_viiia\n' ,right_viiia.shape)
print('right_viiib\n' ,right_viiib.shape)
print('right_ix   \n' ,right_ix.shape)
print('right_x    \n' ,right_x.shape)

print('vermis_vi\n', vermis_vi.shape)
print('vermis_vii\n', vermis_vii.shape)
print('vermis_viii\n', vermis_viii.shape)
print('vermis_ix\n', vermis_ix.shape)
print('vermis_x\n', vermis_x.shape)

drawing.add(right_i2iii.get_svg())
drawing.add(right_iv.get_svg())
drawing.add(right_v.get_svg())
drawing.add(right_vi.get_svg())
drawing.add(right_crusi.get_svg())
drawing.add(right_crusii.get_svg())
drawing.add(right_viib.get_svg())
drawing.add(right_viiia.get_svg())
drawing.add(right_viiib.get_svg())
drawing.add(right_ix.get_svg())
drawing.add(right_x.get_svg())

drawing.add(left_i2iii.get_svg())
drawing.add(left_iv.get_svg())
drawing.add(left_v.get_svg())
drawing.add(left_vi.get_svg())
drawing.add(left_crusi.get_svg())
drawing.add(left_crusii.get_svg())
drawing.add(left_viib.get_svg())
drawing.add(left_viiia.get_svg())
drawing.add(left_viiib.get_svg())
drawing.add(left_ix.get_svg())
drawing.add(left_x.get_svg())

drawing.add(vermis_vi.get_svg())
drawing.add(vermis_vii.get_svg())
drawing.add(vermis_viii.get_svg())
drawing.add(vermis_ix.get_svg())
drawing.add(vermis_x.get_svg())

drawing.save(pretty=True)
