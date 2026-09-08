class Libro:
    def __init__(self, titulo: str, autor: str, paginas: int, precio: float):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.precio = precio

    def verificar_precio(self, m: float) -> bool:
        return self.precio > m

    def mostrar(self):
        print(f"Libro: '{self.titulo}' - {self.autor} | Páginas: {self.paginas} | Precio: ${self.precio}")

if __name__ == "__main__":
    lib1 = Libro("Cien años de soledad", "Gabriel García Márquez", 471, 25.50)
    lib2 = Libro(titulo="El principito", autor="Antoine de Saint-Exupéry", paginas=96, precio=12.00)

    lib1.mostrar()
    lib2.mostrar()

    M = 20.0
    print(f"¿El precio de lib1 es mayor a ${M}?: {lib1.verificar_precio(M)}")

    if lib1.paginas > lib2.paginas:
        lib1.mostrar()
    else:
        lib2.mostrar()