#   1.  Dadas 3 variables numericas x,y,z notar las diferencias entre:
#   a)  x/y + zyx/(y + z)
#   b)  x/y*zyx/(y*z)

def ejercicio_a(x, y, z):
    a = (x/y + z)
    b = z/(y*z)
    return a, b


def ejercicio_b(x, y, z):
    a = (x/y*z)
    b = (x/(y*z))
    return a, b

x = float(input("Ingrese un valor para tu variable x: "))
y = float(input("Ingrese un valor para tu variable y: "))
z = float(input("Ingrese un valor para tu variable z: "))

a = ejercicio_a(x, y, z)
b = ejercicio_b(x, y, z)

print("Las expresiones del ejercicio 1a) son: ", a[0], "y ", a[1])
print("Las expresiones del ejercicio 1b) son: ", b[0], "y ",  b[1])
