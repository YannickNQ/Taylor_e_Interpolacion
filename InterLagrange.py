import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
#INGRESO DATOS DE PRUEBA
xi = np.array([1.5, 2.7, 5.6, 7.2])
fi = np.array([-5., 2., -2., 10.0])

#PROCEDIMIENTO

n = len(xi)
x= sym.Symbol('x')
polinomio = 0
for i in range(0,n,1):
    numerador = 1
    denominador = 1
    for j in range (0,n,1):
        if (i!=j):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i] - xi[j])
        termino = (numerador/denominador)*fi[i]
    polinomio = polinomio + termino
polisimple = sym.expand(polinomio)

px = sym.lambdify(x, polinomio)
#vectores para graficas
a = np.min(xi)
b= np.max(xi)
muestras = 51
p_xi = np.linspace(a,b,muestras)
pfi = px(p_xi)

#SALIDA
print('Polinomio')
print(polinomio)
print('PolinomioSimple')
print(polisimple)
print(px(3.5))
#GRAFICA
plt.plot(xi, fi, 'o')
plt.plot(p_xi, pfi)
plt.title('Interpolación por Lagrange')
plt.show()