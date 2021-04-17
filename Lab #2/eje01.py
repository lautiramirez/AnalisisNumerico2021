#Implementación del METODO DE BUSECCIÓN: (Especie de busqueda binaria de raices de una función).

def rbisec (fun, I, err, mit):
    # Intervalos de la función:
    a = I[0]
    b = I[1]

    # hx: historial de puntos medios: [c]
    # hf: historial de valores funcionales: [f(c)]
    hx = []
    hf = []

    # Caso donde el intervalo no este ordenado de forma creciente.
    if  a >= b:
        print("A no es menor que b, ingrese un intervalo valido.")
        return hx, hf

    # Caso en donde en el intervalo no haya raices.
    if fun(a) * fun (b) >= 0:
        print("f(a) y f(b) tienen el mismo signo ó alguna es igual a 0")
        return hx, hf

    for i in range(mit):
        c = (a + b)/2
        fun_c = fun(c)

        hx.append(c)
        hf.append(fun_c)

        if abs(fun_c) < err:
            print("Encontramos una raiz.")
            break
            
        if fun_c * fun(a) < 0:
            b = c
        elif fun_c * fun(a) > 0:
            a = c
    
    return hx, hf

# Función necesaria para el eje2:
def raiz_de_tres(x):
    return x**2-3