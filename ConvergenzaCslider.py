import math
import numpy as np
from decimal import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

getcontext().prec = 25

def f(x):
    return 2 * np.log(x, dtype="float64") - x / 4


def Df(x):
    return 2 / x - 1 / 4


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


def metodo_bisezione(a, b, f, errore):  # definizione della funzione
    n = 0
    while n < math.log((b - a) / (2 * errore), 2):  # ciclo che si ripete un numero di volte pari a
        c = (a + b) / 2  # assegnazione del punto medio
        if f(c) == 0:  # terminazione del ciclo se il punto medio corrisponde allo 0
            return c
            break
        if np.sign(f(c)) == np.sign(f(a)):  # scelta del nuovo intervallo
            a = c
        else:
            b = c
        n += 1
    return c, n  # output funzione


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

res = 1200
centrox, centroy = -0.168317, -0.6113772
ampiezza_intervallox, ampiezza_intervalloy = 10, 10

m, n, l, k = centrox - ampiezza_intervallox / 2, centrox + ampiezza_intervallox / 2, centroy - ampiezza_intervalloy / 2, centroy + ampiezza_intervalloy / 2

x = np.linspace(m, n, res)
y = np.linspace(l, k, res)  # Possiamo creare un array bi-dimensionale e associare ad ogni valore un punto del piano complesso.

fig = plt.figure()
ax = plt.axes()

def animate(i):
    ax.clear()  # clear axes object
    ax.set_xticks([])  # clear x-axis ticks
    ax.set_yticks([])
    m, n, l, k = centrox - ampiezza_intervallox / (2 * (1.048) ** i), centrox + ampiezza_intervallox / (2 * (1.05) ** i), \
                 centroy - ampiezza_intervalloy / (2 * (1.048) ** i), centroy + ampiezza_intervalloy / (2 * (1.05) ** i)

    x = np.linspace(m, n, res)
    y = np.linspace(l, k, res)

    z = [[None for i in range(len(x))] for j in range(len(y))]

    for i in range(len(x)):
        for j in range(len(y)):
            a, z[i][j] = metodo_tangenti(complex(x[i], y[j]), p(coef), Dp(coef), 0.001)
            # z[i][j] = z[i][j].imag * z[i][j].real

    img = plt.pcolormesh(x, y, z, shading='auto')
    return [img]



anim = animation.FuncAnimation(fig, animate, frames=390, interval=60, blit=True)
anim.save('C:/Users/USER/Documents/scuola/5° superiore/Elaborato/frattali/9/2.gif', writer='imagemagick', dpi=300)
plt.show()
