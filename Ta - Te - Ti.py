def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 10)

def movimiento_valido(tablero, fila, columna):
    return tablero[fila][columna] == " "

def actualizar_tablero(tablero, fila, columna, jugador):
    tablero[fila][columna] = jugador

def hay_ganador(tablero, jugador):
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True
    for col in range(3):
        if tablero[0][col] == jugador and tablero[1][col] == jugador and tablero[2][col] == jugador:
            return True
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    return False

def juego_empatado(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

def jugar_tateti():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    while True:
        imprimir_tablero(tablero)
        try:
            fila = int(input(f"Jugador {jugador_actual}, elige una fila (0-2): "))
            columna = int(input(f"Jugador {jugador_actual}, elige una columna (0-2): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        if not (0 <= fila <= 2 and 0 <= columna <= 2):
            print("Posición fuera del rango. Intenta de nuevo.")
            continue
        if not movimiento_valido(tablero, fila, columna):
            print("Esta posición ya está ocupada. Intenta de nuevo.")
            continue
        actualizar_tablero(tablero, fila, columna, jugador_actual)
        if hay_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Jugador {jugador_actual} ha ganado!")
            break
        if juego_empatado(tablero):
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            break
        jugador_actual = "O" if jugador_actual == "X" else "X"

if __name__ == "__main__":
    jugar_tateti()
