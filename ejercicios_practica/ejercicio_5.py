# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y calcule a sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))
sumatoria = 0  # Inicializo el contador en 0

# for ... in range(....)

# Imprimir el valor de la sumatoria

print("terminamos!")

maximo_numero = None
lista_numeros = []

while True:
    # Tomamos el valor de la consola
    print("Ingrese un número mayor o igual a cero")
    numero = int(input())

    # Verificamos si el número es negativo
    if numero < 0:
        print('Hasta acá llegamos!')
        break   # Salgo del bucle!

    # Verifico si el número ingresado es mayor al
    # máximo número ingresado hasta el momento
    if (maximo_numero is None) or (numero > maximo_numero):
        maximo_numero = numero

    lista_numeros.append(numero)

# Termino el bucle imprimo la lista de números:
print("Lista: ", lista_numeros)
# Imprimo el máximo número encontrado
print("Máximo número = ", maximo_numero)
# Imprimo el máximo número utilizando la función max de Python
print("Máximo número con Python = ", max(lista_numeros))
# Imprimo el índice del máximo número en la lista
print("Índice del máximo número en la lista = ",
        lista_numeros.index(maximo_numero))
# Imprimo cuantas veces se repite el máximo número en la lista
print("Cantidad del máximo número en la lista = ",
        lista_numeros.count(maximo_numero))

print("terminamos!")
