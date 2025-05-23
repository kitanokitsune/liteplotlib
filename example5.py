#!/usr/bin/env python
#-*- coding: utf-8 -*-

###### LitePlotLib Demo 5 ######
##   X scale, Y scale         ##
################################

from liteplotlib import LitePlotLib
import matplotlib

## Prepare plot data
x = [ n for n in range(1,32) ]
y = [ t**2.2 for t in x ]

# -- Create instance
myplt = LitePlotLib(title='X scale, Y scale Demo')

# -- Plot on axes0
myplt.add_plot(x, y)
myplt.set_axes_xlabel('X: Linear Scale')
myplt.set_axes_ylabel('Y: Log10 Scale')
# -- Set scale on axes0
myplt.set_axes_xscale('linear')
myplt.set_axes_yscale('log')

# -- Create axes1
myplt.add_new_axes()

# -- Plot on axes1
myplt.add_plot(x, y)
myplt.set_axes_xlabel('X: Log2 Scale')
myplt.set_axes_ylabel('Y: Log2 Scale')
# -- Set scale on axes1
matplotlib_version = [ n for n in map(int, matplotlib.__version__.split('.')) ]
if matplotlib_version >= [3,3]:
    myplt.set_axes_xscale('log', base=2)
    myplt.set_axes_yscale('log', base=2)
else:
    myplt.set_axes_xscale('log', basex=2)
    myplt.set_axes_yscale('log', basey=2)

myplt.show()

