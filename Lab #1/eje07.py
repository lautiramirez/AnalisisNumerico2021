# Este programa calcula la n-esima potencia del numero real x:
def n_potencia(x , n):
    return x**(n)

a = int(input("Ingrese el numero real: "))
b = int(input("Ingrese el numero de la potencia: "))

res = n_potencia(a, b)
print(f"{a} elevado a la {b} es: {res}")

print("-----------------------------------------------")

#Este programa imprime las primeras 5 potencias de un numero ingresado:
def primerasPotencias(x, n):
    for i in range(1, n+1):
        print(f"La {i} potencia de {x} es: {n_potencia(x, i)}")
    return None

c = int(input("Ingrese un numero: "))
primerasPotencias(c, 5)
