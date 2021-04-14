from math import sqrt

#En este ejercicio vamos a implementar Bashkara de dos formas:
#Forma MALA: Tradicional formula de Bashkara.
#Forma BUENA: Evitamos cancelacion de digitos significativos.

def mala(a, b, c):
    """
    Esta funcion va calcular las raices de la ecuacion ax^2+bx+c = 0 usando la formula de Bashkara.
    La funcion va devolver una lista/tulpa con las dos raices encontradas.
    """
    discriminante = b**2 - 4 * a * c

    if discriminante < 0:
        print("El discriminante es negativo, entonces no tiene raices reales.")
        return None
    
    x_1 = (-b - sqrt(discriminante)) / (2*a)
    x_2 = (-b + sqrt(discriminante)) / (2*a)

    return x_1, x_2


def buena(a, b, c):
    """
    Casi lo mismo que mala, sólo que usamos Bhaskhara para calcular la raíz
    más lejana al cero y luego usamos que x_1 * x_2 = c / a para conseguir la
    segunda raíz. Esto permite eliminar errores numéricos.
    """

    discriminante = b**2 - 4 * a * c

    if discriminante < 0:
        print("El discriminante es menor que 0, por lo tanto no tiene raices reales.")
        return None
    
    if b > 0:
        x_1 = (-b - sqrt(discriminante)) / (2 * a)
    else:
        x_1 = (-b + sqrt(discriminante)) / (2 * a)

    x_2 = (c / a) / x_1

    return x_1, x_2

a = float(input("Ingrese el numero a: "))
b = float(input("Ingrese el numero b: "))
c = float(input("Ingrese el numero c: "))

res1 = mala(a,b,c)
res2 = buena(a,b,c)

print(f"Las raices con el metodo MALA son: {res1[1]} y {res1[0]}.")
print(f"Las raices con el metodo BUENA son: {res2[0]} y {res2[1]}.")
