#Ejerccio escrbir la siguiente ecuación 
#       (a^3(b^2 - 2ac))/2b


a = float(input("a -> "))
b = float(input("b ->"))
c = float(input("c ->"))

resultado = (a**3 * (b**2 - 2*a*c))/(2*b)

print(f"El resultado final es {resultado}")