#Implentacion de la funcion SonReciprocos que devuelve True si dos numeros xy son inversos:
import random

def SonReciprocos(x, y):
    if x * y == 1:
        return True
    else:
        return False


x = float(input("Ingresa el numero x: "))
y = float(input("Ingresa el numero y: "))

for i in range(100):
    x = 1 + random.random()
    y = 1/x
    if not SonReciprocos(x,y):
        print(x)
        # Cuando entra a este if significa que la division en y = 1/x no es exacta, pq luego al multiplicarlo en la funcion SonReciprocos no da 1 y eso es absurdo. Por lo tanto hay casos donde se pierde precision.
