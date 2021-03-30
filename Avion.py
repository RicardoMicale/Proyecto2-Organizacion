class Avion():
    def __init__(self, serial, modelo, nombre, piloto=None):
        self.serial = serial
        self.modelo = modelo
        self.nombre = nombre
        self.piloto = piloto

    def agregarPiloto(self, piloto):
        self.piloto = piloto

    def borrarPiloto(self):
        self.piloto = None
    
    def infoAvion(self):
        print(
            'Serial del avion: {}\n Modelo del avion: {}\n Nombre del avion: {}\n'
            .format(self.serial, self.modelo, self.nombre)
        )
        if self.piloto != None:
            print('Piloto: ' + self.piloto.getInfo())