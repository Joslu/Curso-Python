import math

Numero = int(input("Ingrese un numero: "))

while Numero < 0:
    print("Error")
    Numero = int(input("Ingrese un numero: "))

print(f"\n Su raiz cuadrada es: {(math.sqrt(Numero)):.2f}")
