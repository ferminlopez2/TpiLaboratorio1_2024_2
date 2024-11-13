import random  # se importa random para poder crear numero randoms


def juego_adivinar_numero():  # funcion donde se encuentra el juego
    numero_para_adivinar = random.randint(1, 20)  # se crea un numero al azar del 1 al 20 y se guarda en una variable
    intentos = 0
    print("!!!!Descubre el numero del 1 al 20!!!!")
    while True:
        try:  # el juego se encuentra en un bloque try para asegurar que el juego funcione si ingresa un valor que no es un numero
            numero = int(input("Ingrese un numero: "))
            intentos += 1
            if numero < numero_para_adivinar:
                print("Tu numero es menor al numero secreto.")
            elif numero > numero_para_adivinar:
                print("Tu numero es mayor al numero secreto.")
            else:
                print(f"Felicidades adivinaste el numero secreto en {intentos} intentos.")
                break
        except ValueError:
            print("Ingrese un valor numerico valido:")


def jugar_devuelta():  # funcion para saber si el jugador quiere jugar de vuelta
    while True:
        try:
            print("Ingrese 1 si quiere jugar de vulta y 2 si no quiere jugar de vuelta")
            jugar = int(input("¿Desea jugar de vuelta?: "))

            if jugar == 1:
                juego_adivinar_numero()
            elif jugar == 2:
                break
            else:
                print("Ingrese solamente 1 o 2 ")
        except ValueError:
            print("Ingrese solamente 1 o 2 ")


def tira_la_moneda():
    print("¡Bienvenido al juego de cara o cruz!")

    while True:
        try:
            eleccion = input("Elige: cara o cruz: ").lower()
            if eleccion not in ["cara", "cruz"]:
                raise ValueError("Opción inválida. Por favor ingresa 'cara' o 'cruz'.")
        except ValueError as e:
            print(e)
            continue

            # Simula el lanzamiento de la moneda
        resultado = random.choice(["cara", "cruz"])
        print(f"La moneda cayó en: {resultado}")

        # verifica si el jugador ganó o perdió
        if eleccion == resultado:
            print("¡Ganaste!")
        else:
            print("Perdiste.")

        # pregunta al jugador si quiere jugar otra partida
        try:
            jugar_otra = input("¿Quieres jugar otra partida? (s/n): ").lower()
            if jugar_otra not in ['s', 'n']:
                raise ValueError("Opción inválida. Por favor ingresa 's' o 'n'.")
        except ValueError as e:
            print(e)
            continue

            # Si el jugador elige "n", se termina el juego
        if jugar_otra == 'n':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

def piedra_pael_tijera():
    vida_usuario = 3
    vida_pc = 3
    while vida_usuario != 0 and vida_pc != 0:
        aleatorio = random.randrange(0, 3)
        pc = ""
        print("1) Piedra")
        print("2) Papel")
        print("3) Tijera")
        print("Tienes tres vidas")
        opcion = int(input("Que elijes: "))

        if opcion == 1:
            usuario = "piedra"
        elif opcion == 2:
            usuario = "papel"
        elif opcion == 3:
            usuario = "tijera"
        print("Tu elijes: ", usuario)

        if aleatorio == 0:
            pc = "piedra"
        elif aleatorio == 1:
            pc = "papel"
        elif aleatorio == 2:
            pc = "tijera"
        print("PC elijio: ", pc)

        if pc == "piedra" and usuario == "papel":
            print("GANASTE, papel envulve piedra")
            vida_pc -= 1
        elif pc == "papel" and usuario == "tijera":
            print("GANASTE, Tijera corta papel")
            vida_pc -= 1
        elif pc == "tijera" and usuario == "piedra":
            print("GANASTE, Piedra pisa tijera")
            vida_pc -= 1

        if pc == "papel" and usuario == "piedra":
            print("PERDISTE, papel envulve piedra")
            vida_usuario -= 1
        elif pc == "tijera" and usuario == "papel":
            print("PERDISTE, tijera corta papel")
            vida_usuario -= 1
        elif pc == "piedra" and usuario == "tijera":
            print("PERDISTE, piedra pisa tijera")
            vida_usuario -= 1
        elif pc == usuario:
            print("EMPATE")
        print("-------------")

        if vida_usuario == 0 or vida_pc == 0:
            if vida_usuario == 0:
                print("JUEGO TERMINADO!! GANA PC")
                break
            if vida_pc == 0:
                print("JUEGO TERMINADO!! ¡GANASTE!")
                break


def progreso_palabra(palabra, letras_adivinadas):
    progreso = [letra if letra in letras_adivinadas else '_' for letra in palabra] #Mostrar letras adivinadas en la palabra y '_' en las letras mo adivinadas
    return ' '.join(progreso) #Agrupar '_' dejando un espacio

