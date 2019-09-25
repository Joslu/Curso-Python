# Bucle For
# Hace la iteración sobre un conjunto de datos


coleccion = [1,2,3,4,"jaja"]

Dic = {
    "Luis":12,
    "Danu":29,
    "Pa":20

}
for i in Dic:
    print(f"Elemnto {Dic[i]}")

#Usando dos variables iteradoras

for clave,valor in Dic.items():
    print(f"{clave} -> {valor}")    