# Conversiones, no se pueden hacer operaciones
# entre tipos de datos distintos, por eso se deben
# de convertir.

# Hagamos una suma simple
numero_1 = 65
numero_2 = 94
suma = numero_1 + numero_2

# Antes de concatenarlo e imprimirlo se debe convertir
# a tipo string con la función str()
print("El resultado es: " + str(suma))
# Imprime: El resultado es: 159

# Ejemplos de conversiones de tipo float, bool a string
numero_decimal = str(56.45)
print(type(numero_decimal))
# Imprime: <class 'str'>
booleano = str(True)
print(type(booleano))
# Imprime: <class 'str'>

# float() se para convertir a tipo float
# Creamos dos variables utilizando la función para convertir
# Convertimos de int a float
cantidad = float(5)
# Convertimos de int a float
precio = float("24.95")
# Imprimir el tipo de cantidad y precio
print(type(cantidad), type(precio))
# Imprime: <class 'float'> <class 'float'>
# Hacer un calculo con las variables
resultado = cantidad * precio
print(resultado)
# Imprime: 124.75

# int() convierte a tipo enteros
# Cuando es tipo string y este no es un numero
# lanza una excepción
perritos = int("18")
# Los tipos float solo conservan su parte entera
gatitos = int(56.45)
print(type(perritos), type(gatitos))
# Imprime: <class 'int'> <class 'int'>
mascotas = perritos + gatitos
print(mascotas)
# Imprime: 74

# bool() converte a tipo bool
# bool(0) es False porque es cero
# bool("") es False porque es string vacío
# bool(":)") es True porque no está vacío
# bool(-3.14) es True porque es diferente de cero
print(bool(0), bool(""), bool(":)"), bool(-3.14))
# Imprime: False False True True

# Conversiones que no se pueden hacer
# Están comentadas para que no arroje excepción
# Texto que no es numero a int y float
# int("Hola")
# float("Mundo")
# Texto con numero flotante a int
# int("3.1416")
