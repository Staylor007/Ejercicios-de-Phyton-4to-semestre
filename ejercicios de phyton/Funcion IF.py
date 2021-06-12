#Estructuras de control de phyton - IF
x = int(input("Ingresa un numero entero: "))
if x < 0:
    x = 0
    print('Negativo cambiando a cero')
elif x == 0:
    print('Cero')
elif x == 1:
    print('Uno')
else:
    print('Ninguna opcion')
    print("OK")if type(x) == int else print("-")
