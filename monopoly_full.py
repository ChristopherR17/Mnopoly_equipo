#MONOPOLY
#ALUMNOS: CHRISTOPHER Y MARC
import random
import os

def clearScreen():
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

def banca():
    banc = 1000000
    if banc <= 500000:
        banc += 1000000
        return banc
    else:
        return banc
    
def orden_tirada():
    jugadores = ['Vermell', 'Groc', 'Taronja', 'Blau']
    random.shuffle(jugadores)
    return jugadores

def asignar_especial(jugadors):
    jugador_especial = random.choice(list(jugadors.keys()))
    jugadors[jugador_especial]["especial"] = "Sortir de la presó"

jugadors = {
        "Groc": {
            "Propietats": [],
            "diners": 2000,
            "posicio": 0,
            "inicial": "G",
            "especial": "",
            "torns_pressó": 0
        },
        "Taronja": {
            "Propietats": [],
            "diners": 2000,
            "posicio": 0,  
            "inicial": "T",
            "especial": "",
            "torns_pressó": 0
        },
        "Vermell": {
            "Propietats": [],
            "diners": 2000,
            "posicio": 0,  
            "inicial": "V",
            "especial": "",
            "torns_pressó": 0
        },
        "Blau": {
            "Propietats": [],
            "diners": 2000,
            "posicio": 0,  
            "inicial": "B",
            "especial": "",
            "torns_pressó": 0
        }
    }

