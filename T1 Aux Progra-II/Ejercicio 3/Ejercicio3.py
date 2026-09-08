class Celular:
    def __init__(self, marca: str, modelo: str, memoria: int, bateria: int):
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria
        self.bateria = bateria

    def verificar_bateria(self, p: int) -> bool:
        return self.bateria < p

    def mostrar(self):
        print(f"Celular: {self.marca} {self.modelo} | Memoria: {self.memoria} GB | Batería: {self.bateria}%")

if __name__ == "__main__":
    cel1 = Celular("Samsung", "Galaxy S23", 256, 15)
    cel2 = Celular(marca="Xiaomi", modelo="Redmi Note 12", memoria=128, bateria=85)

    cel1.mostrar()
    cel2.mostrar()

    P = 20
    print(f"¿La batería de cel1 es menor al {P}%?: {cel1.verificar_bateria(P)}")

    if cel1.memoria > cel2.memoria:
        cel1.mostrar()
    else:
        cel2.mostrar()