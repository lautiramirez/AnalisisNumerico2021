#Implemntacion de la funcion SonOrtogonales que el mismo nombre de la funcion ya nos dice cual es su utilidad en esta vida.

def SonOrtogonales(v1, v2):
    if (v1[0]*v2[0] + v1[1]*v2[1]) == 0:
        return True
    else:
        return False

x = [1, 1.1024074512658109]
y = [-1, 1/x[1]]

if not SonOrtogonales(x, y):
    print("Algo salió mal...")
    # Nuevamente algo salio mal por poblemas de precision.