class Auto:

    def __init__(self, marca="Toyota", color="Blanco", gasolina=0):
        self.marca = marca
        self.color = color
        self.gasolina = gasolina
        print(f"Constructor llamado: {self.marca}, {self.color}, {self.gasolina}L")
    
    def mostrar(self):
        return f"Auto: {self.marca} | Color: {self.color} | Gasolina: {self.gasolina}L"
    

    def __iadd__(self, valor):

        if isinstance(valor, int):
            self.gasolina += valor
            print(f"++ aplicado: +{valor}L de gasolina")
        return self


    def __pos__(self):
        self.gasolina += 5
        print("++ aplicado: +5L de gasolina")
        return self


    def __add__(self, nuevo_color):

        if isinstance(nuevo_color, str):
            print(f"Cambiando color de {self.color} a {nuevo_color}")
            self.color = nuevo_color
        return self
    

    def __sub__(self, otro_auto):

        if isinstance(otro_auto, Auto):
            total = self.gasolina + otro_auto.gasolina
            print(f"Total gasolina: {self.gasolina}L + {otro_auto.gasolina}L = {total}L")
            return total
        return 0



print("--- a) y b) CONSTRUCTORES SOBRECARGADOS ---")

auto1 = Auto()
print(auto1.mostrar())

print()

auto2 = Auto("Honda", "Azul", 20)
print(auto2.mostrar())

print("\n--- c) SOBRECARGA ++ ---")
print("Antes:", auto1.mostrar())
+auto1  
print("Despues:", auto1.mostrar())


auto1 += 5
print("Despues de +=5:", auto1.mostrar())

print("\n--- d) SOBRECARGA + PARA CAMBIAR COLOR ---")
print("Antes:", auto2.mostrar())
auto2 + "Rojo" 
print("Despues:", auto2.mostrar())

print("\n--- e) SOBRECARGA - PARA SUMAR GASOLINA ---")
auto1.gasolina = 30
auto2.gasolina = 20
print(f"Auto1: {auto1.mostrar()}")
print(f"Auto2: {auto2.mostrar()}")
total = auto1 - auto2
print(f"Resultado de auto1 - auto2: {total}L")