def taulellDibuixar():
    t = []
    casa = []
    hotel = []

    dic_carrers = {
        'Sortida': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 0},
        'Lauria': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 1},
        'Rosselló': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 2},
        'Sort': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 3},
        'Marina': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 4},
        'Consell de cent': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 5},
        'Muntaner': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 6},
        'Aribau': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 7},
        'Caixa 1': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 8},
        'Sant Joan': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 9},
        'Aragó': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 10},
        'Parking': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 11},
        'Urquinaona': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 12},
        'Fontana': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 13},
        'Les Rambles': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 14},
        'Plaça Catalunya': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 15},
        'Portal de lÀngel': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 16},
        'Via Augusta': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 17},
        'Caixa 2': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 18},
        'Balmes': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 19},
        'Passeig de Gràcia': {'Num. Cases': 0, 'Num. Hoteles': 0, 'posicio': 20}
    }

    

    banca = {
        "diners": 5000  # Dinero inicial de la banca
    }

    for i in range(0, 24):
        t.append("")
        casa.append("")
        hotel.append("")  # Casillas vacías

    # Obtener el orden de tirada de los jugadores
    orden_jugadores = orden_tirada()

    # Colocar los jugadores en la casilla 0 ("Sortida") en el orden de tirada
    t[0] = "".join([jugadors[jugador]["inicial"] for jugador in orden_jugadores])

    # Añadir casas y hoteles a las calles
    for carrer in dic_carrers:
        num_casa = dic_carrers[carrer]['Num. Cases']
        num_hotels = dic_carrers[carrer]['Num. Hoteles']
        posicio_carrer = dic_carrers[carrer]['posicio']  # posición de la calle

        if num_hotels == 0 and num_casa > 0:
            casa[posicio_carrer] = "--" + str(num_casa) + "C"
        elif num_casa > 0 and num_hotels > 0:
            casa[posicio_carrer] = str(num_hotels) + "H" + str(num_casa) + "C"
        else:
            casa[posicio_carrer] = "----"

        # Casas y hoteles en calles específicas
        if posicio_carrer in [4, 5, 6, 7, 12, 13, 14, 15]:
            if num_casa > 0:
                casa[posicio_carrer] = str(num_casa) + "C"
            if num_hotels > 0:
                hotel[posicio_carrer] = str(num_hotels) + "H"
            else:
                casa[posicio_carrer] = " |"
                hotel[posicio_carrer] = " |"

    # Ajustar los espacios para los jugadores
    for i in range(len(t)):
        t[i] = t[i].ljust(6)

    info_jugadors = ""
    for color, info in jugadors.items():
        info_jugadors += f"{color}:\n  Diners: {info['diners']}\n  Posició: {info['posicio']}\n  Especial: {info['especial']}\n\n"

    print(f"""
                +--------+----{casa[8]}+----{casa[9]}+--------+----{casa[10]}+---{casa[11]}+---------+   "Banca":
                |Parking |Urquinao|Fontana |Sort    |Rambles |Pl.Cat  |Anr pró |    Diners: {banca['diners']}
                |{t[12]}  |{t[13]}  |{t[14]}  |{t[15]}  |{t[16]}  |{t[17]}  |{t[18]}  |   
                +--------+--------+--------+--------+--------+--------+--------+   Jugadors:
                |Aragó  {casa[7]}                                            | Angel {casa[12]}    Jugador Blau:   
                |{t[11]} {hotel[7]}                                            |{t[19]} {hotel[12]}  Diners: {jugadors["Blau"]['diners']}   
                +--------+                                            +--------+   Especial: {jugadors["Blau"]['especial']}      
                |S.Joan {casa[6]}                                            |Augusta{casa[13]}   Jugador Vermell:   
                |{t[10]} {hotel[6]}                                            |{t[20]} {hotel[13]}  Diners: {jugadors["Vermell"]['diners']}
                +--------+                                            +--------+   Especial: {jugadors["Vermell"]['especial']}  
                |Caixa   |                                            |Caixa   |   Jugador Taronja:   
                |{t[9]}  |                                            |{t[21]}  |   Diners: {jugadors["Taronja"]['diners']}
                +--------+                                            +--------+   Especial: {jugadors["Taronja"]['especial']}   
                |Aribau {casa[5]}                                            |Balmes {casa[14]}   Jugador Groc:   
                |{t[8]} {hotel[5]}                                            |{t[22]} {hotel[14]}  Diners: {jugadors["Groc"]['diners']}
                +--------+                                            +--------+   Especial: {jugadors["Groc"]['especial']}   
                |Muntan {casa[4]}                                            |Gracia {casa[15]}
                |{t[7]} {hotel[4]}                                            |{t[23]} {hotel[15]}
                +--------+----{casa[3]}+----{casa[2]}+--------+----{casa[1]}+----{casa[0]}+--------+
                |{t[6]}  |{t[5]}  |{t[4]}  |{t[3]}  |{t[2]}  |{t[1]}  |{t[0]}  |
                |Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |
                +--------+--------+--------+--------+--------+--------+--------+
""")

def dados():
    return random.randint(1, 6), random.randint(1, 6)

