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
lista= []
numero=range(inicio,fin)
# for ... in range(....)
for numero in range(inicio, fin):
    sumatoria += numero
    lista.append(numero)  
# Imprimir el valor de la sumatoria
    print("el valor de la sumatoria es: ",sumatoria)
print('cantidad de numeros ingresados: ',len(lista)) #agregue cada numero a la lista y verifico con print la cantidad de numeros ingresados
print('los numeros ingresados son: ',lista) # imprimo los numeros ingresados con range
print("terminamos!")
