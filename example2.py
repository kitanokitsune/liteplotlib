#!/usr/bin/env python
#-*- coding: utf-8 -*-

#################### LitePlotLib Demo 2 ####################
##   Multiple traces, legend, xlabel, ylabel, Titles      ##
############################################################

import math
from liteplotlib import LitePlotLib

## Prepare plot data
x = [ n/32.0 for n in range(32) ]
ysin = [ math.sin(2.0*math.pi*t) for t in x ]
ycos = [ math.cos(2.0*math.pi*t) for t in x ]

# -- Create instance with Graph Title
myplt = LitePlotLib(title='Multiple traces, Legend, X-Y Labels, Titles Demo')

# -- Add multiple traces
myplt.add_plot(x, ysin)
myplt.add_plot(x, ycos)

# -- Legend
myplt.set_axes_legend(['sine', 'cosine']) # label order is the same as add_plot()

# -- xlabel and ylabel
myplt.set_axes_xlabel('X LABEL')
myplt.set_axes_ylabel('Y LABEL')

# -- Axes title
myplt.set_axes_title('- Axes Title -')

# -- Window title
myplt.set_window_title('LitePlotLib Demo 2')

myplt.show()

