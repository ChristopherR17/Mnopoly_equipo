#Monopoly

def print_tablero():
    # Casillas
    tablero = [["Parking","Urqinoa","Fontan","Sort","Rambles","Pl.Cat","Anr pró"],
               ["Aragó","","","","","","Angel"],
               ["S.Joan","","","","","","Augusta"],
               ["Caixa","","","","","","Caixa"],
               ["Aribau","","","","","","Balmes"],
               ["Muntan","","","","","","Gracia"],
               ["Presó","Consell","Marina","Sort","Rosell","Lauria","Sortida"]]
    
    #Borde superior
    print("+--------+--------+--------+--------+--------+--------+--------+")
    print(f"|{tablero[0][0]:^8}|{tablero[0][1]:^8}|{tablero[0][2]:^8}|{tablero[0][3]:^8}|{tablero[0][4]:^8}|{tablero[0][5]:^8}|{tablero[0][6]:^8}|")
    print(f"|{'':^8}|{'':^8}|{'':^8}|{'':^8}|{'':^8}|{'':^8}|{'':^8}|")
    print("+--------+--------+--------+--------+--------+--------+--------+")

    # Filas laterales (izquierda y derecha) + espacios en medio
    for i in range(1, 6):
        print(f"|{tablero[i][0]:^8}|{'':<40}|{tablero[i][6]:^8}|")
        print(f"|{'':^8}|{'':<40}|{'':^8}|")
        print("+--------+                                          +--------+")

    # Borde inferior
    print(f"|{tablero[6][0]:^8}|{tablero[6][1]:^8}|{tablero[6][2]:^8}|{tablero[6][3]:^8}|{tablero[6][4]:^8}|{tablero[6][5]:^8}|{tablero[6][6]:^8}|")
    print(f"|{'':^8}|{'':^8}|{'':^8}|{'':^8}|{'':^8}|{'':^8}|{'':^8}|")
    print("+--------+--------+--------+--------+--------+--------+--------+")


print_tablero()

def jugadores(jugador,carrers,diners,especial):
    pass