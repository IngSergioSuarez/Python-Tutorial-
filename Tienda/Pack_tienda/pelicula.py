peliculas = []

class Pelicula :
    def __init__(self, nombre = "", duracion = "", stock = 0):
        self.nombre = nombre
        self.duracion = duracion
        self.stock = stock

    def Agregar_Pelicula(self, nombre, duracion, stock):
        self.nombre = nombre
        self.duracion = duracion
        self.stock = stock
        peliculas.append({
            "Pelicula": nombre,
            "Duracion": duracion,
            "Stock": stock
        })

    def Listar_Peliculas(self):
        for i in peliculas:
            print(i)


# Usar el siguiente codigo solo para pruebas

"""
p = Pelicula()
p.Agregar_Pelicula("Tarzan", "1:35:00", 21)
p.Agregar_Pelicula("Rambo", "1:25:00", 15)

p.Listar_Peliculas()


"""
