# EL ciclo for se utiliza para iterar sobre una
# secuencia (lista, tupla, string) u otros objetos iterables.

# Se puede iterar sobre una lista.
colores_favoritos = ["Rojo", "Negro", "Blanco", "Naranja", "Rosa"]
for color in colores_favoritos:
    print(color)
    # Imprime los colores en la lista

# Sobre una tupla.
bebidas_favoritas = ("Agua", "Café", "Refresco", "Té")
for bebida in bebidas_favoritas:
    print(bebida)
    # Imprime las bebidas de la tupla

# Las listas contienen claves y valores, con for
# se puede acceder a estas utilizando la función items.
persona = {"Nombre": "Sergio",
           "Apellido": "Contreras",
           "Estatura": 1.81}
for clave, valor in persona.items():
    print(clave, valor)
    # Imprime las claves y los valores

# Igualmente se puede iterar sobre un string.
mensaje = "Hola Bro"
for letra in mensaje:
    print(letra)
    # Imprime cada una de las letras

# la función range permite iterar sobre rangos.
for n in range(1, 10):
    print(n)
    # Imprime los números del 1 al 10
