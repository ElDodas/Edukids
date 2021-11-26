import functions as func # Se importa el archivo functions.py donde se encuentran todas las funciones que usa el programa

while func.condicion1: #menú principal
    if func.main_menu() == 1: # Llama a la función principal para elegir entre (1) juegos o (2) salir 
        func.condicion2 = True # Se vuelven a iniciar las condiciones de los bucles de los menús para poder recorrerlos todas la veces que queramos
        while func.condicion2: #menú de categorias
            categoria = func.category_menu() # Llama a el menú de categorías de juegos y devuelve un número de 1 a 5, siendo este último para volver al menú anterior
            if categoria == 1: #matematicas
                func.condicion3 = True # Se vuelven a iniciar la condicion del bucle para poder recorrerlos todas la veces que queramos
                while func.condicion3: 
                    categoria2 = func.matematicas() # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
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
                    categoria2 = func.lengua() # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
                    if categoria2 == 1:
                        func.ahorcado()
                    elif categoria2 == 2:
                        func.sinonimos()   
                    elif categoria2 == 3:
                        func.condicion3 = False
            elif categoria == 3: #ciencia
                func.condicion3 = True # Se vuelven a iniciar la condicion del bucle para poder recorrerlos todas la veces que queramos
                while func.condicion3:
                    categoria2 = func.ciencia() # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
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
                    categoria2 = func.casual() # Según el número que nos devuelva la función se iniciará un juego o otro, o saldrá al menú anterior
                    if categoria2 == 1:
                        func.trivial()
                    elif categoria2 == 2:
                        func.condicion3 = False
            elif categoria == 5: #Volver
                func.condicion2 = False
    else:
        func.condicion1 = False