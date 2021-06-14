#clase del 14 de junio
class For:
    def __init__(self):
        pass

    #el for es el ciclo repetitivo de incremento o decremento se ejecuta
    def usoFor(self): #metodo
        nombre= "Stalin"
        datos = ["Stalin",19,True]
        numeros = (4,3,2,6,8)
        alumno = {'nombre': 'Stalin', 'edad': 19, 'fac': 'faci'}
        listaNotas = [(30,40),(20,40),(50,40)] #es una coleccion de matriz
        listaCompañeros = [{"nombre":"Juan","final":90},{"nombre":"Maria","final":80},{"nombre":"Nohelia","final":90}]

        #! Maneras de mandar a imprimir cada elemento segun la ubicacion con el range.
        # for i in range(5):
        #     print("i={}".format(i))
        # for i in range(2,10):
        #     print("i={}".format(i))
        # for i in range(4,10,2):
        #     print("i={}".format(i),end= " ")
        # for i in range(12,3,-3):
        #     print("i={}".format(i),end= " ")

        # longitud = len(datos)
        # print(datos[0])
        # print(datos[1])
        # print(datos[2])

        #! La manera de hacer con el while.
        # j=0
        # while j < longitud:
        #     print("while",datos[j])
        #     j=j+1

        # for i in range (longitud -1,-1,-1):
        #     print("for",datos[i], end="  ")

        # for i, dato in enumerate(datos):
        #     print("for",i,dato)

        #! dato tomar cada elemento de la coleccion numeros(cadena,lista,tupla)
        # for dato in numeros:
        #     print(dato)
        # for dato in "Hola":
        #     print(dato)

        # print("\nDiccionario de notas")
        # for clave,valor in docente.items():
        #     print(clave,":",valor,end="  -  ")

        print("\nListado de notas")
        for compañeros in listaCompañeros:
            for clave,valor in compañeros.items():
                print(clave,":",valor,end="     ")

ejercicio = For()
ejercicio.usoFor()