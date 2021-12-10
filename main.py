import functions as func # Se importa el archivo functions.py donde se encuentran todas las funciones que usa el programa

logged, rachas = False, True
User_dates = []

func.listado_usuarios()

while func.condicion1: #menú principal
    if logged == True and rachas == True:
        User_dates = func.rachas(User_dates)
        rachas = False

    categoria0 = func.main_menu(logged,User_dates)
    if categoria0 == 1: # Llama a la función principal para elegir entre (1) juegos o (2) salir 
        func.condicion2 = True # Se vuelven a iniciar las condiciones de los bucles de los menús para poder recorrerlos todas la veces que queramos
        while func.condicion2: #menú de categorias
            categoria = func.category_menu(logged,User_dates) # Llama a el menú de categorías de juegos y devuelve un número de 1 a 5, siendo este último para volver al menú anterior
            if categoria == 1: #matematicas
                func.condicion3 = True # Se vuelven a iniciar la condicion del bucle para poder recorrerlos todas la veces que queramos
                while func.condicion3: 
                    categoria2 = func.matematicas(User_dates) # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
                    if categoria2 == 1:
                        User_dates = func.buscanumeros(User_dates)
                    elif categoria2 == 2:
                        User_dates = func.sucesiones(User_dates)
                    elif categoria2 == 3:
                        User_dates = func.operaciones(User_dates)
                    elif categoria2 == 4:
                        User_dates = func.problemas(User_dates)
                    elif categoria2 == 5:
                        func.condicion3 = False
            elif categoria == 2: #lengua
                func.condicion3 = True # Se vuelven a iniciar la condicion del bucle para poder recorrerlos todas la veces que queramos
                while func.condicion3:
                    categoria2 = func.lengua(User_dates) # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
                    if categoria2 == 1:
                        User_dates = func.ahorcado(User_dates)
                    elif categoria2 == 2:
                        User_dates = func.sinonimos(User_dates)   
                    elif categoria2 == 3:
                        func.condicion3 = False
            elif categoria == 3: #ciencia
                func.condicion3 = True # Se vuelven a iniciar la condicion del bucle para poder recorrerlos todas la veces que queramos
                while func.condicion3:
                    categoria2 = func.ciencia(User_dates) # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
                    if categoria2 == 1:
                        User_dates = func.science_questions(User_dates)
                    elif categoria2 == 2:
                        User_dates = func.historic_dates(User_dates)
                    elif categoria2 == 3:
                        User_dates = func.countries_questions(User_dates)
                    elif categoria2 == 4:
                        func.condicion3 = False
            elif categoria == 4: #casual
                func.condicion3 = True # Se vuelven a iniciar la condicion del bucle para poder recorrerlos todas la veces que queramos
                while func.condicion3:
                    categoria2 = func.casual(User_dates) # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
                    if categoria2 == 1:
                        User_dates = func.trivial(User_dates)
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
                User_dates = [logged_User[1][0],logged_User[1][1]]
            elif categoria_loggin == 2:
                func.register()
        else:
            func.estadisticas(User_dates) # Función estadísticas
    else:
        func.condicion1 = False