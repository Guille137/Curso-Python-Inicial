import random

def obtener_jugada_maquina():
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

def determinar_ganador(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (jugador == "piedra" and maquina == "tijeras") or \
         (jugador == "papel" and maquina == "piedra") or \
         (jugador == "tijeras" and maquina == "papel"):
        return "Jugador gana"
    else:
        return "Máquina gana"

def jugar():
    while True:
        jugada_jugador = input("Ingresa tu jugada (piedra, papel, tijeras): ").lower()
        if jugada_jugador not in ["piedra", "papel", "tijeras"]:
            print("Jugada no válida. Inténtalo de nuevo.")
            continue

        jugada_maquina = obtener_jugada_maquina()
        print(f'La máquina eligió: {jugada_maquina}')
        resultado = determinar_ganador(jugada_jugador, jugada_maquina)
        print(f'El resultado es: {resultado}')

        jugar_de_nuevo = input('¿Quieres jugar de nuevo? (s/n): ').lower()
        if jugar_de_nuevo != 's':
            break

if __name__ == '__main__':
    jugar()