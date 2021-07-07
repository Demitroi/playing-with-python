# En python existen distintos tipos de datos
# Se explicarán algunos a continuación

# Cadenas de caracteres o string
# Están represendatos por la clase str
# Declaramos una variable de tipo string
mensaje = "Este es una frase inspiradora"
print(type(mensaje))
# Imprime: <class 'str'>

# No hay variables tipo de carácter
# todo texto es tratado como string
letra = 'F'
print(type(letra))
# Imprime: <class 'str'>

# Numéricos, enteros o int
# Pertenecen a la clase int
# Su limite es tan grande como la memoria
# lo pueda soportar
numero = 21
print(type(numero))
# Imprime: <class 'int'>

# Decimales, flotantes o float
# Pertenecen a la clase float
# Siempre llevan un punto aunque tenga cero decimales
salario = 17750.28
print(type(salario))
# Imprime: <class 'float'>

# Complejos o complex
# Pertenecen a la clase complex
# Recordad que los números complejos llevan
# una parte real y una parte imaginaria
complejo = 1 + 2j
print(type(complejo))
# Imprime: <class 'complex'>

# El numero complejo esta compuesto por dos
# Números flotantes y se puede acceder a ellos
# de la siguiente forma:
# Al flotante real con .real
# Y al flotante imaginario con .imag
print(type(complejo.real))
print(type(complejo.imag))
# Imprime: <class 'float'>
# <class 'float'>

# Booleanos o Boolean
# Solo pueden tener dos valores
# True o False
# Pertenecen a la clase bool
felicidad = True
tristesa = False
print(type(felicidad))
print(type(tristesa))
# Imprime: <class 'bool'>
# <class 'bool'>

# Para finalizar hagamos algo mas complejo
# Hagamos una suma, comparación y asignación
# de una variable en una sola linea
es_igual = 6 + 7 == 13
print(es_igual)
print(type(es_igual))
# Imprime: True
# <class 'bool'>
