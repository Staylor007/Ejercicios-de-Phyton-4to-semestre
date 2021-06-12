class Cifra:
    contador = 0 #variable de clase (opcional)
    #__init__ Método constructor que se ejecuta al momento de instanciar la clase que tiene como ya que su
    # objetivo es crear e inicializar los atributos de la clase.
    # Self es un objeto que representa a la clase que se crea.
    def __init__(self,can1 = 2, can2 = 6):
        self.cantidad1 = can1  # variable de instancia
        self.cantidad2 = can2
        #cantidad = can1 + can2
        self.cantidad3 = can1
        #variables de instancias

    def usoIF(self):
        # if / elif / else : perimiten que condicionan la ejecución de uno o varios bloques
        # de sentencias al momento dde cumplir con una o varias condiciones.
        if self.cantidad1 == self.cantidad2:
            print("cantidad1:{}, cantidad2:{}: Las cantidades son iguales".format(self.cantidad1,self.cantidad2))
        elif self.cantidad1 == self.cantidad3:
             print("valor1:{}, valor3:{}: Las cantidades son iguales".format(self.cantidad1,self.cantidad3))
        else:
            print("Las cantidades no son iguales")
# usar clase
# condición1 = Valor ()
# print(condición1.valor1)
# print(condición1.valor2)

cond2 = Cifra(20,20)
cond2.usoIF()
print(cond2.cantidad1)