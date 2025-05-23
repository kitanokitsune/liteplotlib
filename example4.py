#!/usr/bin/env python
#-*- coding: utf-8 -*-

###### LitePlotLib Demo 4 ######
##   X limit, Y limit         ##
################################

import math
from liteplotlib import LitePlotLib

## Prepare plot data
x = [ n/32.0 for n in range(32) ]
y = [ math.sin(4.0*math.pi*t) for t in x ]

# -- Create instance
myplt = LitePlotLib(title='X limit, Y limit Demo')

# -- Plot on axes0
myplt.add_plot(x, y)

# -- Create axes1
myplt.add_new_axes()

# -- Plot on axes1
myplt.add_plot(x, y)
myplt.set_axes_xlabel('X limit = [0.1, 0.9]')
# -- Set X limit on axes1
myplt.set_axes_xlim(0.1, 0.9)

# -- Create axes2
myplt.add_new_axes()

# -- Plot on axes2
myplt.add_plot(x, y)
myplt.set_axes_ylabel('Y limit = [-0.8, 0.8]')
# -- Set Y limit on axes2
myplt.set_axes_ylim(-0.8, 0.8)

myplt.show()

