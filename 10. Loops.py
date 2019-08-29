# In Python, we can iterate in different forms. I’ll talk about for.

foods = ["Pozole", "Carnitas", "Hot-Dogs","Chalupas"]

#Para acceder de forma muy básica sería de la siguiente forma

print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])

# Es mejor usar for para iterar 

for food in foods:
    print(food)


for i in range(1,50):
    if i == 30:
        break
    print(i)

#Otro bucle conocido es while

count = 0
while count < 11:
    print(count)
    count += 1


#Bucle para imprimir cada caracter
cadena = "Hola amigos"


for i in cadena:
    print(i)
