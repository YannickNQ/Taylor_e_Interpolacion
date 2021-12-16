import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

# INGRESO
x = sym.Symbol('x')
fx = sym.exp(x)

x0 = 0
n = 4

#PROCEDIMIENTO
k = 0
polinomio = 0
while not (k>n):
    derivada = fx.diff(x, k)
    derivadax0 = derivada.subs(x, x0)
    divisor = np.math.factorial(k)

    terminok = (derivadax0/divisor)*(x-x0)**k

    polinomio = polinomio + terminok
    k = k + 1

#SALIDA

print(polinomio)

#GRAFICA
a = -2
b = 2
muestras = 15

xi = np.linspace(a,b, muestras)
fxn = sym.lambdify(x, fx)
fi = fxn(xi)

px = sym.lambdify(x, polinomio)
pi = px(xi)

plt.plot(xi, fi)
plt.plot(xi, pi)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Polinomio de Taylor')
plt.axvline(0)
plt.axhline(0)
plt.show()