import functions as func # Se importa el archivo functions.py donde se encuentran todas las funciones que usa el programa

logged = False
User_dates = []

func.listado_usuarios()

while func.condicion1: #menú principal
    categoria0 = func.main_menu(logged,User_dates)
    if categoria0 == 1: # Llama a la función principal para elegir entre (1) juegos o (2) salir 
        func.condicion2 = True # Se vuelven a iniciar las condiciones de los bucles de los menús para poder recorrerlos todas la veces que queramos
        while func.condicion2: #menú de categorias
            categoria = func.category_menu(logged,User_dates) # Llama a el menú de categorías de juegos y devuelve un número de 1 a 5, siendo este último para volver al menú anterior
            if categoria == 1: #matematicas
                func.condicion3 = True # Se vuelven a iniciar la condicion del bucle para poder recorrerlos todas la veces que queramos
                while func.condicion3: 
                    categoria2 = func.matematicas(logged,User_dates) # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
                    if categoria2 == 1:
                        func.buscanumeros()
                    elif categoria2 == 2:
                        func.sucesiones()
                    elif categoria2 == 3:
                        func.operaciones()
                    elif categoria2 == 4:
                        func.problemas()
                    elif categoria2 == 5:
                        func.condicion3 = False
            elif categoria == 2: #lengua
                func.condicion3 = True # Se vuelven a iniciar la condicion del bucle para poder recorrerlos todas la veces que queramos
                while func.condicion3:
                    categoria2 = func.lengua(logged,User_dates) # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
                    if categoria2 == 1:
                        func.ahorcado()
                    elif categoria2 == 2:
                        func.sinonimos()   
                    elif categoria2 == 3:
                        func.condicion3 = False
            elif categoria == 3: #ciencia
                func.condicion3 = True # Se vuelven a iniciar la condicion del bucle para poder recorrerlos todas la veces que queramos
                while func.condicion3:
                    categoria2 = func.ciencia(logged,User_dates) # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
                    if categoria2 == 1:
                        func.science_questions()
                    elif categoria2 == 2:
                        func.historic_dates()
                    elif categoria2 == 3:
                        func.countries_questions()
                    elif categoria2 == 4:
                        func.condicion3 = False
            elif categoria == 4: #casual
                func.condicion3 = True # Se vuelven a iniciar la condicion del bucle para poder recorrerlos todas la veces que queramos
                while func.condicion3:
                    categoria2 = func.casual(logged,User_dates) # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
                    if categoria2 == 1:
                        func.trivial()
                    elif categoria2 == 2:
                        func.condicion3 = False
            elif categoria == 5: #Volver
                func.condicion2 = False
    elif categoria0 == 2:
        if logged == False:
            pass # Función loggin
            categoria_loggin = func.login_register_menu()
            if categoria_loggin == 1:
                logged_User = func.login() # Login devuelve una lista con el valor de si está loggeado y los datos del usuario
                logged = logged_User[0]
                User_dates = logged_User[1]
            elif categoria_loggin == 2:
                func.register()
        else:
            pass # Función estadísticas
    else:
        func.condicion1 = False