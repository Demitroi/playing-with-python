# Las tuplas cumplen la misma función que las listas
# almacenar distintivos valores en una variable,
# la diferencia es que los elementos de una
# tupla no pueden ser modificados,

# Las tuplas se declaran con los valores
# entre parentesis y separados por comas.
bebidas_favoritas = ("Agua", "Café", "Refresco", "Té")
print(type(bebidas_favoritas))
# Imprime: <class 'tuple'>
print(bebidas_favoritas)
# Imprime: ('Agua', 'Café', 'Refresco', 'Té')

# Se accede a los datos igual que las listas
# con el indice entre corchetes.
print(bebidas_favoritas[1])
# Imprime: Café

# Al intentar modificar lanza una excepción.
# bebidas_favoritas[1] = "Cerveza"
# Exención: TypeError: 'tuple' object does not support item assignment
