import random

salud = 50 
dificultad = 2 # 3 modos de dificultad 1 = Facil || 2 = Medio || 3 = Dificil (El valor se debe colocar en el GUI) 

pocion_salud = random.randint(25,50)/dificultad # Genera un numero randon en un rango entre 25 y 50 

salud = salud + pocion_salud

print(salud)