from math import sqrt

def f(x):
    return sqrt(x**2 + 1) - 1

def g(x):
    return x**2/(sqrt(x**2 + 1) + 1)

for i in range(20):
    x = 8**(-i)
    print(f"f(x) = {f(x)}, g(x) = {g(x)}") 

#Lo que sucede es que por razones extrañas, posiblemente de problemas de presicion, las funciones son iguales pero dan distintos resultados.