# Construir una funcion que resivacomo parametre
import random 
print("-----------------------------------")
print("--------- PROMEDIO LISTA ---------")
print("-----------------------------------")
# Definicion de la funcion 
def calcular_promedio_lista(Lista):
    suma = 0
    for i in Lista:
        suma = suma + i
    promedio = suma / len(Lista)
    return promedio


# Entrada 
# Creamos una lista vacia
Lista = []
# Tamaño de la lista 
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(14,18)
    Lista.append(num)

# procedimiento
print("Lista: ", Lista)
print("El promedio de la lista es", calcular_promedio_lista(Lista))

# salida
print("\nEso era ...")