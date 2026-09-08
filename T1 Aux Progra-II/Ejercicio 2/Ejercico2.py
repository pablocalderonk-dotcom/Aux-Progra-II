class Computadora:
    def __init__(self, marca: str, procesador: str, ram: int, almacenamiento: int):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento

    def verificar_ram(self, x: int) -> bool:
        return self.ram == x

    def mostrar(self):
        print(f"Computadora: {self.marca} | Procesador: {self.procesador} | RAM: {self.ram} GB | Almacenamiento: {self.almacenamiento} GB")

if __name__ == "__main__":
    comp1 = Computadora("HP", "Intel Core i5", 16, 512)
    comp2 = Computadora(marca="Asus", procesador="AMD Ryzen 7", ram=32, almacenamiento=1024)

    comp1.mostrar()
    comp2.mostrar()

    X = 16
    print(f"¿La RAM de comp1 es igual a {X}?: {comp1.verificar_ram(X)}")

    if comp1.almacenamiento > comp2.almacenamiento:
        comp1.mostrar()
    else:
        comp2.mostrar()