def guardar_resultado(juego_info):
    with open("resultados_juego.txt", "a") as info:
        info.write(juego_info + "\n")  # Agregar una nueva línea con la información del juego


def juego_adivina_palabra():
    while True:
        print("Hola Bienvenido a adivina la palabra ☻☻ ")
        palabra = input("Para poder jugar Ingresa la palabra a adivinar:\n->  ").upper()  # ingreso de palabra y pasaje a mayuscula.
        intentos = 5  # intentos para adivinar.
        letras_adivinadas = set()
        letras_erradas = set()
        print("\n" * 20)
        print("\n¡¡Comienza el juego, Adivinar la Palabra!! :D")
        print(progreso_palabra(palabra, letras_adivinadas))  # Mostrar en pantalla '_' en letras no adivinadas.

        while intentos > 0:  # Ejecutar mientras aun tenga intentos.
            print(f"\n||intentos restantes: {intentos}||")  # Mostrar intentos restantes.
            letra = input("Adivina una letra: -> ").upper()  # Pasaje de letra ingresada a mayuscula.
            print("\n" * 3)

            if letra in letras_adivinadas or letra in letras_erradas:  # Comprobar que la letra ingresada no fue ingresada anteriormente.
                print(f"◙◙ Ya a ingresado anteriormente la letra ║{letra}║, ingrese otra letra.◙◙")
                progreso_actializado = progreso_palabra(palabra, letras_adivinadas)
                print(progreso_actializado)
                continue

            if letra in palabra:  # comprobar si la letra ingresada esta en la palabra.
                letras_adivinadas.add(letra)  # Agregar la letra adivinada al conjunto 'letras_adivinadas'.
                print(f"◙◙¡Bien!, adivinaste la letra◙◙ ║{letra}║")
            else:
                intentos = intentos - 1  # Restar intentos.
                letras_erradas.add(letra)  # Agregar letra incorrecta al conjunto 'letras_erradas'.
                print(f"◙◙¡Incorrecto!, la letra ║{letra}║ no esta en la palabra◙◙")

            progreso_actializado = progreso_palabra(palabra, letras_adivinadas)
            print(progreso_actializado)  # Mostrar el progreso de letras adivinadas.

            if "_" not in progreso_actializado:  # Comprobar si ya adivinaron todas las letras de la palabra.
                print("\n" * 3)
                print("☻☻¡Felesidades, adivinaste la palabra!☻☻")
                resultado = f"Palabra: {palabra}, Resultado: Adivino"
                guardar_resultado(resultado)  # Guardar el resultado en el archivo
                break
        else:
            print(f"◙◙¡Perdiste!◙◙ ◙◙La palabra a adivinar fue:◙◙ ║{palabra}║ ")  # Mostrar que ya no hay intentos.
            resultado = f"Palabra: {palabra}, Resultado: Perdio"
            guardar_resultado(resultado)  # Guardar el resultado en el archivo

        jugar_nuevamente = input("¿Quieres jugar nuevamente? \n'S/N'\nS = Si\nN = No\n-> ").upper()
        if jugar_nuevamente == 'N':
            print("¡Gracias por jugar! :)")
            break
        while jugar_nuevamente != "S" and jugar_nuevamente != "N":
            print("Valores permitidos: S/N")
            jugar_nuevamente = input("¿Quieres jugar nuevamente? \n'S/N'\nS = Si\nN = No\n-> ").upper()
        if jugar_nuevamente == 'N':
            print("¡Gracias por jugar! :)")
            break


lista_juegos = ["PIEDRA PAPEL O TIJERA", "ADIVINA EL NUMERO", "TIRAR LA MONEDA", "ADIVINA LA PALABRA"]
menu = 0
while menu != 5:
    print("JUEGOS")
    print("1- PIEDRA PAPEL O TIJERA")
    print("2- ADIVINA EL NUMERO ")
    print("3- TIRAR LA MONEDA")
    print("4- ADIVINA LA PALABRA")
    print("5- SALIR")
    menu = int(input("Escribe que juego quiere jugar: "))
    if menu == 1:
        print("BIENVENIDO A ", lista_juegos[0], piedra_pael_tijera())
    if menu == 2:
        print("BIENVENIDO A ", lista_juegos[1], juego_adivinar_numero(),jugar_devuelta())
    if menu == 3:
        print("BIENVENIDO A ", lista_juegos[2], tira_la_moneda())
    if menu == 4:
        print("BIENVENIDO A ", lista_juegos[3], juego_adivina_palabra())

print("Gracias por jugar con nuestro juegos ☻☻")