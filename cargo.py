class Cargo:
    secuencia = 0
    def __init__(self,des="Sin cargo"):
        Cargo.secuencia = Cargo.secuencia+1
        self.codigo = Cargo.secuencia
        self.descripcion = des

cargo1 = Cargo()
print(cargo1.codigo,cargo1.descripcion)
cargo2 = Cargo()
cargo2.descripcion = "Gerente"
print(cargo2.codigo,cargo2.descripcion)
cargo3 = Cargo("Administrador")
print(cargo3.codigo,cargo3.descripcion)
# print(Cargo.secuencia)
# print(cargo1.secuencia)
# print(cargo2.secuencia)
# print(cargo3.secuencia)