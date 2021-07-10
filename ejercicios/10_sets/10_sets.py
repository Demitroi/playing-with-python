# Los set son una colección desordenada
# ya que los datos no se muestran en el
# orden que se ingresan, no permite
# almacenar datos duplicados y tampoco permite
# los tipos de colección listas, tuplas y diccionarios.

# Crear un conjunto vacío con la función set()
conjunto_vacio = set()
print(type(conjunto_vacio))
# Imprime: <class 'set'>
print(conjunto_vacio)
# Imprime: set()

# Inicializar un cojunto con datos utilizando las llaves
# con los valores separados por comas dentro.
conjunto = {1, "A", 2.0}
print(conjunto)
# Imprime: {1, 2.0, 'A'}

# Agregar mas datos con la función add()
conjunto.add("K")
print(conjunto)
# Recordemos que los conjuntos no respetan el orden
# En ocasiones lo imprime así: {1, 2.0, 'K', 'A'}
# Y en otras así: {1, 2.0, 'A', 'K'}

# Ingresamos mas datos para probar
conjunto.add(3.14)
conjunto.add(False)
conjunto.add(34)
conjunto.add(48)
conjunto.add("F")
print(conjunto)
# En ocasiones lo imprime así: {False, 1, 2.0, 3.14, 34, 'K', 'A', 48, 'F'}
# Y en otras así: {False, 1, 2.0, 3.14, 34, 'K', 'F', 48, 'A'}

# Comprobar que un elemento existe utilizando la palabra
# in de la siguiente manera.
existe = 'F' in conjunto
print(existe)
# Imprime: True

# Obtener una lista a partir de un set
lista = list(conjunto)
print(type(lista))
# Imptime: <class 'list'>
print(lista)
# Imprime: [False, 1, 2.0, 3.14, 34, 'F', 'A', 48, 'K']

# Agregar al numero 34 tanto a la lista como al set
# para ver las diferencias de su comportamiento.
lista.append(34)
conjunto.add(34)
print(lista)
# Imprime: [False, 1, 2.0, 3.14, 34, 'F', 48, 'A', 'K', 34]
print(conjunto)
# Imprime: {False, 1, 2.0, 3.14, 34, 'F', 48, 'A', 'K'}
# La lista duplica el numero 34 y el set no

# Eliminar datos de un set con la función discard()
# pasando como parametro el valor.
conjunto.discard("F")
print(conjunto)
# Imprime: {False, 1, 2.0, 3.14, 34, 'K', 48, 'A'}

# Eliminar todos los datos del conjunto
# con la función clear()
conjunto.clear()
print(conjunto)
# Imprime: set()
