

print("---------------------------------")
print("--- MOSTRAR CADENA N VECES EN ---")
print("------------PANTALLA-------------")
print("---------------------------------")

def mostrarCadena(cadena,n):
    for i in range(1,n):
        print(f"{i} . {cadena}")

# entrada 
cadena = input("Digite la cadena a mostrar: ")
n = int(input("Digite el numero de veces que quiere mostrar la cadena: "))

# procedimiento 
mostrarCadena(cadena, n)

# salida
print("\nEso era ...")