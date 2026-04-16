# Proyecto Final
# Juego Piedra, Papel o Tijera (Christian Esteban Calderón Acurio).

# Primero importo una libreria de Python para generar azar.
import random

# Creamos un diccionario que nos servirá como una lista de relaciones.
# En este caso colocamos las relaciones que derivan en victoria, mas adelante la función se encargará de asignar la derrota o empate.
NORMA = {"piedra" : "tijera", "papel" : "piedra", "tijera" : "papel"}

# Creamos la función del juego, basado en la dinámica de descarte.
def obtener_resultado(jugador, cpu):
    
    # En el caso que sean iguales.
    if jugador == cpu:
        return "Empate"
    
    # En el caso donde la opción que envia el jugador se tranforma en la respuesta del diccionario y eso se compara con el cpu. (Clave:valor)
    elif NORMA[jugador] == cpu:
        return "Ganaste"
    
    # Por descarte, si no empata ni gana.
    else:
        return "Perdiste"

    

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

            # Proceso de asignación de resultado a través de la función.
            resultado = obtener_resultado(eleccion_jugador, eleccion_cpu)
            print("Resultado: " + resultado)

            # Inmediatamente se pregunta se quiere jugar de nuevo.
            jugar_otra = input("\n¿Quieres volver a jugar? (si/no): ")
            if jugar_otra != "si":
                # Si se escribe no se rompe el bucle y termina el juego porque declara false a la variable jugando y ejecutando_juego.    
                jugando = False 
                ejecutando_juego = False
                print("Gracias por jugar.")

    else:
        # Si no escribió ni jugar ni reglas le sale este mensaje.
        print("Opción incorrecta.")
    