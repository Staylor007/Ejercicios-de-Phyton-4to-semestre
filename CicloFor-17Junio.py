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
        
        listaNotas = [(30,40),[20,40,20],(50,40,20,10,5)]
        acum= 0
        long = 0
        for notas in listaNotas:
            #print (notas)
            parcial = 0
            print(notas,end= " ")
            for nota in notas:
                print(nota)
                long = long + 1
                acum = acum + nota
                parcial += nota
            promParcial = parcial/len(notas)
            print("Notas parciales={} Promedio Parcial = {}".format(parcial,promParcial))
        # Para hallar el promedio
        prom = acum/long
        print("*** El total de notas es de = {} **** #Notas = {}  *** El promedio es de = {} ***".format(acum,long,prom))
        
        print("*********************************************************************")
        
        listaCompañeros = [{"nombre":"Juan","final":90},{"nombre":"Maria","final":80},{"nombre":"Nohelia","final":90}]
        acum = 0
        cont=0
        for compañeros in listaCompañeros:
            print(compañeros)
            for clave,valor in compañeros.items():
                print(clave,":",valor,end=" ")
                if clave=="final":acum=acum+valor
            cont +=1
        print(acum/cont)
        
        print("********************************************************************")
        
        frase = "Hola como estas"
        vocales = []
        for vocal in frase:
            if vocal in('a','e','i','o','u'):
                vocales.append(vocal)
        print(vocales)
        
        print("********************************************************************")
        
        # Si quiero que solo me salga en una linea
        vocales = [vocal for vocal in frase if vocal in ('a','e','i','o','u')]
        print(vocales)

ejercicio = For()
ejercicio.usoFor()