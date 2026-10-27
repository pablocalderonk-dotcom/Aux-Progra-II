class Pantalla:
    def __init__(self, tipo="amoled", ancho=7, alto=6):
        self.tipo = tipo
        self.ancho = ancho
        self.alto = alto

    def __str__(self):
        return f"Pantalla(tipo={self.tipo}, ancho={self.ancho}, alto={self.alto})"

class Aplicacion:
    def __init__(self, nombre, tamanio):
        self.nombre = nombre
        self.tamanio = tamanio

    def __str__(self):
        return f"Aplicacion(nombre={self.nombre}, tamanio={self.tamanio})"

class Laptop:
    def __init__(self, modelo, tipo_pantalla, ancho, alto):
        self.modelo = modelo
        self.apps = []  # apps:Aplicacion[50] - AGREGACION
        self.pantalla = Pantalla(tipo_pantalla, ancho, alto) # COMPOSICION

    @property
    def cant_apps(self):
        return len(self.apps)

    def agrega_app(self, app):
        if len(self.apps) < 50:
            self.apps.append(app)

    def eliminar_apps(self):
        self.apps.clear()

    def ordenar_apps(self):
        # f. decreciente por tamanio, si empata por nombre
        self.apps.sort(key=lambda a: (-a.tamanio, a.nombre))

    def __str__(self):
        return f"Laptop(modelo={self.modelo}, cantApps={self.cant_apps}, {self.pantalla}, apps={self.apps})"

# ================= MAIN =================

def main():
    # a. Instanciar N objetos Laptop en un vector
    vec = []
    lap1 = Laptop("samsung", "lcd ips", 13, 7)
    lap1.agrega_app(Aplicacion("Word", 200))
    lap1.agrega_app(Aplicacion("Excel", 150))

    lap2 = Laptop("hp", "oled", 15, 9)
    lap2.agrega_app(Aplicacion("Photoshop", 500))

    lap3 = Laptop("lenovo", "amoled", 13, 7)
    lap3.agrega_app(Aplicacion("Chrome", 300))
    lap3.agrega_app(Aplicacion("VSCode", 250))
    lap3.agrega_app(Aplicacion("Zoom", 100))

    vec.extend([lap1, lap2, lap3])

    # b. Mostrar la laptop que tenga más aplicaciones
    print("--- b. Laptop con mas apps ---")
    mayor = max(vec, key=lambda l: l.cant_apps)
    print(mayor)

    # c. Agregar una aplicacion a la laptop de modelo X
    print("\n--- c. Agregar app ---")
    x = input("Ingrese modelo X: ").strip()
    for l in vec:
        if l.modelo.lower() == x.lower():
            nom = input("Nombre nueva app: ")
            tam = int(input("Tamanio nueva app: "))
            l.agrega_app(Aplicacion(nom, tam))
            print(f"Agregada a {l.modelo}")

    # d. Eliminar todas las aplicaciones de la laptop con pantalla de ancho Y
    print("\n--- d. Eliminar apps por ancho Y ---")
    y = int(input("Ingrese ancho Y: "))
    for l in vec:
        if l.pantalla.ancho == y:
            l.eliminar_apps()
            print(f"Apps eliminadas de: {l.modelo}")

    # e. Mostrar a laptop que tiene mas aplicaciones.
    print("\n--- e. Laptop con mas apps (actualizado) ---")
    mayor = max(vec, key=lambda l: l.cant_apps)
    print(mayor)

    # f. Ordenar de forma decreciente las aplicaciones de cada laptop
    print("\n--- f. Apps ordenadas ---")
    for l in vec:
        l.ordenar_apps()
        print(l)

if __name__ == "__main__":
    main()