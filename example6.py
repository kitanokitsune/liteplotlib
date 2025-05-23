#!/usr/bin/env python
#-*- coding: utf-8 -*-

###### LitePlotLib Demo 6 ######
##   Misc.                    ##
################################

import math
from liteplotlib import LitePlotLib

## Prepare plot data
x = [ n/512.0 for n in range(512+1) ]
y1 = [ math.sin(2.0*math.pi*t) for t in x ]
y2 = [ math.cos(2.0*math.pi*t) for t in x ]
y3 = [ math.sin(16.0*math.pi*t) for t in x ]
y4 = [ math.cos(16.0*math.pi*t) for t in x ]
y5 = [ math.sin(64.0*math.pi*t) for t in x ]
y6 = [ math.cos(64.0*math.pi*t) for t in x ]


# -- Create instance
myplt = LitePlotLib(size=(1000, 600), sharex=True, sharey=True)
myplt.set_graph_title('Miscellaneous Demo', x=0.84, fontstyle='oblique', fontweight='extra bold', fontsize='xx-large', color='w', backgroundcolor='c')
myplt.set_window_title('Miscellaneous Demo')
myplt.set_save_dir('./')

# -- on axes0
myplt.add_plot(x, y1, '.:m')
myplt.add_plot(x, y2, '-g')
myplt.set_axes_title('1Hz', fontstyle='italic', fontsize='x-large', fontweight='bold', fontfamily='serif', color='b')
myplt.set_axes_ylabel('Y LABEL', fontweight='bold', fontfamily='serif', color='g')
myplt.set_axes_legend(['sin', 'cos'], loc='upper right', fontsize='medium', title='LEGEND')

# -- Create axes1
myplt.add_new_axes()
# -- on axes1
myplt.add_plot(x, y3, '-r')
myplt.add_plot(x, y4, '--b')
myplt.set_axes_title('8Hz', fontstyle='italic', fontsize='x-large', fontweight='bold', fontfamily='serif', color='b')
myplt.set_axes_ylabel('Y LABEL', fontweight='bold', fontfamily='serif', color='c')

# -- Create axes2
myplt.add_new_axes()
# -- on axes1
myplt.add_plot(x, y5)
myplt.add_plot(x, y6)
myplt.set_axes_title('32Hz', fontstyle='italic', fontsize='x-large', fontweight='bold', fontfamily='serif', color='b')
myplt.set_axes_ylabel('Y LABEL', fontweight='bold', fontfamily='serif', color='m')


myplt.show()
myplt.savefig('./example6.png')
myplt.save_plot_data('./example6.dat')
