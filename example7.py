#!/usr/bin/env python
#-*- coding: utf-8 -*-

###### LitePlotLib Demo 7 ######
##   Restore data             ##
################################

from liteplotlib import LitePlotLib

# -- Create instance
myplt = LitePlotLib()
myplt.restore_plot_data('./example6.dat')
myplt.set_window_title('Restore Data Demo')
myplt.show()
