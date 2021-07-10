# Los diccionarios en python al igual que
# las listas pueden contener varios datos,
# cada dato en el diccionario es accesible
# a través de una llave.
persona = {"Nombre": "Victor Manuel",
           "Apellido": "Contreras",
           "Estatura": 1.81}
print(type(persona))
# Imprime: <class 'dict'>
print(persona)
# Imprime: {'Nombre': 'Victor Manuel', 'Apellido': 'Contreras', 'Estatura': 1.81}

# Se accede a los datos con su llave
# indicada como string entre corchetes.
print(persona["Nombre"])
# Imprime: Victor Manuel

# Cambiarle el valor "Nombre" al diccionario.
persona["Nombre"] = "Sergio"
print(persona)
# Imprime: {'Nombre': 'Sergio', 'Apellido': 'Contreras', 'Estatura': 1.81}

# Se pueden asignar nuevos valores al diccionario.
persona["Color_Favorito"] = "Rojo"
print(persona)
# Imprime: {'Nombre': 'Sergio', 'Apellido': 'Contreras', 'Estatura': 1.81, 'Color_Favorito': 'Rojo'}

# del() se utiliza para eliminar valores por su llave
del(persona["Color_Favorito"])
print(persona)
# Imprime: {'Nombre': 'Victor Manuel', 'Apellido': 'Contreras', 'Estatura': 1.81}

# Los diccionarios pueden ser tan complejos como se requieran.
# Al ejemplo anterior le agregaremos una lista con otros
# diccionarios dentro
lenguaje_1 = {"Nombre": "GO", "Habilidad": "Alta"}
lenguaje_2 = {"Nombre": "PHP", "Habilidad": "Media"}
lenguaje_3 = {"Nombre": "JavaScript", "Habilidad": "Media"}
lenguaje_4 = {"Nombre": "Python", "Habilidad": "Baja"}
# Crear lista con los lenguajes
lenguajes = [lenguaje_1, lenguaje_2, lenguaje_3, lenguaje_4]
print(lenguajes)
# Imprime: [{'Nombre': 'GO', 'Habilidad': 'Alta'}, {'Nombre': 'PHP', 'Habilidad': 'Media'}, {'Nombre': 'JavaScript', 'Habilidad': 'Media'}, {'Nombre': 'Python', 'Habilidad': 'Baja'}]
# Añadir la lista de lenguajes al diccionario
persona["Lenguajes"] = lenguajes
print(persona)
# Imprime: {'Nombre': 'Sergio', 'Apellido': 'Contreras', 'Estatura': 1.81, 'Lenguajes': [{'Nombre': 'GO', 'Habilidad': 'Alta'}, {'Nombre': 'PHP', 'Habilidad': 'Media'}, {'Nombre': 'JavaScript', 'Habilidad': 'Media'}, {'Nombre': 'Python', 'Habilidad': 'Baja'}]}

# Se puede convinar la sintaxis de la lista con
# los diccionaros para acceder a los datos
# tan profundos como sea necesario.
# Por ejemplo acceder al nombre del tercer lenguaje
print(persona["Lenguajes"][2]["Nombre"])
# Imprime: JavaScript
