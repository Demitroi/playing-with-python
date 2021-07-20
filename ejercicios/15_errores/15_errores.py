# Ningún programa está exento de errores y
# en python existen mecanismos para lidiar con ellos.
# Las excepciones ocurridas dentro de los bloques de
# código try, serán procesadas en el bloque except.

# Por ejemplo si se intenta concatenar texto con un número.
# Esto arroja una excepción por lo que se ejecuta el bloque de except.
try:
    texto = "Numero " + 25
    print(texto)
except:
    print("Ha ocurrido un error")
    # Imprime: Ha ocurrido un error

# Sí no ocurre ningún error no se ejecuta except.
try:
    texto = "Numero " + "25"
    print(texto)
    # Imprime: Numero 25
except:
    print("Ha ocurrido un error")

# En except se puede indicar el tipo de error esperado.
try:
    resultado = 16 / 0
    print(resultado)
except ZeroDivisionError:
    print("No es posible dividir sobre cero")
    # Imprime: No es posible dividir sobre cero
except:
    print("Alguna otra excepción")

# El bloque finally se ejecuta siempre independientemente
# si ocurrió error o no.
try:
    resultado = 16 / 8
    print(resultado)
    # Imprime: 2.0
except:
    print("Tenemos problemas")
finally:
    print("Hemos terminado")
    # Imprime: Hemos terminado

# Los errores se pueden guardar en variables y 
# obtener mas información de ellos.
try:
    resultado = 16 / 0
    print(resultado)
except Exception as err:
    print(err)
    # Imprime: division by zero
    print(type(err))
    # Imprime: <class 'ZeroDivisionError'>

# Lanzar errores manualmente, se utiliza la palabra
# reservada raise seguido del error en cuestión.
try:
    raise TypeError
except Exception as err:
    print(type(err))
    # Imprime: <class 'TypeError'>
