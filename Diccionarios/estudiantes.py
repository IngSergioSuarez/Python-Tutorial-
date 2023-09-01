estudiantes = {}
estudiantes = {"Gino":42,"Paula":28,"Juliana":29,"Oscar":29,"Felipe":32,"Julian":23}

#Para conocer el valor de una llave colocamos el nombre de la clave en corchetes

print(estudiantes["Gino"]) # Imprimira el valor de la llave "Gino" el resultado en consola deberia ser 42
print(estudiantes) # para poder imprimir todo el diccionario se usa print y la variable usada para guardar el diccionario

estudiantes["Sergio"] = 28 # Podemos agregar un nuevo dato en el diccionario colocando en corchetes la clave y asignando el valor en la clave despues del igual
print(estudiantes)

# Si deseamos eliminar un dato del diccionario podemos usar la función "del nombre_dic[llave]" tener en cuenta de que no solo se borra la imagen sino tambien el valor 

del estudiantes["Gino"]
print(estudiantes)

# para imprimir las llaves de un diccionario usamos el metodo ".keys()" 

print(estudiantes.keys()) #Imprimira solo las claves del diccionario

# para imprimir las llaves de un diccionario usamos el metodo ".values()" 

print(estudiantes.values()) #Imprimira solo los valores del diccionario

# los valores de Keys y Values los podemos guardar como listas para futuros usos utilizado la funcion "List()" y guardandola en una variable

llaves = list(estudiantes.keys())
print(f"los valores de las llaves del diccionario son: {llaves}")
valores = list(estudiantes.values())
print(f"los valores  del diccionario son: {valores}")



