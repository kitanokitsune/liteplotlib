#!/usr/bin/env python

__version__ = "1.0.0"
"""Lite Plot Library for Python ver1.0

"""
##################################################################################
# This library is released under the MIT license.                                #
# -------------------------------------------------------                        #
# Copyright (c) 2025 Kitanokitsune                                               #
#                                                                                #
# Permission is hereby granted, free of charge, to any person obtaining a copy   #
# of this software and associated documentation files (the "Software"), to deal  #
# in the Software without restriction, including without limitation the rights   #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      #
# copies of the Software, and to permit persons to whom the Software is          #
# furnished to do so, subject to the following conditions:                       #
#                                                                                #
# The above copyright notice and this permission notice shall be included in all #
# copies or substantial portions of the Software.                                #
#                                                                                #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  #
# SOFTWARE.                                                                      #
##################################################################################


#  panels = [ panel, panel, ... ]
#  panel  = [ plots, panelattr ]
#  panelattr = {'xlabel':?, 'ylabel':?, 'xmin':?, 'xmax':?, 'ymin':?, 'ymax':?, ...}
#  plots  = [ plot, plot, ... ]
#  plot   = [ xlist, ylist, format ]
#  format = '<marker><line><color>'   ex). 'b' 'or', '-g', '--', '^k:'
#    See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

import os.path as _my_path_
import pickle as _my_pickle_
import zlib as _my_zlib_
import matplotlib.pyplot as _my_pyplot_


