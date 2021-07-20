# El ciclo while permite ejecutar un bloque de código,
# siempre y cuando una condición sea verdadera.

# Este ejemplo utiliza un contador para imprimir
# números desde el 0 al 9
contador = 0
while contador <= 9:
    print("Contador", contador)
    # Imprime Contador del 0 al 9
    contador += 1

# break permite romper el ciclo sin completarlo
contador = 0
while contador <= 9:
    print("Contador", contador)
    # Imprime Contador del 0 al 5
    if contador == 5:
        break
    contador += 1

# continue permite saltarse a la siguiente iteración
contador = 0
while contador <= 9:
    contador += 1
    # Sí no es par no imprimirlo
    if contador % 2 != 0:
        continue
    print("Contador", contador)
    # Imprime Contador números pares del 2 al 10
