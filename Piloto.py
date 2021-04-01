class Piloto():
    def __init__(self, nombre):
        self.nombre = nombre
        self.tieneAvion = False

    def asignarAvion(self):
        #Declara que el piloto tiene un avion asignado
        self.tieneAvion = True

    def quitarAvion(self):
        #Declara que el piloto ya no tiene el avion asignado
        self.tieneAvion = False

    def getInfo(self):
        return self.nombre