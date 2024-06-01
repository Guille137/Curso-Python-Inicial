import random


numero = random.randint(1,20)
for i in range(5):
    adivina = int(input("Adivina el numero entre 1 y 20: "))
    if i == 4 and adivina != numero: print("Perdiste, el numero era: ",numero)
    elif adivina == numero:
        print("Felicidades, acertaste")
        
    elif adivina < 1 or adivina > 20:
        print("El numero debe estar entre 1 y 20")
    elif adivina < numero:
        print("El numero es mayor")
    elif adivina > numero:
        print("El numero es menor")
    else:
        continue
input("Presione Enter para cerrar el programa.")
