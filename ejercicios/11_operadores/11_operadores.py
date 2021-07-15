# Los operadores son símbolos y palabras reservadas
# que permiten hacen operaciones aritméticas, de comparación,
# lógicas, de identidad, de membresía, operadores a nivel
# de bits y de asignación.

# Aritméticos, hacen operaciones matemáticas con números
# + Suma números
print(5 + 3)
# Imprime: 8
# - Resta números.
print(5 - 3)
# Imprime: 2
# * Multiplica números.
print(8 * 8)
# Imprime: 64
# / Divide el numero de la izquierda en el de la derecha, siempre retorna un tipo flotante.
print(13 / 5)
# Imprime: 2.6
# % Retorna el residuo de una división.
print(13 % 5)
# Imprime: 3
# // Retorna el numero entero de la división.
print(13 // 5)
# Imprime: 2
# ** Exponente del numero derecho.
print(2 ** 8)
# Imprime: 256

# Comparación, son usados para comparar valores.
# Retornan True o False
# > Mayor que, Retorna True si el valor izquierdo es Mayor que el derecho.
print(5 > 4)
# Imprime: True
print(4 > 5)
# Imprime: False
# < Menor que, Retorna True si el valor derecho es Mayor que el izquierda.
print(5 < 4)
# Imprime: False
print(4 < 5)
# Imprime: True
# == Igual que, Retorna True si los valores a comparar son iguales.
print(10 == 10)
# Imprime: True
print(10 == 8)
# Imprime: False
# != Diferente que, Retorna True si los valores a comparar son diferentes.
print(10 != 10)
# Imprime: False
print(10 != 8)
# Imprime: True
# >= Mayor o igual que, Retorna True si el valor izquierdo es Mayor o igual que el derecho.
print(7 >= 6)
# Imprime: True
print(7 >= 7)
# Imprime: True
print(7 >= 8)
# Imprime: False
# <= Menor o igual que, Retorna True si el valor izquierdo es Menor o igual que el derecho.
print(7 <= 6)
# Imprime: False
print(7 <= 7)
# Imprime: True
print(7 <= 8)
# Imprime: True

# Lógicos, hacen operaciones lógicas con valores booleanos.
# and, Retorna True si ambos son True.
print(True and True)
# Imprime: True
print(True and False)
# Imprime: False
print(False and False)
# Imprime: False
# or, Retorna True si cualquiera de los dos es True.
print(True or True)
# Imprime: True
print(True or False)
# Imprime: True
print(False and False)
# Imprime: False
# not, Cambia el valor de True a False y viceversa.
print(not True)
# Imprime: False
print(not False)
# Imprime: True

# Identidad, determinan si dos valores están alojados en
# la misma parte de la memoria, si dos variables son
# iguales no significa que sean idénticas.
numero_1 = 5
numero_2 = 5
# is, Retorna True si los operandos son idénticos.
print(numero_1 is numero_1)
# Imprime: True
print(numero_1 is numero_2)
# Imprime: True
# is not, Retorna True si los operandos no son idénticos.
print(numero_1 is not numero_1)
# Imprime: False
print(numero_1 is not numero_2)
# Imprime: False
lista_1 = [1, 2, 3]
lista_2 = [1, 2, 3]
# Comparar la misma lista.
print(lista_1 is lista_1)
# Imprime: True
# Comparar diferentes listas.
print(lista_1 is lista_2)
# Imprime: False

# Membresía, validan sí un valor o variable se encuentra dentro
# de una secuencia, (string, lista, tupla, set y diccionario).
# Retorna un valor Booleano.
texto = "Buenos días mundo"
lenguajes = ["Python", "GO", "JavaScript", "PHP", "C#", "Java"]
# in, Valida sí un valor se encuentra en una secuencia.
print("mundo" in texto)
# Imprime: True
print("noches" in texto)
# Imprime: False
# not in, Valida sí un valor no se encuentra en una secuencia.
print("Rust" not in lenguajes)
# Imprime: True
print("GO" not in lenguajes)
# Imprime: False

# Operaciones a nivel de bits, realizan operaciones bit a bit.
# Tomando como ejemplo estos dos números en su representación binaria.
x, y = 10, 8
print(bin(x))
# Imprime: 0b1010
print(bin(y))
# Imprime: 0b1000
# &, Realiza una operación AND sobre los bits de misma posición.
print(bin(x & y))
# Imprime: 0b1000
# |, Realiza una operación OR sobre los bits de misma posición.
print(bin(x | y))
# Imprime: 0b1010
# ~. Realiza una operación NOT, cambia el signo y los valores de los bits.
print(bin(~ x))
# Imprime: -0b1011
# ^, Realiza una operación XOR sobre los bits de misma posición, cuando no son pares es uno.
print(bin(x ^ y))
# Imprime: 0b10
# >>, Cambio de bits a la derecha. recorre los bits del valor de la izquierda hacia la derecha con el valor de la derecha.
print(bin(x >> 2))
# Imprime: 0b10
# >>, Cambio de bits a la izquierda. recorre los bits del valor de la izquierda hacia la izquierda con el valor de la derecha.
print(bin(x << 2))
# Imprime: 0b101000

# Asignación, asigna valores a las variables.
# La forma mas simple de estos es asignar una simple
# variable con un valor.
# a = 5
# Sin embargo, existen más operadores de asignación,
# que ayudan a acortar código.
# +=, equivale a x = x + n acortado a x += n
# -=, equivale a x = x - n acortado a x -= n
# *=, equivale a x = x * n acortado a x *= n
# /=, equivale a x = x / n acortado a x /= n
# %=, equivale a x = x % n acortado a x %= n
# //=, equivale a x = x // n acortado a x //= n
# **=, equivale a x = x ** n acortado a x **= n
# &=, equivale a x = x & n acortado a x &= n
# |=, equivale a x = x | n acortado a x |= n
# ^=, equivale a x = x ^ n acortado a x ^= n
# >>=, equivale a x = x >> n acortado a x >>= n
# <<=, equivale a x = x << n acortado a x <<= n
