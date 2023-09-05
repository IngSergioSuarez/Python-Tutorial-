libros = []

class Libro :
    def __init__(self, nombre = "", hojas = 0, stock = 0):
        self.nombre = nombre
        self.hojas = hojas
        self.stock = stock

    def Agregar_Libro(self, nombre, hojas, stock):
        self.nombre = nombre
        self.hojas = hojas
        self.stock = stock
        libros.append({
            "Titulo": nombre,
            "hojas": hojas,
            "Stock": stock
        })

    def Listar_Libros(self):
        for i in libros:
            print(i)


# Usar el siguiente codigo solo para pruebas

"""
lib = Libro()
lib.Agregar_Libro("Matematicas I", 200, 21)
lib.Agregar_Libro("El perfume", 120, 15)

lib.Listar_Libros()

"""