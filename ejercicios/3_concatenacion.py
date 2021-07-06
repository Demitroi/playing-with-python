# En python como en otros lenguajes la concatenación de texto se hace con el símbolo +
print("Hola!" + " " + "esta" + " " + "es" + " " + "una" + " " + "concatenación")

# Otra forma de concatenar es usar el formateo de string,
# se le pone un punto. al final de la cadena y se llama a la función format
# los parámetros reemplazaran el texto en el orden que se indique.
print("Me gusta {} con {} antes de {}".format("ver el amanecer", "un buen café", "trabajar"))

# EL orden de los parametros con formateo se puede cambiar utilizando el indice del parametro
# recuerden que los indices comienzan con 0.
print("Me gusta {2} con {1} antes de {0}".format("ver el amanecer", "un buen café", "trabajar"))
