# En python las variables se declaran con un valor inicial
# No es necesario indicar el tipo de variable ya que
# es un lenguaje de tipado dinamico.
nombre_bebida = "El cafe"
print("Mi bebida favorita es " + nombre_bebida)
# Imprime: Mi bebida favorita es El cafe

# Las variables pueden cambiar en tiempos de ejecución.
nombre_bebida = "El te"
print("Mi bebida favorita no es " + nombre_bebida)
# Imprime: Mi bebida favorita no es El te

# Se puede asignar el mismo valor a diferentes variables
# en un solo statement.
color_1 = color_2 = "Rojo"
print("Mis colores favoritos son el {} y el {}".format(color_1, color_2))
# Imprime: Mis colores favoritos son el Rojo y el Rojo

# Otra forma es asignar diferentes valores a cada variable en el orden que
# están escritas, si el número de valores no coincide con el de variables
# python arrojara una excepción.
pasa_tiempo_1, pasa_tiempo_2, pasa_tiempo_3 = "Estudiar", "Jugar", "Correr"
# Nota: Se utiliza la f al principio del texto para indicar que es un formato.
print(f"Mis pasatiempos preferidos son {pasa_tiempo_1}, {pasa_tiempo_2} y {pasa_tiempo_3}")
# Imprime: Mis pasatiempos preferidos son Estudiar, Jugar y Correr
