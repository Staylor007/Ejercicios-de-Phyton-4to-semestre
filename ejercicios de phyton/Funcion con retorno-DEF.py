# Estructuras de control de Phyton - DEF
'''Funcion con retorno del valor'''
def calificacion(cal):
    suma = 0
    for n in cal:
        suma += n
    return suma / len(cal)

#llamada a funcion
listado = [9, 10, 7, 8, 10]
promedio = calificacion(listado)
print('Sus calificaciones son: {} y como resultado de su promedio obtuvo = {}'.format(listado, promedio))
