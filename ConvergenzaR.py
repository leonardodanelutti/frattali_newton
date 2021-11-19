import math
import numpy as np
from decimal import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

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

o = 0
m, n = 2.516 - 4, 2.516 + 4
init_zoom = 1

while o < 14:
    zoomx = abs(m - n) / 4
    dx = abs(m - n) / 400
    x = np.mgrid[slice(m, n, dx)]
    lenght = len(x)
    y = [None for i in range(len(x))]

    for i in range(lenght):
        y[i], k = metodo_tangenti(x[i], p(coef), Dp(coef), 0.000001)

    c = plt.plot(x, y, 'bo')
    plt.savefig('C:/Users/USER/Documents/scuola/5° superiore/Elaborato/frattali/6/{0}.png'.format(o),
                bbox_inches='tight', dpi=300)
    plt.close()
    m, n = m + zoomx, n - zoomx
    print(m, n)
    o += 1