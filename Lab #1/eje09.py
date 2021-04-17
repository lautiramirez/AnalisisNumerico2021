# Esta funcion es una implementacion del Algoritmo de Horner, para la evaluacion de polinomios:

def horn(coefs, x):
    n = len(coefs)
    b = coefs[0]
    for i in range(1,n):
        b = coefs[i] + b * x

    return b

n = int(input("Ingrese el grado del polinomio: "))
arr_coefs = []

for i in range(0, n): 
    x = int(input(f"Ingrese el coeficiente  de x^{n-i-1}: "))
    arr_coefs.append(x)

print("La funcion ingresada es: ", end='')
for i in range(0, n):
    if i != n-1:
        print(f"{arr_coefs[i]}x^{n-i-1} + ", end='')
    else:
        print(f"{arr_coefs[i]}")

x0 = int(input("\n\nIngrese el x a evaluar en el polinomio: "));
p = horn(arr_coefs, x0)
print(f"El valor del polinomio evaluado en {x0} es: {p}.")
