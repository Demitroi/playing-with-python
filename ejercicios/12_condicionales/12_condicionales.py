# Las condicionales permiten controlar el flujo
# de la ejecución, estas se utilizan con la palabra
# reservada if y evalúan un valor booleano.

# Ejemplo de if con condición verdadera
if True:
    print("Condición verdadera")
    # Imprime: Condición verdadera

# Ejemplo de condición falsa
if False:
    print("Esto nunca se va a imprimir")

# Se pueden utilizar operadores en el if
numero_1 = 18
numero_2 = 19
suma = numero_1 + numero_2
if suma == 37:
    print("La suma es el valor esperado")
    # Imprime: La suma es el valor esperado

# else permite definir un bloque de código
# que se ejecutará cuando la condición no se cumpla.
if suma == 40:
    print("La suma es el valor esperado")
else:
    print("La suma no es el valor esperado")
    # Imprime: La suma no es el valor esperado

# Es permitido incluir condiciones if dentro de if o else,
# a esto se le denomina condiciones anidadas.
if suma < 50:
    if suma < 25:
        print("La suma es menor a 25")
    else:
        print("La suma esta entre 25 y 49")
        # Imprime: La suma esta entre 25 y 49
else:
    if suma > 75:
        print("La suma es mayor a 75")
    else:
        print("La suma esta entre 50 y 75")

# Es muy común que se complique leer los if anidados,
# con elif se puede tener otra condición si la primera
# no se cumple.
if suma < 25:
    print("La suma es menor a 25")
elif suma < 50:
    print("La suma esta entre 25 y 49")
    # Imprime: La suma esta entre 25 y 49
elif suma < 75:
    print("La suma esta entre 50 y 75")
else:
    print("La suma es mayor a 75")
