class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    def ladrar(self):
        print("guau, guau!")
    def __self__(self):
        return "perro {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)
def ladrar():
    print("no tengo perro")