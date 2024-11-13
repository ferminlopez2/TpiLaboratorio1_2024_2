import random                   
vida_usuario=3
vida_pc=3
while vida_usuario != 0 and vida_pc != 0:

    aleatorio = random.randrange(0, 3)
    pc = ""
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    opcion = int(input("Que elijes: "))

    if opcion == 1:
        usuario = "piedra"
    elif opcion == 2:
        usuario = "papel"
    elif opcion == 3:
        usuario = "tijera"
    print("Tu elijes: ",usuario)

    if aleatorio == 0:
        pc = "piedra"
    elif aleatorio == 1:
        pc = "papel"
    elif aleatorio == 2:
        pc = "tijera"
    print("PC elijio: ",pc)
    
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



    if vida_usuario==0 or vida_pc==0:
        if vida_usuario == 0:
            print("JUEGO TERMINADO!! GANA PC")
            break
        if vida_pc == 0:
            print("JUEGO TERMINADO!! ¡GANASTE!")
            break