# ===================================================================
#  Class: LitePlotLib
# ===================================================================
class LitePlotLib:
    # -------------------------------------
    def __init__(self, x=None, y=None, fmt=None, title='', size=None, sharex=False, sharey=False):
        self.__graphtitle = title
        self.__graphtitleattr = {}
        self.__windowtitle = ''
        self.__size = size
        self.__facecolor = None
        self.__edgecolor = None
        self.__edgewidth = 0.0
        self.__savepath = None
        self.__graphstyle = None
        self.__sharex = sharex
        self.__sharey = sharey
        self.__panels = []
        if x is not None:
            if y is None:
                y = x
                x = [ n for n in range(len(y)) ]
            plot = [x, y]
            if fmt:
                plot.append(fmt)
            self.chk_plot_data(plot)
            plots = [ plot ]
            panel = [ plots, {} ]
            self.__panels.append( panel )

    # -------------------------------------
    def save_plot_data(self, filename):
        if self.__savepath:
            filename = _my_path_.join(self.__savepath, filename)
        filename = _my_path_.normpath(filename)
        dict_dat = {
            'description':'LitePlotLib Plot Data',
            'graphtitle':self.__graphtitle,
            'graphtitleattr':self.__graphtitleattr,
            'windowtitle':self.__windowtitle,
            'size':self.__size,
            'facecolor':self.__facecolor,
            'edgecolor':self.__edgecolor,
            'edgewidth':self.__edgewidth,
            'graphstyle':self.__graphstyle,
            'sharex':self.__sharex,
            'sharey':self.__sharey,
            'panels':self.__panels
        }
        with open(filename, 'wb') as f:
            f.write(_my_zlib_.compress(_my_pickle_.dumps(dict_dat, protocol=3)))
        del dict_dat

    # -------------------------------------
    def restore_plot_data(self, filename):
        if self.__savepath:
            filename = _my_path_.join(self.__savepath, filename)
        filename = _my_path_.normpath(filename)
        with open(filename, 'rb') as f:
            dict_dat = _my_pickle_.loads(_my_zlib_.decompress(f.read()))
        self.__graphtitle = dict_dat['graphtitle']
        self.__graphtitleattr = dict_dat['graphtitleattr']
        self.__windowtitle = dict_dat['windowtitle']
        self.__size = dict_dat['size']
        self.__facecolor = dict_dat['facecolor']
        self.__edgecolor = dict_dat['edgecolor']
        self.__edgewidth = dict_dat['edgewidth']
        self.__graphstyle = dict_dat['graphstyle']
        self.__sharex = dict_dat['sharex']
        self.__sharey = dict_dat['sharey']
        self.__panels = dict_dat['panels']
        del dict_dat

    # -------------------------------------
    def chk_plot_data(self, d):
        #---------------
        # is iterable ?
        #---------------
        l = len(d)
        #---------------
        # has x and y ?
        #---------------
        if l < 1:
            raise TypeError('Incorrect Plot Data: Data are missing!')
        elif l < 2:
            raise TypeError('Incorrect Plot Data: Y data is required!')
        x = d[0]
        y = d[1]
        #---------------
        # list length is the same ?
        #---------------
        lx = len(x)
        ly = len(y)
        if lx*ly < 1 or lx != ly:
            raise TypeError('Incorrect Plot Data: X data and Y data must have the same length!')
        #---------------
        # data is number list ?
        #---------------
        sx = sum(x)
        sy = sum(y)

    # -------------------------------------
    def add_new_axes(self, plots=None, xlabel='', ylabel=''):
        panelattr = {}
        if xlabel:
            panelattr['xlabel'] = xlabel
        if ylabel:
            panelattr['ylabel'] = ylabel
        newpanel = [ plots, panelattr ]
        if self.__panels:
            panel = self.__panels[-1]
            if panel[0]:
                self.__panels.append(newpanel)
            else:
                self.__panels[-1] = newpanel
        else:
            self.__panels.append(newpanel)

    def add_new_panel(self, plots=None, xlabel='', ylabel=''):
        self.add_new_axes(plots, xlabel, ylabel)

    # -------------------------------------
    def add_plot(self, x, y=None, fmt=None):
        if y is None:
            y = x
            x = [ n for n in range(len(y)) ]
        plot = [x, y]
        if fmt:
            plot.append(fmt)
        self.chk_plot_data(plot)
        self.add_plots(plot)

    # -------------------------------------
    def add_plots(self, newplot, *newplots):
        self.chk_plot_data(newplot)
        if self.__panels:
            panel = self.__panels[-1]
            if panel:
                plots = panel[0]
                if plots:
                    if not plots[-1]:
                        plots[-1] = newplot
                    else:
                        plots.append(newplot)
                else:
                    plots = [ newplot ]
                    panel[0] = plots
            else:
                plots = [ newplot ]
                panel = [ plots, {} ]
                self.__panels[-1] = panel
        else:
            plots = [ newplot ]
            self.add_new_axes(plots)

        panel = self.__panels[-1]
        plots = panel[0]
        for pl in newplots:
            self.chk_plot_data(pl)
            plots.append(pl)

    # -------------------------------------
    def set_axes_xlabel(self, label, **kwargs):
        if not self.__panels:
            self.add_new_axes(None, '', '')
        panel = self.__panels[-1]
        if panel:
            panelattr = panel[1]
            panelattr['xlabel'] = label
            panelattr['xlabelattr'] = kwargs
        else:
            panel = [ None, {'xlabel':label, 'xlabelattr':kwargs} ]
            self.__panels[-1] = panel

    # -------------------------------------
    def set_axes_ylabel(self, label, **kwargs):
        if not self.__panels:
            self.add_new_axes(None, '', '')
        panel = self.__panels[-1]
        if panel:
            panelattr = panel[1]
            panelattr['ylabel'] = label
            panelattr['ylabelattr'] = kwargs
        else:
            panel = [ None, {'ylabel':label, 'ylabelattr':kwargs} ]
            self.__panels[-1] = panel

    # -------------------------------------
    def set_axes_xylabel(self, xlabel, ylabel):
        if self.__panels:
            panel = self.__panels[-1]
            if panel:
                panelattr = panel[1]
                panelattr['xlabel'] = xlabel
                panelattr['ylabel'] = ylabel
            else:
                panel = [ None, {'xlabel':xlabel, 'ylabel':ylabel} ]
                self.__panels[-1] = panel
        else:
            self.add_new_axes(None, xlabel, ylabel)

    # -------------------------------------
    def set_axes_xlim(self, xmin=None, xmax=None, auto=False):
        if not self.__panels:
            self.add_new_axes(None, '', '')
        panel = self.__panels[-1]
        if panel:
            panelattr = panel[1]
            if xmin is None:
                if 'xmin' in panelattr:
                    del panelattr['xmin']
            else:
                panelattr['xmin'] = xmin * 1.0
            if xmax is None:
                if 'xmax' in panelattr:
                    del panelattr['xmax']
            else:
                panelattr['xmax'] = xmax * 1.0
            if not auto:
                if 'xauto' in panelattr:
                    del panelattr['xauto']
            else:
                panelattr['xauto'] = True
        else:
            panelattr = {}
            if xmin is not None:
                panelattr['xmin'] = xmin * 1.0
            if xmax is not None:
                panelattr['xmax'] = xmax * 1.0
            if auto:
                panelattr['xauto'] = True
            panel = [ None, panelattr ]
            self.__panels[-1] = panel

    # -------------------------------------
    def set_axes_ylim(self, ymin=None, ymax=None, auto=False):
        if not self.__panels:
            self.add_new_axes(None, '', '')
        panel = self.__panels[-1]
        if panel:
            panelattr = panel[1]
            if ymin is None:
                if 'ymin' in panelattr:
                    del panelattr['ymin']
            else:
                panelattr['ymin'] = ymin * 1.0
            if ymax is None:
                if 'ymax' in panelattr:
                    del panelattr['ymax']
            else:
                panelattr['ymax'] = ymax * 1.0
            if not auto:
                if 'yauto' in panelattr:
                    del panelattr['yauto']
            else:
                panelattr['yauto'] = True
        else:
            panelattr = {}
            if ymin is not None:
                panelattr['ymin'] = ymin * 1.0
            if ymax is not None:
                panelattr['ymax'] = ymax * 1.0
            if auto:
                panelattr['yauto'] = True
            panel = [ None, panelattr ]
            self.__panels[-1] = panel

    # -------------------------------------
    def set_axes_xscale(self, xscale=None, **kwargs):
        if not self.__panels:
            self.add_new_axes(None, '', '')
        panel = self.__panels[-1]
        if panel:
            panelattr = panel[1]
            if xscale is None:
                if 'xscale' in panelattr:
                    del panelattr['xscale']
                    del panelattr['xscaleattr']
            else:
                panelattr['xscale'] = xscale
                panelattr['xscaleattr'] = kwargs
        else:
            panelattr = {}
            if xscale is not None:
                panelattr['xscale'] = xscale
                panelattr['xscaleattr'] = kwargs
            panel = [ None, panelattr ]
            self.__panels[-1] = panel

    # -------------------------------------
    def set_axes_yscale(self, yscale=None, **kwargs):
        if not self.__panels:
            self.add_new_axes(None, '', '')
        panel = self.__panels[-1]
        if panel:
            panelattr = panel[1]
            if yscale is None:
                if 'yscale' in panelattr:
                    del panelattr['yscale']
                    del panelattr['yscaleattr']
            else:
                panelattr['yscale'] = yscale
                panelattr['yscaleattr'] = kwargs
        else:
            panelattr = {}
            if yscale is not None:
                panelattr['yscale'] = yscale
                panelattr['yscaleattr'] = kwargs
            panel = [ None, panelattr ]
            self.__panels[-1] = panel

    # -------------------------------------
    def set_axes_legend(self, labels, **kwargs):
        if not self.__panels:
            self.add_new_axes(None, '', '')
        panel = self.__panels[-1]
        if panel:
            panelattr = panel[1]
            if labels:
                panelattr['legend'] = labels
                panelattr['legendattr'] = kwargs
            else:
                if 'legend' in panelattr:
                    del panelattr['legend']
                    del panelattr['legendattr']
        else:
            panelattr = {}
            if labels:
                panelattr['legend'] = labels
                panelattr['legendattr'] = kwargs
            panel = [ None, panelattr ]
            self.__panels[-1] = panel

    # -------------------------------------
    def set_axes_title(self, title, **kwargs):
        if not self.__panels:
            self.add_new_axes(None, '', '')
        panel = self.__panels[-1]
        if panel:
            panelattr = panel[1]
            if title:
                panelattr['title'] = title
                panelattr['titleattr'] = kwargs
            else:
                if 'title' in panelattr:
                    del panelattr['title']
                    del panelattr['titleattr']
        else:
            panelattr = {}
            if title:
                panelattr['title'] = title
                panelattr['titleattr'] = kwargs
            panel = [ None, panelattr ]
            self.__panels[-1] = panel

    # -------------------------------------
    def set_graph_title(self, title, **kwargs):
        self.__graphtitle = str(title)
        self.__graphtitleattr = kwargs

    # -------------------------------------
    def set_window_title(self, title):
        self.__windowtitle = str(title)

    # -------------------------------------
    def set_window_size(self, x, y):
        self.__size = (x, y)

    # -------------------------------------
    def set_save_dir(self, path=None):
        self.__savepath = path

    # -------------------------------------
    def get_graph_style_available(self):
        return _my_pyplot_.style.available

    # -------------------------------------
    def set_graph_style(self, style=None):
        if style in self.get_graph_style_available():
            self.__graphstyle = style
        else:
            self.__graphstyle = None

    # -------------------------------------
    def set_face_color(self, color=None):
        self.__facecolor = color

    # -------------------------------------
    def set_edge_color(self, color=None):
        self.__edgecolor = color

    # -------------------------------------
    def set_edge_width(self, width=0.0):
        self.__edgewidth = width

    # -------------------------------------
    def set_sharex(self, tf):
        self.__sharex = tf

    # -------------------------------------
    def set_sharey(self, tf):
        self.__sharey = tf

    # -------------------------------------
    def show(self, filename=None):
        Npanel = len(self.__panels)
        if Npanel < 1:
            return

        if self.__size:
            wx, wy = self.__size
            figsize = (wx/100.0, wy/100.0)
            dpi = 100
        else:
            figsize = None
            dpi = None

        if self.__facecolor:
            facecolor = self.__facecolor
        else:
            facecolor = None

        if self.__edgecolor:
            edgecolor = self.__edgecolor
        else:
            edgecolor = None

        fig = _my_pyplot_.figure(figsize = figsize, dpi=dpi, facecolor=facecolor, edgecolor=edgecolor, linewidth=self.__edgewidth)

        if self.__windowtitle and isinstance(self.__windowtitle, str):
            fig.canvas.manager.set_window_title(self.__windowtitle)

        if self.__graphtitle and isinstance(self.__graphtitle, str):
            kwargs = self.__graphtitleattr
            _my_pyplot_.suptitle(self.__graphtitle, **kwargs)

        if self.__graphstyle:
            _my_pyplot_.style.use(self.__graphstyle)

        ax = None
        for PanelNo in range(Npanel):
            if not self.__panels[PanelNo]:
                continue

            plots  = self.__panels[PanelNo][0]
            panelattr = self.__panels[PanelNo][1]

            if not plots:
                continue
            while not plots[0]:
                plots = plots[1:]
                if not plots:
                    break
            if not plots:
                continue

            kwargs = {}
            if self.__sharex:
                if ax is not None:
                    kwargs['sharex'] = ax
            if self.__sharey:
                if ax is not None:
                    kwargs['sharey'] = ax

            ax = _my_pyplot_.subplot(Npanel,1,PanelNo+1, **kwargs)

            xlabel = panelattr.get('xlabel', '')
            xlabelattr = panelattr.get('xlabelattr', {})
            if xlabel:
                ax.set_xlabel(xlabel, **xlabelattr)

            ylabel = panelattr.get('ylabel', '')
            ylabelattr = panelattr.get('ylabelattr', {})
            if ylabel:
                ax.set_ylabel(ylabel, **ylabelattr)

            title = panelattr.get('title', '')
            titleattr = panelattr.get('titleattr', {})
            if title:
                ax.set_title(title, **titleattr)

            p = plots[0]
            x = p[0]
            y = p[1]
            xmin = min(x)
            xmax = max(x)
            ymin = min(y)
            ymax = max(y)
            for p in plots[1:]:
                if p is None or len(p) == 0:
                    continue
                if p[0] is None or len(p[0]) == 0:
                    continue

                x = p[0]
                d = min(x)
                if d < xmin:
                    xmin = d
                d = max(x)
                if d > xmax:
                    xmax = d
                y = p[1]
                d = min(y)
                if d < ymin:
                    ymin = d
                d = max(y)
                if d > ymax:
                    ymax = d

            for p in plots:
                x = p[0]
                y = p[1]
                if len(p) > 2 and isinstance(p[2], str):
                    fmt = p[2]
                else:
                    fmt = ''

                if fmt:
                    v = ax.plot(x, y, fmt)
                else:
                    v = ax.plot(x, y)

            labels = panelattr.get('legend', False)
            if labels:
                kwargs = panelattr.get('legendattr', {})
                ax.legend(labels, **kwargs)

            xscale = panelattr.get('xscale', None)
            if xscale is not None:
                kwargs = panelattr.get('xscaleattr', {})
                ax.set_xscale(xscale, **kwargs)
            v = panelattr.get('xmin', None)
            if v is not None:
                xmin = v
            v = panelattr.get('xmax', None)
            if v is not None:
                xmax = v
            xauto = panelattr.get('xauto', False)
            if xauto:
                ax.set_xlim(auto=True)
            else:
                ax.set_xlim(xmin, xmax)

            yscale = panelattr.get('yscale', None)
            if yscale is not None:
                kwargs = panelattr.get('yscaleattr', {})
                ax.set_yscale(yscale, **kwargs)
                if ymin > 0:
                    ymin = ymin * 0.95
                else:
                    ymin = ymin * 1.05
                if ymax > 0:
                    ymax = ymax * 1.05
                else:
                    ymax = ymax * 0.95
            else:
                ymag = ymax - ymin
                yavr = (ymax + ymin)/2.0
                ymax = yavr + 0.55*ymag
                ymin = yavr - 0.55*ymag
            v = panelattr.get('ymin', None)
            if v is not None:
                ymin = v
            v = panelattr.get('ymax', None)
            if v is not None:
                ymax = v
            yauto = panelattr.get('yauto', False)
            if yauto:
                ax.set_ylim(auto=True)
            else:
                ax.set_ylim(ymin, ymax)

            ax.grid(which = 'major', color='silver', linestyle=':' )

        if self.__savepath:
            _my_pyplot_.rcParams['savefig.directory'] = self.__savepath
        else:
            _my_pyplot_.rcParams['savefig.directory'] = ''

        fig.tight_layout(rect=[0,0,1,0.96])

        if filename:
            if self.__savepath:
                filename = _my_path_.join(self.__savepath, filename)
            filename = _my_path_.normpath(filename)
            _my_pyplot_.savefig(filename)
        else:
            _my_pyplot_.show()
        _my_pyplot_.clf()
        _my_pyplot_.close()

    def plot(self, filename=None):
        self.show(filename)

    def savefig(self, filename):
        self.plot(filename)



