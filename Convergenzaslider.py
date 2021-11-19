import math
import numpy as np
from decimal import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox
import mpl_interactions.ipyplot as iplt

getcontext().prec = 25


def f(x):
    return 2 * np.log(x, dtype="float64") - x / 4


def Df(x):
    return 2 / x + 1 / 4


def p(coefficente):
    def f_polinomio(x):
        p_coef = 0
        for a in range(len(coefficente)):
            p_coef = p_coef + coefficente[a] * (x ** a)
        return p_coef

    return f_polinomio


def Dp(coefficente):
    def Df_polinomio(x):
        Dp_coef = 0
        for a in range(len(coefficente) - 1):
            Dp_coef = Dp_coef + coefficente[a + 1] * (a + 1) * (x ** a)
        return Dp_coef

    return Df_polinomio


def metodo_bisezione(a, b, f, errore):
    n = 0
    while n < math.log((b - a) / (2 * errore), 2):
        c = (a + b) / 2
        if f(c) == 0:
            return c
            break
        if np.sign(f(c)) == np.sign(f(a)):
            a = c
        else:
            b = c
    return c


def metodo_tangenti(a, f, Df, errore):
    n = 0
    differenza = errore + 1
    while differenza >= errore:
        b = a
        if Df(b) == 0:
            a = b - (f(b) / (Df(b) + errore))
        else:
            a = b - (f(b) / Df(b))
        differenza = abs(b - a)
        n += 1
    return a, n


coef = [5,-6,-29,6]

a_min = 1    # the minimial value of the paramater a
a_max = 200   # the maximal value of the paramater a


centro = 2.516
ampiezza_intervallo = 8


m, n = centro - ampiezza_intervallo/2, centro + ampiezza_intervallo/2
init_zoom = 1
x = np.linspace(m, n, 1000000)
lenght = len(x)
y = [None for i in range(len(x))]

for i in range(lenght):
    y[i], k = metodo_tangenti(x[i], p(coef), Dp(coef), 0.01)

fig = plt.figure()
conv_ax = plt.axes([0.1, 0.2, 0.8, 0.65])
slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])


plt.axes(conv_ax)
plt.title('y = sin(ax)')
conv_plot, = plt.plot(x, y, 'bo')
plt.xlim(centro - ampiezza_intervallo/2, centro + ampiezza_intervallo/2)
plt.ylim(min(y)-1, max(y)+1)

a_slider = Slider(slider_ax, 'a', a_min, a_max, valinit=init_zoom)

def update(a):
    plt.title((1.05)**a)
    plt.xlim(centro - ampiezza_intervallo/(2*(1.05)**a), centro + ampiezza_intervallo/(2*(1.05)**a))
    fig.canvas.draw_idle()

controls2 = iplt.plot(x, y, 'bo', freq=a_slider)
a_slider.on_changed(update)
anim2 = controls2.save_animation('C:/Users/USER/Documents/scuola/5° superiore/Elaborato/frattali/7/{0}.gif'.format(1), fig, "freq", interval=120, N_frames=100)
plt.show()
