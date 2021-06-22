from cargo import Cargo
class Empleados:
    secuencia = 0
    def __init__(self,nom,ced,sue,cargo):
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.cedula= ced
        self.sueldo = sue
        self.cargo=cargo
    def mostrar(self):
        print("*** codigo: {} *** nombre: {} *** cargo: {}--{}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion))

    def generarCodigo(self):
        Empleados.secuencia = Empleados.secuencia+1
        return Empleados.secuencia

cargo1 = Cargo("Secretaria")
emp1 = Empleados("Maria","0942",600,cargo1)
emp1.mostrar()