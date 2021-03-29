# Proyecto 2 - Organizacion del computador
from Hashtable import Hashtable
from Piloto import Piloto
from Avion import Avion

hashtable = Hashtable()

def buscarAvionSerial(serial):
    if serial == '':
        print('No existe el avion')
    elif len(serial) > 8:
        print('Serial no valido. Ingrese un serial de maximo 8 caracteres')

    avion = hashtable.get(serial)
    return avion

def buscarAvionNombre(nombre):
    serial = ''

    # for avion in aviones:
    #     if nombre == avion.nombre:
    #         serial = avion.serial
    #         break
    
    return serial

def buscarAvionModelo(modelo):
    return
