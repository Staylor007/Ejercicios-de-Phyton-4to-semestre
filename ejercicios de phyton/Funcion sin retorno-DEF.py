# Estructuras de control de Phyton - DEF
'''Funciones sin retorno'''
def vocales(frase):
    for abc in frase:
        if abc in('a','e','i','o','u'):
            print(abc)

'''Llamada a funcion'''
frase = input('Ingrese una frase: ')
vocales(frase.lower())