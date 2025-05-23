#!/usr/bin/env python
#-*- coding: utf-8 -*-

###### LitePlotLib Demo 3 ######
##   Multiple axes            ##
################################

import math
from liteplotlib import LitePlotLib

## Prepare plot data
x = [ n/32.0 for n in range(32) ]
ysin = [ math.sin(2.0*math.pi*t) for t in x ] # Data for axes0
ycos = [ math.cos(2.0*math.pi*t) for t in x ] # Data for axes1

# -- Create instance
myplt = LitePlotLib(title='Multiple Axes Demo')

# -- Plot on axes0
myplt.add_plot(x, ysin)
myplt.set_axes_xlabel('x')
myplt.set_axes_ylabel('sin(x)')
myplt.set_axes_title('* SINE *')

# -- Create axes1
myplt.add_new_axes()

# -- Plot on axes1
myplt.add_plot(x, ycos)
myplt.set_axes_xlabel('x')
myplt.set_axes_ylabel('cos(x)')
myplt.set_axes_title('* COSINE *')

myplt.show()

