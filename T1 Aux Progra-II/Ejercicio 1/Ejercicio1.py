class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int, kilometraje: int, color: str = "Blanco"):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.color = color

    def mostrar_kilometraje(self):
        metros = self.kilometraje * 1000
        print(f"Kilometraje: {self.kilometraje} km ({metros:,} metros)")

    def cambiar_color(self, nuevo_color: str):
        self.color = nuevo_color

    def mostrar_datos(self):
        print(f"Vehículo: {self.marca} {self.modelo} ({self.anio}) | Color: {self.color}")
        self.mostrar_kilometraje()

# Programa Principal
if __name__ == "__main__":
    # c) Creación de dos autos
    auto1 = Vehiculo("Toyota", "Corolla", 2023, 12500, "Plata")
    auto2 = Vehiculo("Hyundai", "Tucson", 2024, 3400, "Negro")

    # Cambio de color
    auto1.cambiar_color("Rojo Cereza")
    auto2.cambiar_color("Azul Eléctrico")

    # Mostrar resultados
    print("--- Auto 1 ---")
    auto1.mostrar_datos()

    print("\n--- Auto 2 ---")
    auto2.mostrar_datos()