def caselles_especials(jugador, jugadors):
    # Obtener la información del jugador
    info_jugador = jugadors[jugador]
    posicio = info_jugador["posicio"]
    diners = info_jugador["diners"]
    especial = info_jugador["especial"]
    torns_preso = info_jugador.get("torns_preso", 0)  # Control de turnos en prisión

    # Si está en prisión, debe esperar o sacar dobles para salir
    if posicio == 6 and torns_preso > 0:
        dado1, dado2 = dados()

        if dado1 == dado2:  # Si saca dobles, puede salir de la prisión
            print(f"{jugador} ha sacado dobles y puede salir de la prisión.")
            jugadors[jugador]["torns_preso"] = 0
        else:
            jugadors[jugador]["torns_preso"] -= 1
            print(f"{jugador} sigue en la prisión. Le quedan {jugadors[jugador]['torns_preso']} turnos.")
            return jugadors  # El jugador no puede jugar este turno

    # Tirar los dados si no está en prisión o si ya ha salido
    dado1, dado2 = dados()

    # Actualizar la posición
    posicio += (dado1 + dado2)

    # Si pasa de la casilla 23, vuelve a empezar desde la casilla 0
    if posicio >= 23:
        posicio -= 23

    # Actualizar la posición en el diccionario del jugador
    jugadors[jugador]["posicio"] = posicio
    print(f"{jugador} ha avançat a la posició {posicio}.")

    # Casilla según la posición del tablero
    if posicio == 0:  # Sortida
        diners += 200
        print(f"{jugador} ha cobrat 200€ per caure a la Sortida. Total diners: {diners}€")

    elif posicio == 6:  # Presó
        if especial == "Sortir de la presó":
            print(f"{jugador} utilitza la seva carta per sortir de la presó.")
            jugadors[jugador]["especial"] = ""  # Pérdida de la carta
        else:
            print(f"{jugador} ha anat a la presó. Perderá 3 turnos o deberá sacar dobles para salir.")
            jugadors[jugador]["torns_preso"] = 3  # El jugador pierde 3 turnos

    elif posicio == 18:  # Anar a la presó
        print(f"{jugador} ha anat a la presó sense cobrar la sortida i sense jugar 3 torns.")
        jugadors[jugador]["posicio"] = 6  # Va a la casilla de prisión
        jugadors[jugador]["torns_preso"] = 3  # Pierde 3 turnos

    elif posicio == 12:  # Parking
        print(f"{jugador} ha caigut al Parking i no cobra ni paga res.")

    elif posicio in [3, 15]:  # Tarjeta de Sort (posiciones 3 y 15)
        Tarjetes_sort = [
            "Sortir de la presó", 
            "Anar a la presó", 
            "Anar a la sortida", 
            "Anar tres espais endarrera", 
            "Fer reparacions a les propietats", 
            "Ets escollit alcalde, cada jugador el paga 50€"
        ]
        tarjeta = random.choice(Tarjetes_sort)
        print(f"{jugador} ha tirat la tarjeta: {tarjeta}")

        if tarjeta == "Sortir de la presó":
            print(f"{tarjeta}: {jugador} podrà seguir jugant i perdrà aquesta opció.")
            jugadors[jugador]["especial"] = tarjeta
        elif tarjeta == "Anar a la presó":
            print(f"{tarjeta}: {jugador} va a la presó sense cobrar la sortida i sense jugar 3 torns.")
            jugadors[jugador]["posicio"] = 6
            jugadors[jugador]["torns_preso"] = 3
        elif tarjeta == "Anar a la sortida":
            print(f"{tarjeta}: {jugador} va a la sortida i cobra 200€.")
            diners += 200
        elif tarjeta == "Anar tres espais endarrera":
            print(f"{tarjeta}: {jugador} va tres espais endarrera.")
            posicio -= 3
        elif tarjeta == "Fer reparacions a les propietats":
            # Calcular el cost total de reparacions
            num_propiedades = len(info_jugador["carrers"])
            num_hotels = info_jugador["hotels"]
            cost_reparaciones = (25 * num_propiedades) + (100 * num_hotels)

            # Actualizar el dinero del jugador
            diners -= cost_reparaciones
            print(f"{jugador} paga {cost_reparaciones}€ per reparacions (25€ per propietat i 100€ per hotel). Total diners: {diners}€.")

        elif tarjeta == "Ets escollit alcalde, cada jugador el paga 50€":
            print(f"{tarjeta}: {jugador} rep 50€ de cada jugador.")
            for other_jugador in jugadors:
                if other_jugador != jugador:
                    jugadors[other_jugador]["diners"] -= 50  # Otros jugadores pagan 50€
                    jugadors[jugador]["diners"] += 50  # El jugador alcalde recibe 50€

    elif posicio in [9, 21]:  # Tarjeta de Caixa (posiciones 9 y 21)
        Tarjetes_caixa = [
            "Sortir de la presó", 
            "Anar a la presó", 
            "Error de banca al teu favor, guanyes 150€", 
            "Despeses mèdiques, pagues 50€", 
            "Despeses escolars, pagues 50€", 
            "Reparacions al carrer, pagues 40€", 
            "Concurs de bellesa, guanyes 10€"
        ]
        tarjeta = random.choice(Tarjetes_caixa)
        print(f"{jugador} ha tirat la tarjeta: {tarjeta}")

        if tarjeta == "Sortir de la presó":
            print(f"{tarjeta}: {jugador} podrà seguir jugant i perdrà aquesta opció.")
            jugadors[jugador]["especial"] = tarjeta
        elif tarjeta == "Anar a la presó":
            print(f"{tarjeta}: {jugador} va a la presó sense cobrar la sortida i sense jugar 3 torns.")
            jugadors[jugador]["posicio"] = 6
            jugadors[jugador]["torns_preso"] = 3
        elif tarjeta == "Error de banca al teu favor, guanyes 150€":
            print(f"{tarjeta}: {jugador} guanya 150€.")
            diners += 150
        elif tarjeta == "Despeses mèdiques, pagues 50€":
            print(f"{tarjeta}: {jugador} paga 50€.")
            diners -= 50
        elif tarjeta == "Despeses escolars, pagues 50€":
            print(f"{tarjeta}: {jugador} paga 50€.")
            diners -= 50
        elif tarjeta == "Reparacions al carrer, pagues 40€":
            print(f"{tarjeta}: {jugador} paga 40€.")
            diners -= 40
        elif tarjeta == "Concurs de bellesa, guanyes 10€":
            print(f"{tarjeta}: {jugador} guanya 10€.")
            diners += 10

    # Actualizar dineros y posición del jugador
    jugadors[jugador]["diners"] = diners
    jugadors[jugador]["posicio"] = posicio

    return jugadors

