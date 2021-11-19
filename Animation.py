import math
import numpy as np
from decimal import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox

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


coef = [-1, 0, 0, 1]

a_min = 1    # the minimial value of the paramater a
a_max = 200   # the maximal value of the paramater a

res = 200

centrox, centroy = 0, 0
ampiezza_intervallox, ampiezza_intervalloy = 8, 8

m, n, l, k = centrox - ampiezza_intervallox/2, centrox + ampiezza_intervallox/2, centroy - ampiezza_intervalloy/2, centroy + ampiezza_intervalloy/2
init_zoom = 1

x = np.linspace(m, n, res)
y = np.linspace(l, k, res)
z = [[None for i in range(len(y))] for j in range(len(x))]

for i in range(len(y)):
    for j in range(len(x)):
        z[i][j], a = metodo_tangenti(complex(x[j], y[i]), p(coef), Dp(coef), 0.000001)
        z[i][j] = z[i][j].imag * z[i][j].real

fig = plt.figure()
conv_ax = plt.axes([0.1, 0.2, 0.8, 0.65])
slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])

plt.axes(conv_ax)
plt.title('y = sin(ax)')
conv_plot = plt.pcolormesh(x, y, z)
plt.xlim(m, n)
plt.ylim(l, k)

a_slider = Slider(slider_ax, 'a', a_min, a_max, valinit=init_zoom)

def update(a):
    m, n, l, k = centrox - ampiezza_intervallox / (2*(1.05)**a), centrox + ampiezza_intervallox / (2*(1.05)**a), centroy - ampiezza_intervalloy / (2*(1.05)**a), centroy + ampiezza_intervalloy / (2*(1.05)**a)
    plt.title((1.05)**a)
    x = np.linspace(m, n, res)
    y = np.linspace(l, k, res)
    z = [[None for i in range(len(y))] for j in range(len(x))]

    for i in range(len(y)):
        for j in range(len(x)):
            z[i][j], a = metodo_tangenti(complex(x[j], y[i]), p(coef), Dp(coef), 0.000001)
            z[i][j] = z[i][j].imag * z[i][j].real
    plt.xlim(m, n)
    plt.ylim(l, k)
    conv_plot = plt.pcolormesh(x, y, z)
    fig.canvas.draw_idle()


a_slider.on_changed(update)

def buildmebarchart(a=int):


import matplotlib.animation as ani
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 100)
plt.show()
