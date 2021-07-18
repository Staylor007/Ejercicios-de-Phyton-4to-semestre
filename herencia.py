class Persona:
    _siguiente = 0
    def __init__(self,nombre = "Invitado",activo = True):
        #Persona._siguiente = Persona._siguiente + 1
        #self.__codigo = Persona._siguiente
        #self.__nombre = nombre
        self.__codigo = self.siguiente()
        self.__nombre = self.__nombreMayuscula(nombre)
        self.activo = activo
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,cod):
        self.__codigo = cod
        
    def siguiente(self):
        Persona._siguiente = Persona._siguiente + 1
        return Persona._siguiente
    
    def __nombreMayuscula(self,nomb):
        return nomb.upper()
    
    def mostrar_datos(self):
        return "Codigo: {} - Nombre: {} - Activo: {}".format(self)
    
per1 = Persona()
print(per1.nombre)
per2 = Persona("Stalin",False)
print(per2.nombre,per2.activo)