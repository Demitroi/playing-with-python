# Las listas pueden contener varios datos
# Se declaran con corchetes y los valores separados,
# Los valores pueden ser de distintos tipos incluso listas.
# por comas, Por ejemplo:
numeros_favoritos = [7, 6, 14, 21, 4]
print(type(numeros_favoritos))
# Imprime: <class 'list'>
print(numeros_favoritos)
# Imprime: [7, 6, 14, 21, 4]

# Se accede a un dato por su indice
# los cuales empiezan desde el cero.
print(numeros_favoritos[3])
# Imprime: 21

# De igual forma se puede modificar
# indicando el indice de la lista
# y asignando un valor.
numeros_favoritos[2] = 0
print(numeros_favoritos)
# Imprime: [7, 6, 0, 21, 4]

# Las listan pueden tener distintos tipos de
# datos, por ejemplo la siguiente lista de string.
colores_favoritos = ["Rojo", "Negro", "Blanco", "Naranja", "Rosa"]
print(colores_favoritos)
# Imprime: ['Rojo', 'Negro', 'Blanco', 'Naranja', 'Rosa']

# Para acceder al primer elemento se utiliza el indice 0
print(colores_favoritos[0])
# Imprime: Rojo
# Al ultimo se accede con -1
# Cuando se utilizan valores negativos en los indices
# se empieza a contar des de el ultimo elemento
print(colores_favoritos[-1])
# Imprime: Rosa
# Acceder al penúltimo elemento
print(colores_favoritos[-2])
# Imprime: Naranja

# Sub listas, obtiene una lista de un rango
# de indices separados por dos puntos.
# Por ejemplo: desde la posición 1 a la 3
print(colores_favoritos[1:3])
# Imprime: ['Negro', 'Blanco']
# De posición 3 a la última
print(colores_favoritos[3:])
# Imprime: ['Naranja', 'Rosa'
# De la primera posición a la 2
print(colores_favoritos[:2])
# Imprime: ['Rojo', 'Negro']

# Agregar valores al final de la lista
# utilizando la función append()
colores_favoritos.append("Azul")
print(colores_favoritos)
# Imprime: ['Rojo', 'Negro', 'Blanco', 'Naranja', 'Rosa', 'Azul']

# Insertar un elemento en una posición especifica de la lista
# con la función insert()
colores_favoritos.insert(-1, "Amarillo")
print(colores_favoritos)
# Imprime: ['Rojo', 'Negro', 'Blanco', 'Naranja', 'Rosa', 'Amarillo', 'Azul']

# Eliminar el último elemento de la lista
# con la función pop()
colores_favoritos.pop()
print(colores_favoritos)
# Imprime: ['Rojo', 'Negro', 'Blanco', 'Naranja', 'Rosa', 'Amarillo']

# Eliminar una posición especifica con la función
# pop() indicando el indice.
colores_favoritos.pop(3)
print(colores_favoritos)
# Imprime: ['Rojo', 'Negro', 'Blanco', 'Rosa', 'Amarillo']

# Quitar un elemente con el valor con la función
# remove() indicando el valor.
# Nota: elimina solo el primer valor encontrado.
colores_favoritos.remove('Blanco')
print(colores_favoritos)
# Imprime: ['Rojo', 'Negro', 'Rosa', 'Amarillo']

# Podemos conocer cuantos elementos contiene
# una lista con la función len()
print(len(colores_favoritos))
# Imprime: 4

# Index nos ayuda a conocer la posición
# de un elemento conociendo su valor.
# Por ejemplo para conocer la posición
# del valor 'Amarillo'.
print(colores_favoritos.index('Amarillo'))
# Imprime: 3

# Listas anidadas, python permite tener
# listas dentro de listas.
# Por ejemplo creamos una con las listas
# creadas anteriormente.
lista_combinada = [numeros_favoritos, colores_favoritos]
print(lista_combinada)
# Imprime: [[7, 6, 0, 21, 4], ['Rojo', 'Negro', 'Rosa', 'Amarillo']]
# Para poder acceder al valor 'Rosa' primero tenemos que ubicar su indice,
# el cual es el tercer valor de la segunda lista. Se hace de esta forma.
print(lista_combinada[1][2])
# Imprime: Rosa
