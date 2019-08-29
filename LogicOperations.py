#Determinar el fresultado de la siguiente operación lógica
#       ((3 + 5x8)<3 and ((-6*4/3)+2<2)) or (a>b)

a = float(input("Da el número a: "))
b = float(input("Da el número b: "))


resultado = ((3+5*8)<3 and (-6/3*4) +2<2) or (a>b)

print(f"El resultado es: {resultado}")