def turno_jugador(jugador):
    dado1, dado2 = dados()
    if jugadors[jugador]["torns_pressó"] > 0:
        print(f"{jugador} está en la presó y tiene que esperar {jugadors[jugador]['torns_pressó']} turnos más.")
        jugadors[jugador]["torns_pressó"] -= 1
    else:
        jugadors[jugador]["posicio"] += dado1+dado2

def propiedades():
    propiedad = {
        "Lauria": {
            "LL_Casa": 10,
            "LL_Hotel": 15,
            "CMP_Trrny": 50,
            "CMP_Casa": 200,
            "CMP_Hotel": 250,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Rosselló": {
            "LL_Casa": 10,
            "LL_Hotel": 15,
            "CMP_Trrny": 50,
            "CMP_Casa": 225,
            "CMP_Hotel": 255,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Marina": {
            "LL_Casa": 15,
            "LL_Hotel": 15,
            "CMP_Trrny": 50,
            "CMP_Casa": 250,
            "CMP_Hotel": 260,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "C. de cent": {
            "LL_Casa": 15,
            "LL_Hotel": 20,
            "CMP_Trrny": 50,
            "CMP_Casa": 275,
            "CMP_Hotel": 265,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Muntaner": {
            "LL_Casa": 20,
            "LL_Hotel": 20,
            "CMP_Trrny": 60,
            "CMP_Casa": 300,
            "CMP_Hotel": 270,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Aribau": {
            "LL_Casa": 20,
            "LL_Hotel": 20,
            "CMP_Trrny": 60,
            "CMP_Casa": 325,
            "CMP_Hotel": 275,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Sant Joan": {
            "LL_Casa": 25,
            "LL_Hotel": 25,
            "CMP_Trrny": 60,
            "CMP_Casa": 350,
            "CMP_Hotel": 280,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Aragó": {
            "LL_Casa": 25,
            "LL_Hotel": 25,
            "CMP_Trrny": 60,
            "CMP_Casa": 375,
            "CMP_Hotel": 285,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Urquinaona": {
            "LL_Casa": 30,
            "LL_Hotel": 25,
            "CMP_Trrny": 70,
            "CMP_Casa": 400,
            "CMP_Hotel": 290,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Fontana": {
            "LL_Casa": 30,
            "LL_Hotel": 30,
            "CMP_Trrny": 70,
            "CMP_Casa": 425,
            "CMP_Hotel": 300,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Les Rambles": {
            "LL_Casa": 35,
            "LL_Hotel": 30,
            "CMP_Trrny": 70,
            "CMP_Casa": 450,
            "CMP_Hotel": 310,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Pl. Catalunya": {
            "LL_Casa": 35,
            "LL_Hotel": 30,
            "CMP_Trrny": 70,
            "CMP_Casa": 475,
            "CMP_Hotel": 320,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "P. Àngel": {
            "LL_Casa": 40,
            "LL_Hotel": 35,
            "CMP_Trrny": 80,
            "CMP_Casa": 500,
            "CMP_Hotel": 330,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Via Augusta": {
            "LL_Casa": 40,
            "LL_Hotel": 35,
            "CMP_Trrny": 80,
            "CMP_Casa": 525,
            "CMP_Hotel": 340,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Balmes": {
            "LL_Casa": 50,
            "LL_Hotel": 40,
            "CMP_Trrny": 80,
            "CMP_Casa": 550,
            "CMP_Hotel": 350,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        },
        "Pg. de Gràcia": {
            "LL_Casa": 50,
            "LL_Hotel": 50,
            "CMP_Trrny": 80,
            "CMP_Casa": 525,
            "CMP_Hotel": 360,
            "Num. Cases": 0,
            "Num. Hoteles": 0
        }
    }
    
    return propiedad

#Global de propiedades
propiedad = propiedades()

# Lista global de jugadores en orden aleatorio
turno_jugadores = orden_tirada()

# Índice para seguir al siguiente jugador
turno_actual = 0

# Función para pasar al siguiente jugador
def siguiente_jugador():
    global turno_actual
    turno_actual += 1
    if turno_actual >= len(turno_jugadores):
        print(turno_jugadores)
        turno_actual = 0  # Vuelve al primer jugador cuando llegues al final
    return turno_jugadores[turno_actual]

def comprar_propiedad(jugador, propiedad):
    propiedades_dict = propiedades()  # Diccionario de propiedades disponible en el juego
    if propiedad not in propiedades_dict:
        print(f"La propiedad {propiedad} no existe.")
        return
    
    precio_terreno = propiedades_dict[propiedad]["CMP_Trrny"]
    
    # Verificar si el jugador tiene suficiente dinero para comprar la propiedad
    if jugadors[jugador]["diners"] >= precio_terreno:
        # Realizar la compra
        jugadors[jugador]["diners"] -= precio_terreno
        jugadors[jugador]["Propietats"].append(propiedad)
        print(f"{jugador} ha comprado la propiedad {propiedad} por {precio_terreno}€. Dinero restante: {jugadors[jugador]['diners']}€")
    else:
        print(f"{jugador} no tiene suficiente dinero para comprar la propiedad {propiedad}. Le faltan {precio_terreno - jugadors[jugador]['diners']}€.")

def comprar_casa(jugador, propiedad):
    propiedades_dict = propiedades()  # Diccionario de propiedades disponible en el juego

    # Verificar si el jugador posee la propiedad
    if propiedad not in jugadors[jugador]["Propietats"]:
        print(f"{jugador} no posee {propiedad}, no puede comprar casas.")
        return
    
    # Obtener el precio de una casa en la propiedad
    precio_casa = propiedades()[propiedad]["CMP_Casa"]

    # Verificar si el jugador tiene suficiente dinero
    if jugadors[jugador]["diners"] >= precio_casa:
        # Verificar si ya tiene el máximo de casas permitido (4 casas)
        if propiedades_dict[propiedad]['Num. Cases'] < 4:
            # Comprar una casa
            jugadors[jugador]["diners"] -= precio_casa
            propiedades_dict[propiedad]['Num. Cases'] += 1
            print(f"{jugador} ha comprado una casa en {propiedad}. Ahora tiene {propiedades_dict[propiedad]['Num. Cases']} casas.")
        else:
            print(f"{jugador} ya tiene 4 casas en {propiedad}. Debe comprar un hotel antes de seguir.")
    else:
        print(f"{jugador} no tiene suficiente dinero para comprar una casa en {propiedad}.")

def comprar_hotel(jugador, propiedad):
    propiedades_dict = propiedades()  # Diccionario de propiedades disponible en el juego

    # Verificar si el jugador posee la propiedad
    if propiedad not in jugadors[jugador]["Propietats"]:
        print(f"{jugador} no posee {propiedad}, no puede comprar un hotel.")
        return
    
    # Obtener el precio de un hotel en la propiedad
    precio_hotel = propiedades()[propiedad]["CMP_Hotel"]

    # Verificar si el jugador tiene 4 casas en la propiedad
    if propiedades_dict[propiedad]['Num. Cases'] == 4:
        # Verificar si el jugador tiene suficiente dinero
        if jugadors[jugador]["diners"] >= precio_hotel:
            # Comprar el hotel
            jugadors[jugador]["diners"] -= precio_hotel
            propiedades_dict[propiedad]['Num. Hoteles'] += 1
            propiedades_dict[propiedad]['Num. Cases'] = 0  # Se eliminan las casas al comprar un hotel
            print(f"{jugador} ha comprado un hotel en {propiedad}.")
        else:
            print(f"{jugador} no tiene suficiente dinero para comprar un hotel en {propiedad}.")
    else:
        print(f"{jugador} necesita tener 4 casas en {propiedad} antes de poder comprar un hotel.")

def preus():
    # Datos de las calles
    datos = [
    ("Lauria", 10, 15, 50, 200, 250),
    ("Rosselló", 10, 15, 50, 225, 255),
    ("Marina", 15, 15, 50, 250, 260),
    ("C. de cent", 15, 20, 50, 275, 265),
    ("Muntaner", 20, 20, 60, 300, 270),
    ("Aribau", 20, 20, 60, 325, 275),
    ("Sant Joan", 25, 25, 60, 350, 280),
    ("Aragó", 25, 25, 60, 375, 285),
    ("Urquinaona", 30, 25, 70, 400, 290),
    ("Fontana", 30, 30, 70, 425, 300),
    ("Les Rambles", 35, 30, 70, 450, 310),
    ("Pl. Catalunya", 35, 30, 70, 475, 320),
    ("P. Àngel", 40, 35, 80, 500, 330),
    ("Via Augusta", 40, 35, 80, 525, 340),
    ("Balmes", 50, 40, 80, 550, 350),
    ("Pg. de Gràcia", 50, 50, 80, 525, 360),
    ]

    # Imprimir el encabezado
    print(f"| {'Carrer':<13} | {'Ll. Casa':<9} | {'Ll. Hotel':<10} | {'Cmp. Trrny':<11} | {'Cmp. Casa':<10} | {'Cmp. Hotel':<11} |")
    print(f"|{'-'*15}|{'-'*11}|{'-'*12}|{'-'*13}|{'-'*12}|{'-'*13}|")

    # Imprimir las filas de la tabla
    for carrer, ll_casa, ll_hotel, cmp_trrrny, cmp_casa, cmp_hotel in datos:
        print(f"| {carrer:<13} | {ll_casa:<9} | {ll_hotel:<10} | {cmp_trrrny:<11} | {cmp_casa:<10} | {cmp_hotel:<11} |")

def mostrar_valor_venta_propiedades(jugador):
    total_valor_venta = 0

    # Iterar sobre las propiedades del jugador
    for propiedad in jugadors[jugador]["Propietats"]:
        # Obtener el precio de compra de la propiedad
        precio_compra = propiedades()[propiedad]["Preu"]

        # Calcular el valor de venta al 50%
        valor_venta = precio_compra * 0.5

        # Sumar el valor de venta total
        total_valor_venta += valor_venta

    # Mostrar el resultado en el espacio de información
    print(f"{jugador} podría ganar un total de {total_valor_venta} si vende todas sus propiedades al banco.")

def mostrar_valor_venta_a_jugador(jugador):
        precio_compra = propiedades()[propiedad]["Preu"]
        valor_venta = precio_compra * 0.9
        print(f"Si vende todas sus propiedades a otro jugador, {jugador} ganará {valor_venta}.")

def vender_todas_propiedades_al_banco(jugador):
    total_valor_venta = 0

    for propiedad in jugadors[jugador]["Propietats"]:
        # Obtener el precio de compra de la propiedad
        precio_compra = propiedades()[propiedad]["Preu"]

        # Verificar si la propiedad tiene casas u hoteles y sumar el valor
        casas = jugadors[jugador]["Propietats"][propiedad]["cases"]
        hotels = jugadors[jugador]["Propietats"][propiedad]["hotels"]
        
        # Calcular el costo adicional de las casas y hoteles
        valor_casas = casas * propiedades()[propiedad]["Preu casa"] * 0.5
        valor_hoteles = hotels * propiedades()[propiedad]["Preu hotel"] * 0.5
        
        # Calcular el valor de venta de la propiedad (50% del precio original)
        valor_venta_propiedad = precio_compra * 0.5
        total_valor_venta += valor_venta_propiedad + valor_casas + valor_hoteles

        # Liberar la propiedad, restableciéndola como disponible
        propiedades()[propiedad]["propietari"] = None  # Liberar propiedad
        propiedades()[propiedad]["Num. Cases"] = 0  # Quitar casas
        propiedades()[propiedad]["Num. Hoteles"] = 0  # Quitar hoteles

    # Añadir el total de la venta al dinero del jugador
    jugadors[jugador]["diners"] += total_valor_venta

    # Limpiar las propiedades del jugador
    jugadors[jugador]["Propietats"] = {}

    # Mostrar el resultado en el espacio de información
    print(f"{jugador} ha vendido todas sus propiedades al banco por un total de {total_valor_venta}. Todas las propiedades están ahora disponibles para la compra.")

def menu_opcions(jugador_actual, jugador, propiedad):
    print(f"\nTurno de {jugador_actual}")
    print("""
    Opcions: passar, comprar terreny, comprar casa, comprar hotel, preus, preu banc, preu jugador, vendre al banc, vendre a B, vendre a (T,G o V)
    """)
    opcion = input("Opcion: ").lower()
    
    if opcion == 'passar':
        siguiente_jugador = siguiente_jugador()
        print(siguiente_jugador)

    elif opcion == 'comprar terreny':
        comprar_propiedad(jugador, propiedad)

    elif opcion == 'comprar casa':
        comprar_casa(jugador, propiedad)

    elif opcion == 'comprar hotel':
        comprar_hotel(jugador, propiedad)

    elif opcion == 'preus':
        preus()

    elif opcion == 'preu banc':
        mostrar_valor_venta_propiedades(jugador)

    elif opcion == 'preu jugador':
        mostrar_valor_venta_a_jugador(jugador)

    elif opcion == 'vendre al banc':
        vender_todas_propiedades_al_banco(jugador)
    elif opcion == 'vendre a b':
        pass
    elif opcion == 'Vendre a t' or opcion == 'vendre a g' or opcion == 'vendre a v':
        pass
    elif opcion == 'trucs':
        menu_trucs()
    else:
        print("Error! No existe esta opcion!")
    
def menu_trucs():
    print("""
    <============== Trucs ==============>"
    1.Anar a 'Nom de la casella o carrer'
    2.afegir X cases (on X és un número entre 1 i 4)
    3.afegir X hotels (on X és 1 o bé 2)
    4.seguent X (on X és el proper jugador a jugar, G, T, V o B)
    5.diners X YY (on X és el jugador i YY els diners que tindrà disponibles)
    6.diners X banca (on X són els diners que tindrà la banca)
    """)


taulellDibuixar()

jugador_actual = turno_jugadores[turno_actual]
menu_opcions(jugador_actual, jugadors, propiedad)
print(jugador_actual)

asignar_especial(jugadors)