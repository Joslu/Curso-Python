myStr = "hola compadres"

print(dir(myStr )) #dir() nos dice que se puede hacer con myStr

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("hola","jaja").upper()) #Remplaza lo primero por lo segundo
print(myStr.count('o'))

print(myStr.startswith("hola"))
Variable = myStr.endswith("jaja")
print(Variable)

#Dividir el string en dos partes, lo hace cuando detecta un caracter en blanco, se puede por una coma, o un
#caracter

print(myStr.split("a"))

#Posicion de un caracter

print(myStr.find(" ")) #Posición del caracter en blanco

print(len(myStr)) #Imprimé la longitud

print(myStr[0])
print(myStr[3])

