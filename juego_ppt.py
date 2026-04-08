# APRENDIZAJE AUTÓNOMO 2
# Juego Piedra, Papel o Tijera (Christian Esteban Calderón Acurio).

# Primero importo una libreria de Python para generar azar.
import random

# Creo la lista de opociones válidas dentro del juego.
opciones_ppt = ["piedra", "papel", "tijera"]

# Creo la variable que permite que el juego se mantenga en bucle con while.
# Debe ser un booleano.
ejecutando_juego = True

while ejecutando_juego:
    # Print del título y su input.
    print("\nPIEDRA, PAPEL O TIJERA")
    opciones_menu = input("Escribe 'jugar' para iniciar o 'reglas' para ver instrucciones: ")

    # Opción de reglas.
    if opciones_menu == "reglas":
        print("\nREGLAS DEL JUEGO")
        print("Piedra gana a Tijera. Tijera gana a Papel. Papel gana a Piedra.")
        print("Si ambos eligen lo mismo, empate.")

    # Opción de Jugar.    
    elif opciones_menu == "jugar":
        # Creo otro booleano para que se mantenga en bucle con el segundo while.
        jugando = True
        
        while jugando:
            # Input de la elección del jugador.
            eleccion_jugador = input("\nElige piedra, papel o tijera: ")

            if eleccion_jugador not in opciones_ppt:
                print("Opción incorrecta. Inténtalo de nuevo.")
                # Usamos la función continue que permite saltarse la linea de codigo (la vuelta) y repite el while. no break porque acaba el bucle.
                continue

            # Elección del CPU.
            eleccion_cpu = random.choice(opciones_ppt)
            print("La computadora eligió: " + eleccion_cpu)

            # Proceso de Asignación de Resultado.
            # Creo la variable resultado, que se va ha determinar cuando termine el proceso de Asignación.
            resultado = ""

            # Caso 1: El jugador eligió piedra.
            if eleccion_jugador == "piedra":
                if eleccion_cpu == "piedra":
                    resultado = "EMPATE"
                elif eleccion_cpu == "papel":
                    resultado = "PERDISTE"
                # Se asume tijera porque ya se descartan las otras opciones en los pasos anteriores.
                else:
                    resultado = "GANASTE"

            # Caso 2: El jugador eligió papel.
            elif eleccion_jugador == "papel":
                if eleccion_cpu == "piedra":
                    resultado = "GANASTE"
                elif eleccion_cpu == "papel":
                    resultado = "EMPATE"
                else:
                    resultado = "PERDISTE"

            # Caso 3: El jugador eligió tijera
            # Aquí no se coloca nada en else porque ya no queda otra opción más que tijera.
            else:
                if eleccion_cpu == "piedra":
                    resultado = "PERDISTE"
                elif eleccion_cpu == "papel":
                    resultado = "GANASTE"
                else:
                    resultado = "EMPATE"

            # Con la variable determinada se muestra el resultado.
            print(resultado)

            # Inmediatamente se pregunta se quiere jugar de nuevo.
            jugar_otra = input("\n¿Quieres volver a jugar? (si/no): ")
            if jugar_otra != "si":
                # Si se escribe no se rompe el bucle y termina el juego porque declara false a la variable jugando y ejecutando_juego.    
                jugando = False 
                print("Gracias por jugar.")
                ejecutando_juego = False

    else:
        # Si no escribió ni jugar ni reglas le sale este mensaje.
        print("Opción incorrecta.")
    









# prueba de cambio en github.