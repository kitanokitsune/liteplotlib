# Lite Plot Library API

## コンストラクタ

| コンストラクタ | 説明  |
| :-----   | :---- |
| **LitePlotLib**(x=*None*, y=*None*, fmt=*None*, title='', size=*None*, sharex=*False*, sharey=*False*) | 引数は全て省略可能です（その場合は中身が空のインスタンスが生成されます）。x に曲線のX座標データの数値リスト、y に曲線のY座標データの数値リストを指定し、fmtにはプロットする線のスタイル（[Format Strings]( https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html )）を指定します（メソッド add_plot(x,y,fmt) でも設定可能）。x が与えられ y が与えられなかった場合は、x がY座標データを表し、X座標データは __[__*n* __for__ *n* __in__ __range__(__len__(x))__]__  によって自動生成されます。titleにはグラフのタイトルを指定します（メソッド set_graph_title() でも設定可能）。size にはウィンドウのサイズをピクセル単位で size=(*width*, *height*) のようにタプルで指定します（メソッド set_window_size(*width*, *height*) でも設定可能）。sharex, sharey に True を設定すると複数の Axes（パネル）がある場合に軸の拡大・縮小の動作が Axes 間で連動します（メソッド set_sharex(*True*)、set_sharey(*True*) でも設定可能） |

## メソッド

### 基本

| メソッド | 説明  |
| :-----   | :---- |
| **add_plot**(x, y=*None*, fmt=*None*) | 現在の Axes（パネル）にプロット（曲線）を追加します。x に曲線のX座標データの数値リスト、y に曲線のY座標データの数値リストを指定します。x が与えられ y が与えられなかった場合は、x がY座標データを表し、X座標データは __[__*n* __for__ *n* __in__ __range__(__len__(x))__]__  によって自動生成されます。fmt には線のスタイル（[Format Strings]( https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html )）を指定します（省略可能）。add_plot() を連続して実行すると、同じ Axes 上に複数のプロット（曲線）を重ねて表示します |
| **show**() | ウィンドウを作成し、その上にグラフを表示します。ウィンドウ上でグラフの Zoom や Pan などの操作が可能です。show() は必要なデータ入力と設定が全て終わってから呼び出してください。show() より後ろで行われた設定はグラフに反映されません |


### 保存

| メソッド | 説明  |
| :-----   | :---- |
| **savefig**(filename) | グラフを画像データとして filename で示されるファイル（.png）へ保存します。filename はフルパスでもファイル名のみでも構いません。ファイル名のみの場合は set_save_dir() で指定されたディレクトリに保存されます。savefig() は必要なデータ入力と設定が全て終わってから呼び出してください。savefig() より後ろで行われた設定は画像に反映されません |
| **save_plot_data**(filename) | 現在のインスタンスの内部状態を filename で示されるファイルへ保存します。このファイルを restore_plot_data() で読み込むとインスタンスの内部状態を復元できます。filename はフルパスでもファイル名のみでも構いません。ファイル名のみの場合は set_save_dir() で指定されたディレクトリに保存されます |
| **restore_plot_data**(filename) | save_plot_data() で保存されたファイル（filename）からグラフのデータ（内部状態）をロードして復元します。filename はフルパスでもファイル名のみでも構いません。ファイル名のみの場合は set_save_dir() で指定されたディレクトリが仮定されます |
| **set_save_dir**(path=*None*) | 画像の保存（savefig()）やプロットデータの保存（save_plot_data()）のデフォルトの保存ディレクトリを設定します |


### Axes操作

