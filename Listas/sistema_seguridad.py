lista_Usuarios = ["Diego","Felipe", "Luis","Juan","Nicolas","Camilo"]

while True: 
    print("¡Bienvenido a su sistema de segridad!\n")
    nombre_usuario = input("Ingrese su usuario: ").strip().capitalize()

    if nombre_usuario in lista_Usuarios:
        opcion_menu = int(input(f"\nBienvenido {nombre_usuario}, escoge una de las opciones del siguiente menu:\n\n\t1- Eliminar el usuario.\n\t2- Agregar un nuevo usuario.\n\t3- imprimir lista de usuarios.\n\t4- Salir. "))

        if opcion_menu == 1:

            usuario_Eliminar = input("Ingrese el usuario a Eliminar: ")

            if usuario_Eliminar in lista_Usuarios:
                lista_Usuarios.remove(usuario_Eliminar)
            else:
                print("El usuario ingresado no se encuentra creado.")

        elif opcion_menu == 2: 

            usuario_Agregar = input("Ingrese el usuario a agregar: ")

            lista_Usuarios.append(usuario_Agregar)

        elif opcion_menu == 3: 

            for i in lista_Usuarios:
                print(i)

        elif opcion_menu == 4: 

            print(f"Gracias por utilizar nuestro sistema {nombre_usuario}... ¡Vuelve Pronto!")
            break
    
    else: 
        print("Ingrese un usuario valido...")



    


            


