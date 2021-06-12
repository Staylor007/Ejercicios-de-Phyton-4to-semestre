# num = 20
# if type(num) == int:
#     print("Resultado: ", num*6)
# else:
#     print("El numero no es numerico")

# def mensaje(mensj):
#     print(mensj)

# mensaje("Mi primer Programa")
# mensaje("Mi segundo Programa")


#*******************************************************************************************

# class Sintaxis:
#     def usoVariables(self):
#         diaDelMes, año = 11, 2021
#         print(diaDelMes,año)

# ejerci1 = Sintaxis()
# ejerci1.usoVariables()


#********************************************************************************************

class Persona:
    instancia = 0 #variable de clase (opcional)
    #_init_Metodo constructor que se ejecutaq cuando se instancia la clase cuyo objetivo es crear
    # e inicializar los atributos de la clase. Self es un objeto que representa la clase creada.
    def __init__(self,apunte="Muchas gracias"):
        self.expresion = apunte
        #Sintaxis.instancia = Sintaxis.instancia+1

    def usoVariable(self):
        edad, peso = 19, 63.5
        nombre = 'Stalin Espinoza'
        TipoSexo = 'M'
        civil = True
        #tuplas = () son colecciones de datos de cualquier tipo inmutable
        usuario = ('sespinozac', '2021' ,'stalinec2002@gmail.com', True)
        #usuario[3] = "Milagro"
        # listas = [] colecciones mutables
        materias = []
        materias = ['POO','Base de datos','Sistemas Operativos']
        materias[1] = "Python"
        materias.append("Go")
        #diccionario ={} colcecciones de objetos clave:valor tipo json
        alumno = {}
        alumno = {'Nombre':'Stalin','Edad':19,'Facultad': 'Faci'}
         #presentacion con format
        print("""Mi nombre es {}, tengo {} años""".format(nombre,edad))
        print(usuario,materias,alumno)

        usuario = ('sespinozac','2021','stalinec2002@gmail.com')
        #usuario[3] = "Milagro"
        # listas = [] colecciones multiples
        materias = []
        materias = ['POO','Base de datos','Sistemas Operativos']
        materias[1] = "Python"
        materias.append("Go")
        #diccionario ={} colcecciones de objetos clave:valor tipo json
        alumno = {}
        alumno = {'Nombre':'Stalin','Edad':19,'Facultad': 'Faci'}
         #Imprimir
        print("""Mi nombre es {}, tengo {} años""".format(nombre,edad))
        print(usuario,materias,alumno)
        print(nombre,edad)

estudiante = Persona() #se crea un objeto que es una instancia de la clase
estudiante.usoVariable()
print(estudiante.expresion)