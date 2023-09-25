import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle
import PySimpleGUI as sg
import math
import matplotlib as mt
x0 = 50
y0 = 50
h_w = 12
w_w = 2
ro = 2
m = 80
p = 1.29
c = 1.22
# s = рост * полуобхват
s = 0.7
class Canvas(FigureCanvasTkAgg):
  """
    Create a canvas for matplotlib pyplot under tkinter/PySimpleGUI canvas
    """

  def __init__(self, figure=None, master=None):
    super().__init__(figure=figure, master=master)
    self.canvas = self.get_tk_widget()
    self.canvas.pack(side='top', fill='both', expand=1)

def cm_to_inch(value):
  return value / 2.54

def plot_figure(m,ro,c,s,p,x0,y0):
    g = 9.80665
    ax_1.cla()
    ax_2.cla()
    # v,t,h массивы

    # k_2
    try:
        m = float(m)
        ro = float(ro)
        c = float(c)
        s = float(s)
        p = float(p)
        k = 0.5*c*s*p
        v = []
        t = []
        h = []
        v.append(0)
        t.append(ro)
        h.append(0)
        dot = True
        rn = 100
        i = 0
        while (rn>0):
            v.append(v[i]+ro/2*((m*g-k*v[i]*v[i])/m)+(m*g-k*((v[i]+ro*(m*g-k*v[i]*v[i])/m)**2))/m)
            if (abs(v[i]-v[i+1])<0.1):
                    if (dot == True):
                        # ax_1.set_xlabel(r'${v}$'+f' = const = {v[i]:.{3}f} при t = {t[i]:.{3}f}', fontsize=16)
                        ax_1.text(t[i]+2,v[i]-8,r'${v}$'+f' = const = {v[i]:.{3}f} при t = {t[i]:.{3}f}', fontsize=10, color='black')
                        ax_1.add_patch(plt.Circle((t[i],v[i]),0.7,color='blue'))
                        dot = False
                    rn = rn - 1
            t.append(t[i]+ro)
            h.append(h[i]+v[i+1]*ro)
            i = i+1
    except:
        return
    # calculation
    ax_1.grid(True, linestyle='--', alpha=0.5)
    ax_1.set_xlim(0, x0)
    ax_1.set_ylim(0, y0)
    ax_2.set_xlim(0, x0)
    # ax_2.set_ylim(0, y0)
    ax_1.set_title('График зависимости v от t', fontsize=12)
    ax_2.set_xlabel('График зависимости h от t', fontsize=12)
    ax_1.plot(t, v, color='g')

    ax_2.plot(t, h, color='r')
    canvas.draw()

layout = [
    [sg.Canvas(size=(640, 480), key='Canvas')],
    [sg.Text('m'), sg.Input(70,enable_events=True,k='-M-',size=(5, 1)),sg.Text('ro'), sg.Input(1,enable_events=True,k='-R-',size=(5, 1)),sg.Text(text="xm"),
    sg.Spin([i for i in range(-200, 200)],
            initial_value=50,
            enable_events=True,
            k='-X-'),
    sg.Text(text="ym"),
    sg.Spin([i for i in range(-200, 200)],
            initial_value=50,
            enable_events=True,
            k='-Y-')],
    [[sg.Text('c'), sg.Input(1.22,enable_events=True,k='-C-',size=(5, 1)),sg.Text('S'), sg.Input(0.7,enable_events=True,k='-S-',size=(5, 1)),sg.Text('p'), sg.Input(1.29,enable_events=True,k='-P-',size=(5, 1))]],
    [[sg.Push(), sg.Button('go'), sg.Push()]]
    ]
# sg.theme('DefaultNoMoreNagging')
window = sg.Window('Свободное падение',
                   layout,
                   finalize=True,
                   resizable=True, size = (640, 520))
# plt.figure(figsize=(cm_to_inch(h_w), cm_to_inch(w_w)))
fig = Figure(figsize=(cm_to_inch(16), cm_to_inch(10.7)))
ax_1 = fig.add_subplot(2, 1, 1)
# fig.subplots_adjust(top=0.8, bottom=0.1)
ax_2 = ax_1.twinx()
ax_2 = fig.add_subplot(2, 1, 2)
canvas = Canvas(fig, window['Canvas'].Widget)
def launch():
    return plot_figure(m,ro,c,s,p,x0,y0)
while True:

  event, values = window.read()
  # print(event)
  if event in (sg.WIN_CLOSED, 'Exit'):
    break
  elif event == '-M-':
      m = values[event]
      # launch()
  elif event == '-R-':
      ro = values[event]
      # launch()
  elif event == '-C-':
      c = values[event]
      # launch()
  elif event == '-S-':
      s = values[event]
      # launch()
  elif event == '-P-':
      p = values[event]
      # launch()
  elif event == '-Y-':
    # print(values)
    y0 = values[event]
    launch()
  elif event == '-X-':
    # print(values)
    x0 = values[event]
    launch()
  elif event == 'go':
      launch()


window.close()
