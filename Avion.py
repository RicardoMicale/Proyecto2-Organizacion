class Avion():
    def __init__(self, serial, modelo, nombre, piloto="No tiene Piloto"):
        self.serial = serial
        self.modelo = modelo
        self.nombre = nombre
        self.piloto = piloto

    def agregarPiloto(self, piloto):
        self.piloto = piloto

    def borrarPiloto(self):
        self.piloto = "No tiene Piloto"
    
    def infoAvion(self):
        print(
            'Serial del avion: {}\nModelo del avion: {}\nNombre del avion: {}\n'
            .format(self.serial, self.modelo, self.nombre)
        )
        if self.piloto != "No tiene Piloto":
            print('Piloto: ' + self.piloto + '\n')