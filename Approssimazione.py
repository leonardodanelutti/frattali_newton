import math
import numpy as np
from decimal import *
import matplotlib.pyplot as plt

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


coef = [1, 2, 0, 3]

o=0
k, l, m, n = -0.6113772-5, -0.6113772+5, -0.168317-5, -0.168317+5


while o<26:
    zoomx, zoomy = abs(k - l) / 4, abs(m - n) / 4
    dx, dy = abs(k - l) / 1000, abs(m - n) / 1000
    x, y = np.mgrid[slice(m, n, dx),
                    slice(k, l, dy)]

    lenght = len(x)

    z = [[None for i in range(len(x[1]))] for j in range(lenght)]
    """ Per colorare tutte le soluzioni
    for i in range(lenght):
        for j in range(len(x[1])):
            z[i][j], a = metodo_tangenti(complex(x[i][j], y[i][j]), p(coef), Dp(coef), 0.000001)
            if z[i][j].imag > 0.001 : z[i][j] = abs(z[i][j])
            else: z[i][j]=-1 * abs(z[i][j])
    print(o/14*100) 
    
    Per la velocità di convergenza:
    for i in range(lenght):
        for j in range(len(x[1])):
            a, z[i][j]= metodo_tangenti(complex(x[i][j], y[i][j]), p(coef), Dp(coef), 0.000001)
    print(o/14*100) 
    """

    for i in range(lenght):
        for j in range(len(x[1])):
            z[i][j], a = metodo_tangenti(complex(x[i][j], y[i][j]), p(coef), Dp(coef), 0.0001)
            z[i][j] = z[i][j].imag * z[i][j].real
    print(o/14*100, o)

    c = plt.pcolormesh(y, x, z, shading='auto')
    plt.savefig('C:/Users/USER/Documents/scuola/5° superiore/Elaborato/frattali/3/{0}.png'.format(o), bbox_inches='tight', dpi=300)
    plt.close()
    k, l, m, n = k+zoomx, l-zoomx, m+zoomy, n-zoomy
    print(k, l, m, n)
    o+=1

