#Determinar área y longitud de la circunferencia del circulo

import math  #Importamos el módulo math

radio = float(input("Ingrese el radio del circulo: "))

area = (math.pi)*(radio**2)
longitud = 2*math.pi*radio

print(f"El área es {area:.2f} y la longitud es {longitud:.2f}")