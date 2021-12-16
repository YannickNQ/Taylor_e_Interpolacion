import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

#INGRESO
xi = np.array([550, 600])
fi = np.array([1.040 , 1.051])
#PROCEDIMIENTO

#n = len(xi)
x = 570

res = 0

numerador = x - xi[0]  #x - 550
denominador = xi[1] - xi[0] #600 - 550
multi = fi[1]- fi[0] #1.051 - 1.040

res = (numerador/denominador)*(multi) + fi[0]

#SALIDA
print(res)
#GRAFICA

plt.plot(xi,fi,'o')
plt.plot(x, res, 'o')
plt.plot(xi,fi)
plt.show()