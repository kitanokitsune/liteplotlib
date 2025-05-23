#!/usr/bin/env python
#-*- coding: utf-8 -*-

###### LitePlotLib Demo 1 ######
##   Instant plot             ##
################################
import math
from liteplotlib import LitePlotLib

## Prepare plot data
xdata = [ n/32.0 for n in range(32) ]
ydata = [ math.sin(2.0*math.pi*t) for t in xdata ]

# Plot
myplt = LitePlotLib(xdata, ydata, '-g')
myplt.show()