| メソッド | 説明  |
| :-----   | :---- |
| **add_new_axes**(plots=*None*, xlabel='', ylabel='') | 現在の Axes（パネル）の下に新たな Axes を追加します。これ以降、add_plot() や set_axes_...() の操作は、この新たな Axes に対して行われます。plots を指定すると、新たに Axes を追加してからその上にプロット（曲線）を追加します。Plots はプロットデータのリストであり、[ [xlist1, ylist1, fmt1], [xlist2, ylist2, fmt2], ...] の形式です。fmt は線のスタイル（[Format Strings]( https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html )）です。なおリスト中の fmt は省略できます（xlist と ylist は省略できません）。xlabel と ylabel はそれぞれ X軸ラベル、Y軸ラベルです。なお、LitePlotLib のインスタンスを生成すると自動で初期 Axes が生成されるため（*AXES#0*）、インスタンス生成直後の add_new_axes() は不要です |
| **set_axes_xlim**(xmin=*None*, xmax=*None*, auto=*False*) | 現在の Axes のX軸のリミット（表示範囲）を設定します。xmin または xmax いずれか片方のみ設定した場合は、設定されなかった方の範囲が自動で計算されます。auto が True の場合はリミットが自動で計算されます |
| **set_axes_ylim**(ymin=*None*, ymax=*None*, auto=*False*) | 現在の Axes のY軸のリミット（表示範囲）を設定します。ymin または ymax いずれか片方のみ設定した場合は、設定されなかった方の範囲が自動で計算されます。auto が True の場合はリミットが自動で計算されます |
| **set_axes_xylabel**(xlabel, ylabel) | 現在の Axes のX軸ラベルとY軸ラベルを設定します。ラベルは文字列で指定します |
| **set_axes_xlabel**(label, _**kwargs_) | 現在の Axes のX軸ラベルを設定します。ラベルは文字列で指定します。オプション引数（_**kwargs_）は [matplotlib.axes.Axes.set_xlabel()](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html) に渡され、ラベルの装飾や細かな設定に利用できます |
| **set_axes_ylabel**(label, _**kwargs_) | 現在の Axes のY軸ラベルを設定します。ラベルは文字列で指定します。オプション引数（_**kwargs_）は [matplotlib.axes.Axes.set_ylabel()](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html) に渡され、ラベルの装飾や細かな設定に利用できます |
| **set_axes_xscale**(xscale=*None*, _**kwargs_) | 現在の Axes のX軸のスケールを設定します。xscale に設定可能な値（文字列）は matplotlib のマニュアル（[matploglib3.3より前](https://matplotlib.org/2.2.2/api/_as_gen/matplotlib.pyplot.xscale.html)、[matploglib3.3以降](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html)）を参照してください。オプション引数（_**kwargs_）は matplotlib.axes.Axes.set_xscale() に渡され、スケールの細かな設定に利用できます |
| **set_axes_yscale**(yscale=*None*, _**kwargs_) | 現在の Axes のY軸のスケールを設定します。yscale に設定可能な値（文字列）は matplotlib のマニュアル（[matploglib3.3より前](https://matplotlib.org/2.2.2/api/_as_gen/matplotlib.pyplot.yscale.html)、[matploglib3.3以降](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html)）を参照してください。オプション引数（_**kwargs_）は matplotlib.axes.Axes.set_yscale() に渡され、スケールの細かな設定に利用できます |
| **set_axes_title**(title, _**kwargs_) | 現在の Axes のタイトルを文字列で指定します。 オプション引数（_**kwargs_）は [matplotlib.axes.Axes.set_title()](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html) に渡され、Axes タイトルの装飾や細かな設定に利用できます |
| **set_axes_legend**(labels, _**kwargs_) | 現在の Axes の凡例を表示します。labels は曲線のラベル文字列のリストです。labels 内のラベル文字列の順序は曲線の add_plot() 実行順に対応しています。オプション引数（_**kwargs_）は [matplotlib.axes.Axes.legend()](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html) に渡され、凡例の装飾や細かな設定に利用できます |


### 応用

| メソッド | 説明  |
| :-----   | :---- |
| **set_graph_title**(title, _**kwargs_) | グラフのタイトルを設定します。オプション引数（_**kwargs_）は [matplotlib.pyplot.suptitle()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html) へ渡され、グラフタイトルの装飾や細かな設定に利用できます |
| **set_window_title**(title): | ウィンドウのタイトルを設定します。ウィンドウタイトルは `save the figure` ボタンで画像を保存する際のデフォルトファイル名としても使われます |
| **set_window_size**(x, y) | ウィンドウのサイズをピクセル単位で設定します。なお show() で表示されるウィンドウのサイズは、環境によって多少大きさが変わります。savefig() で画像として保存する場合は、ここで指定したサイズになります |
| **set_sharex**(*True* or *False*) | 引数を True にすると、複数の Axes がある場合に Zoom や Pan を行うと全ての Axes でX軸の表示範囲が連動して変化します |
| **set_sharey**(*True* or *False*) | 引数を True にすると、複数の Axes がある場合に Zoom や Pan を行うと全ての Axes でY軸の表示範囲が連動して変化します |
| **set_graph_style**(style=*None*) | グラフの[スタイル](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)を設定します。指定可能なスタイルは get_graph_style_available() で調べることができます |
| **get_graph_style_available**() | 指定可能なグラフスタイルの一覧をリストで返します |
| **set_face_color**(color=*None*) | ウィンドウの色を設定します。引数には 'r', 'g', 'b', 'c', 'm', 'y', 'w', 'k' と16進数 '#*RRGGBB*' が指定可能です。 |
| **set_edge_color**(color=*None*) | グラフの枠の色を設定します。引数には 'r', 'g', 'b', 'c', 'm', 'y', 'w', 'k' と16進数 '#*RRGGBB*' が指定可能です。なお、set_edge_width() で線幅を 0 より大きな値に設定しないと視覚効果が現れません |
| **set_edge_width**(width=0.0) | グラフの枠の太さを設定します |


