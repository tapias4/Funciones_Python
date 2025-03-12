
import random 
print("-----------------------------------")
print("-------- SUMA LISTA DATOS --------")
print("-----------------------------------")

# Definicion de la funcion 
def sumar_lista_datos(Lista):
    suma = 0
    for i in Lista:
        suma = suma + i 
    return suma

# Entrada 
# Creamos una lista vacia
Lista = []
# Tamaño de la lista 
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1,9)
    Lista.append(num)


# procedimiento
print("Lista: ", Lista)
print("La suma es", sumar_lista_datos(Lista))


# salida
print("\nEso era ...")

