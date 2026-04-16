# Juego Piedra, Papel o Tijera.

Información del Proyecto
Desarrollador: Christian Esteban Calderón Acurio 
Fecha de creación: 15 de abril de 2026
Lenguaje: Python 3.14.0

Objetivo del Programa
El objetivo principal de este software es replicar el juego Piedra, Papel o Tijera mediante una programación estructurada y eficiente. El sistema permite una interacción fluida entre un usuario y la computadora (CPU), garantizando una experiencia sin errores mediante la gestión de estados y validación de datos.

# Funcionalidades Principales

1. Inteligencia Aleatoria (random)
Para asegurar un desafío real, el programa utiliza la librería estándar de Python para generar elecciones impredecibles por parte de la CPU.

2. Estructura de Datos: El Diccionario (NORMA)
Se implementó un diccionario como una "lista de relaciones" para simplificar la lógica de victoria. Esto permite que el programa consulte instantáneamente el resultado sin procesos complejos de comparación.

3. Programación Modular (Funciones)
La lógica de combate se procesa en la función obtener_resultado.
Esta utiliza una dinámica de descarte:
  3.1. Verifica el Empate.
  3.2. Consulta el diccionario NORMA para verificar si el jugador Gana.
  3.3. Por defecto, determina si el jugador Pierde.

5. Control de Ciclo de Vida (while)
El programa utiliza bucles para gestionar la persistencia de la aplicación:
  5.1. Bucle Principal: Mantiene el menú activo para navegar entre jugar o leer reglas.
  5.2. Bucle de Juego: Permite jugar múltiples rondas consecutivas sin reiniciar el programa.

6. Lógica de Decisiones y Validación (if, elif, else)
Se utilizan condicionales para dirigir el flujo y asegurar la integridad de los datos:
  6.1. Navegación: Distingue entre las opciones del menú.
  6.2. Validación de entrada: Si el usuario ingresa un dato inválido, la instrucción continue reinicia el bucle de entrada.
  6.3. Seguridad: El else final actúa como una red de seguridad para capturar entradas no reconocidas.

![Flujograma Principal](img/FlujogramaPPT-01.jpg)
![Flujograma Principal](img/FlujogramaPPT-02.jpg)
