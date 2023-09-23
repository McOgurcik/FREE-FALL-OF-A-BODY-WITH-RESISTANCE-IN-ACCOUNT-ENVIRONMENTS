import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle
import PySimpleGUI as sg
import math
import matplotlib as mt
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

def plot_figure(m,ro,c,s,p):
    g = 9.80665
    ax_1.cla()
    ax_2.cla()
    # v,t,h массивы
    x0 = 50
    y0 = 50
    # k_2
    k = 0.5*c*s*p
    v = []
    t = []
    h = []
    v.append(0)
    t.append(ro)
    h.append(0)
    dot = True
    for i in range(100*ro):
        v.append(v[i]+ro/2*((m*g-k*v[i]*v[i])/m)+(m*g-k*((v[i]+ro*(m*g-k*v[i]*v[i])/m)**2))/m)
        if (abs(v[i]-v[i+1])<0.1) and (dot == True):
            ax_1.set_xlabel(r'${v}$'+f' = const = {v[i]:.{3}f} при t = {t[i]:.{3}f}', fontsize=16)
            ax_1.add_patch(plt.Circle((t[i],v[i]),0.7,color='blue'))
            dot = False
        t.append(t[i]+ro)
        h.append(v[i+1]*t[i+1])

    ax_1.set_xlim(0, x0)
    ax_1.set_ylim(0, y0)
        # ax.set_title(r'${V}_0$'+f' = {v0}, α = {a}', fontsize=32)
        # if l == np.max(x):
        #   ax.set_xlabel(f'L = {l} - Максимальная дальность полёта')
        # else:
        #   ax.set_xlabel(f'L = {l}')
        # ax.set_ylabel(f'H = {np.max(y)} - Максимальная высота')
    ax_1.set_title('График зависимости v от t', fontsize=16)
    ax_2.set_title('График зависимости h от t', fontsize=16)
    ax_1.plot(t, v, color='g')

    ax_2.plot(t, h, color='r')
    canvas.draw()
    # except:
    #     ax.plot(v, t, color='g')
    #     print('gg')

layout = [
    [sg.Canvas(size=(640, 480), key='Canvas')],
    [[sg.Text('m'), sg.InputText(70,enable_events=True,k='-M-'),sg.Text('kg')],[sg.Text('ro'), sg.InputText(1,enable_events=True,k='-R-'),sg.Text('с')]],
    [[sg.Text('c'), sg.InputText(70,enable_events=True,k='-C-')],[sg.Text('S'), sg.InputText(70,enable_events=True,k='-S-')],[sg.Text('p'), sg.InputText(70,enable_events=True,k='-P-')]],
    [[sg.Push(), sg.Button('go'), sg.Push()]]
    ]
# sg.theme('DefaultNoMoreNagging')
window = sg.Window('Свободное падение',
                   layout,
                   finalize=True,
                   resizable=True)
# plt.figure(figsize=(cm_to_inch(h_w), cm_to_inch(w_w)))
fig = Figure(figsize=(cm_to_inch(16), cm_to_inch(10)))
ax_1 = fig.add_subplot(2, 1, 1)
ax_2 = fig.add_subplot(2, 1, 2)
canvas = Canvas(fig, window['Canvas'].Widget)
def launch():
    return plot_figure(m,ro,c,s,p)
while True:

  event, values = window.read()
  # print(event)
  if event in (sg.WIN_CLOSED, 'Exit'):
    break
  elif event == '-M-':
      m = float(values[event])
      # launch()
  elif event == '-R-':
      ro = float(values[event])
      # launch()
  elif event == '-C-':
      c = float(values[event])
      # launch()
  elif event == '-S-':
      s = float(values[event])
      # launch()
  elif event == '-P-':
      p = float(values[event])
      # launch()
  elif event == 'go':
      launch()


window.close()
