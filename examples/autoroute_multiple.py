# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 16:08:55 2016

@author: dkita
"""

from pmat_pdk import *
import pmat_pdk.toolkit as tk

top = tk.Cell('Top')

wgt = WaveguideTemplate(
    bend_radius=5.0,
    wg_width=2.0,
    clad_width=2.0,
)

gc1 = GratingCoupler("gc1", wg_template=wgt, center =(-300, -225))
tk.rotate(gc1, 180)
gc2 = GratingCoupler("gc2", wg_template=wgt, center =(300, 225))
top.add(gc1)
top.add(gc2)
gc3 = GratingCoupler("gc3", wg_template=wgt, center =(-300, -225*2))
tk.rotate(gc3, 180)
gc4 = GratingCoupler("gc4", wg_template=wgt, center =(300, 225*2))
top.add(gc3)
top.add(gc4)

netlist = [
    (top.components["gc1"].portlist["input"], top.components["gc2"].portlist["input"]),
    (top.components["gc3"].portlist["input"], top.components["gc4"].portlist["input"]),
]

tk.autoBuildWaveguides(top, netlist, wgt)

layout = core.Layout('LIBRARY')
layout.add(top.gdscell)
layout.save('first_mask.gds')
os.system('first_mask.gds')
# layout.show()
