class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = self.actualizar_humor()
        self.esta_vivo = True

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nivel de energía: {self.nivel_energia}")
        print(f"Nivel de hambre: {self.nivel_hambre}")
        print(f"Nivel de felicidad: {self.nivel_felicidad}")
        print(f"Humor: {self.humor}")
        print(f"Está vivo: {'Sí' if self.esta_vivo else 'No'}")

    def alimentar(self):
        if self.esta_vivo:
            self.nivel_hambre = max(0, self.nivel_hambre - 10)
            self.nivel_energia = max(0, self.nivel_energia - 15)
            self.verificar_estado()

    def jugar(self):
        if self.esta_vivo:
            self.nivel_felicidad = min(100, self.nivel_felicidad + 20)
            self.nivel_energia = max(0, self.nivel_energia - 18)
            self.nivel_hambre = min(100, self.nivel_hambre + 10)
            self.verificar_estado()

    def dormir(self):
        if self.esta_vivo:
            self.nivel_energia = min(100, self.nivel_energia + 40)
            self.nivel_hambre = min(100, self.nivel_hambre + 5)
            self.verificar_estado()

    def verificar_estado(self):
        if self.nivel_energia <= 0:
            self.esta_vivo = False
            print(f"{self.nombre} ha muerto.")
            return
        if self.nivel_hambre >= 20:
            self.nivel_energia = max(0, self.nivel_energia - 20)
            self.nivel_felicidad = max(0, self.nivel_felicidad - 30)
        self.humor = self.actualizar_humor()

    def actualizar_humor(self):
        if self.nivel_felicidad < 10:
            return 'enojado'
        elif 10 <= self.nivel_felicidad < 30:
            return 'triste'
        elif 30 <= self.nivel_felicidad < 70:
            return 'indiferente'
        elif 70 <= self.nivel_felicidad < 90:
            return 'feliz'
        else:
            return 'eufórico'