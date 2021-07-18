class Operaciones:
    def __init__(self,num1,num2):
        self.numero1 = num1
        self.numero2 = num2
    
    def suma(self):
        suma = self.numero1 + self.numero2
        return suma
    
    def resta(self):
        # if self.numero1 >= self.numero2:
        #     return self.numero1 - self.numero2
        # return 0
        return self.numero1 - self.numero2
    
    def multiplicacion(self):
        return self.numero1 * self.numero2
    
    def division(self):
        if self.numero2 != 0:  return self.numero1 / self.numero2
        return 0
    
    def divisionEntera(self):
        return self.numero1 / self.numero2
    
    def residuo(self):
        return self.numero1 % self.numero2
    
    def exponente(self):
        return self.numero1 / self.numero2
    
    def mostrar(self):
        print("Operando1={},Operando2={}".format(self.numero1,self.numero2))
    
# operacion = Operaciones(10,20)
# x = operacion.suma()
# print(operacion.suma())
# print(operacion.division())
# y = operacion.resta()
# z = x ** y
# print(z)
# operacion.mostrar()

print("Menu de operaciones Matematicas")
print("1) Suma\n2) Resta\n3) Multiplicacion\n4) Division\n5) Division entera\n6) Residuo\n7) Exponenete\n")
opc='0'

while opc !='8':
    opc = input("Elija opcion[1...8]: ")
    if opc == '1':
        num1 = int(input("Ingrese Numero1: "))
        num2 = int(input("Ingrese Numero2: "))
        ope = Operaciones(num1,num2)
        print(ope.suma())
    elif opc == '2':
        num1 = int(input("Ingrese Numero1: "))
        num2 = int(input("Ingrese Numero2: "))
        ope = Operaciones(num1,num2)
        print(ope.resta())
    elif opc == '3':
        num1 = int(input("Ingrese Numero1: "))
        num2 = int(input("Ingrese Numero2: "))
        ope = Operaciones(num1,num2)
        print(ope.multiplicacion())
    elif opc == '4':
        num1 = int(input("Ingrese Numero1: "))
        num2 = int(input("Ingrese Numero2: "))
        ope = Operaciones(num1,num2)
        print(ope.division())
    elif opc == '5':
        num1 = int(input("Ingrese Numero1: "))
        num2 = int(input("Ingrese Numero2: "))
        ope = Operaciones(num1,num2)
        print(ope.divisionEntera())
    elif opc == '6':
        num1 = int(input("Ingrese Numero1: "))
        num2 = int(input("Ingrese Numero2: "))
        ope = Operaciones(num1,num2)
        print(ope.residuo())
    elif opc == '7':
        num1 = int(input("Ingrese Numero1: "))
        num2 = int(input("Ingrese Numero2: "))
        ope = Operaciones(num1,num2)
        print(ope.exponente())
    elif opc == '8':
        break

print("Gracias por su visita...")
