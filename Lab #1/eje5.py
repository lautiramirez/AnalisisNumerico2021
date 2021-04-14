import math

#Calcula el factorial de un numero (en este caso, el numero es la constante 6).
resultado = 1
for i in range(1, 7):
    resultado = resultado * i

print("\nEl factorial de 6 usando un for es:", resultado)

#Calcula el factorial de un numero usando la libreria math.
y = math.factorial(6)
print("El factorial de 6 usando la libreria math es:", y)

print("-------------------------------------------------")
entrada = int(input("Ingrese el numero para calcular su factorial: "))

fact = math.factorial(entrada)
print(f"El factorial de {entrada} es: {fact}\n")