def plot(x, y=None, fmt=None, title='', size=None):
    plt = LitePlotLib(x, y, fmt, title, size)
    plt.set_axes_xlim(auto=True)
    plt.set_axes_ylim(auto=True)
    plt.show()


# ===================================================================
#  test
# ===================================================================
if __name__ == "__main__":
    myplt = LitePlotLib()

    x1 = [0.1,  1, 10]
    y1 = [3, 0.6,   7]

    x2 = [ 1, 2, 4]
    y2 = [ 5, 1, 3]

    x3 = [-1,  2,  4]
    y3 = [ 1, -2, -1]

    ############################################################
    #  plot  =  [ XLIST, YLIST ]  or  [ XLIST, YLIST, STYLE ]  #
    ############################################################
    plot1 = [ x1, y1 ]
    plot2 = [ x2, y2, '+:r' ]
    plot3 = [ x3, y3, 'o-g' ]

    # ----------- Graph Style
    print(myplt.get_graph_style_available())
    myplt.set_graph_style('default')

    # ----------- AXES:#0
    myplt.set_axes_ylabel('Y') # AXES #0 is automatically created if there is no AXES.
    myplt.add_plots(plot1, plot2)  # plot on AXES #0
    myplt.set_axes_xlabel('Serif/Italic/x-large/bold/blue', fontstyle='italic', fontsize='x-large', fontweight='bold', fontfamily='serif', color='b')
    ### set_axes_xlabel property: https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text
    myplt.set_axes_xscale('log')
    myplt.set_axes_yscale('log') 
    ### set_?scale value: 'asinh', 'linear', 'log', 'logit', 'symlog', 'function', 'functionlog'
    ### set_axes_yscale property: https://matplotlib.org/2.2.2/api/_as_gen/matplotlib.pyplot.yscale.html
    myplt.set_axes_ylim(auto=True) # auto

    # ----------- (GLOBAL) graph title & window title (can put these anywhere before myplt.show() )
    myplt.set_graph_title('x=0.3/Oblique/xx-large/extra bold/red/black', x=0.3, fontstyle='oblique', fontweight='extra bold', fontsize='xx-large', color='r', backgroundcolor='k')
    ### set_graph_title property: https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text
    myplt.set_window_title('LitePlotLib Test')   # Set window title

    # ----------- AXES:#1
    myplt.add_new_axes(xlabel='X2', ylabel='Y2')  # create a new AXES (AXES #1)
    myplt.add_plots(plot3, plot2)   # plot on AXES #1
    myplt.set_axes_xlim(-2, 5)      # Set xmin=-2.0, xmax=5.0   on AXES #1
    myplt.set_axes_ylim(ymax=4.5)   # Set ymin=auto, ymax=4.5   on AXES #1
#    myplt.set_axes_xlim()           # Reset xmin, ymin ( equiv.: myplt.set_axes_xlim(None, None) )

    # ----------- (GLOBAL) window size and edge style (can put this anywhere before myplt.show() )
    myplt.set_window_size(1200,900)
    myplt.set_edge_width(5.0)
    myplt.set_edge_color('m')
    myplt.set_face_color('#e8e8d0')
    ### set_????_color value: 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w' or '#RRGGBB'


    myplt.show()

