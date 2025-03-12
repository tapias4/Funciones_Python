print("-----------------------------------")
print("-- MOSTRAR NOMBRE EN LA PANTALLA --")
print("-----------------------------------")

# definicion dela funcion
def mostrarNombre(nombre):
    """print(f"1. {nombre}")
    print(f"2. {nombre}")
    print(f"3. {nombre}")
    print(f"4. {nombre}"
    print(f"5. {nombre}")"""

    for i in range(1,6):
        print(f"{i} . {nombre}")

# Entrada 
nombre = input("Digite su nombre: ")

# Procedimiento 
mostrarNombre(nombre)

# salida
print("\nEso era ...")
