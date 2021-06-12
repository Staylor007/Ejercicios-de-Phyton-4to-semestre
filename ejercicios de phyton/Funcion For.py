# Estructuras de control de phyton - FOR
# for range(v) - range(vi,vf) - range(vi,vf.inc)
palabras = input("Ingrese una frase: ")
for lista in range(len(palabras)):
    print(lista,'=',palabras[lista])

# for in cadena - in(tupla) - in(lista)
contVoc = 0
for letra in palabras:
    if letra in ("a","e","i","o","u","A","E","I","O","U"):
        if letra in ["A","E","I","O","U"]:
            continue
        else:
            contVoc = contVoc + 1
print('La cantidad vocales es de : {}'.format(contVoc))

# Comprehension - [var for var in datos condicion]
[letra for letra in['a','e','i','o','u']if letra not in('a','i','o')]

