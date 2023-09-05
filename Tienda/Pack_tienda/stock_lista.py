from pelicula import Pelicula
from libro import Libro 

pel = Pelicula()
lib = Libro()

lib.Agregar_Libro("Matematicas I", 200, 4)
lib.Agregar_Libro("El perfume", 120, 8)
pel.Agregar_Pelicula("Tarzan", "1:35:00", 3)
pel.Agregar_Pelicula("Rambo", "1:25:00", 9)

def Listar_Stock(numero_stock):
    lista_productos = []
    nueva_lista = []

    for x in pel.Listar_Peliculas():
        lista_productos.append(pel)

    for y in lib.Listar_Libros():
        lista_productos.append(lib)

    for producto in lista_productos:
        if numero_stock >= producto["Stock"]:
            nueva_lista.append(producto)
            
    return (nueva_lista)

print(Listar_Stock(5))