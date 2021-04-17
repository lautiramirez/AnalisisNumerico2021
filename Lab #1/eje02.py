# Comprobar que el epsilon-maquina es 2^(-52)=2.2204x10^(-16), escribiendo y comparando las siguientes dos lines de comando:

a = 1 + 2**-53
b = a - 1

print(a)
print(b)

print("---")

a_ = 1 + 2**(-53)
b_ = a - 1

print(a_)
print(b_)
