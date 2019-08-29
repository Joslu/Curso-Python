#Control de flujo de un programa

# x = float(input("Ingrese un número: "))
clave = input("Ingresa OK or NOT OK: ")

if x < 20 and clave == "OK":
    print("X es menor que 30")
elif x == 20:    
    print("Es igual a 20")
else:
    print("El número es mayor que 20")
