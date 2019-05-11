class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    def ladrar(self):
        if self.peso > 8:
            print("GUAU, GUAU")
        else:
            print("guau, guau!")
    def __self__(self):
        return "perro {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)

class Perroayuda(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
    def __str__(self):
        return "perro de ayuda de {}".format(self.amo)
    def pasear():
        return "ayudo a pasear a mi amo {}".fotmat(self.amo)
    def ladrar():
        if self.__trabajando:
            print("shh, no puedo ladrar")
        else:
            return Perro.ladrar(self)
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor