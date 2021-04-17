from eje01 import rbisec, raiz_de_tres
import math
import matplotlib.pyplot as plt

# Parte a):

def tan_menos_dos(x):
    return math.tan(x) - 2*x

hx, hy = rbisec(tan_menos_dos, [0.8, 1.4], 1e-5, 100);

print(f"La menor solución positiva encontrada para f(x) = tan(x)-2x es : {hx[-1]}")

# Parte b):
ha, hb = rbisec(raiz_de_tres, [0, 2], 1e-5, 100)
print(f"La solución encontrada para f(x) = sqrt(3) = {ha[-1]}")

# Parte c):

#Creamos el grafico con los puntos marcados en f(c) hallados con el metodo: 
plt.plot(ha, hb, '*')

# Graficamos la función:
puntos = [0]
evals = [raiz_de_tres(0)]
for idx in range(1, 21):
    puntos.append(idx * 0.1)
    evals.append(raiz_de_tres(idx * 0.1))

# Graficamos puntos en X y evals en Y
plt.plot(puntos, evals)
plt.show()
    