# Esta funcion va devolver el maximo de dos numeros reales:

def maxNumero(x, y):
    if x > y:
        print(f"El mayor numero es {x}")
        return x
    elif x < y:
        print(f"El mayor numero es {y}")
        return y
    elif x == y:
        print(f"Ambos numeros son iguales a {x}")
        return x

a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))

res = maxNumero(a, b)
