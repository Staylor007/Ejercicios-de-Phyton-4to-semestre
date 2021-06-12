#Estructuras de control de phyton - WHILE
'''while validation'''
vocal = input("Ingrese vocal: ")
while vocal not in ('a','e','i','o','u'):
    if vocal == '-':
        break
    vocal = input("Vocal: ")
print('Su vocal o punto es: {}'.format(vocal))