# Proyecto 2 - Organizacion del computador
from Hashtable import Hashtable
from Piloto import Piloto
from Avion import Avion

hashtable = Hashtable()

def buscarAvionSerial(serial):
    '''Busca el avion por serial'''
    if serial == '' or len(serial) > 9 or type(serial[0]) != str:
        #Si no es valido, retorna none
        print('Serial no valido. Ingrese un serial de maximo 9 caracteres donde el primero sea una letra')
        return None
    else:
        #De lo contrario se busca el avion
        avion = hashtable.buscar(serial)
        return avion

def buscarAvionNombre(nombre):
    '''Busca el avion por nombre'''
    serial = ''
    #Se declara serial como string vacio por defecto

    if nombre == '' or len(nombre) > 12:
        #Si el nombre no es valido se retorna como string vacio
        print('Nombre no valido. Ingrese un nombre de maximo 12 caracteres')
    else:
        #Se busca el avion segun el nombre y se retorna el serial del avion
        return

        # for avion in aviones:
        #     if nombre == avion.nombre:
        #         serial = avion.serial
        #         break

    return serial

def buscarAvionModelo(modelo):
    '''Busca el avion por modelo'''
    serial = ''
    #Se declara serial como string vacio por defecto

    if modelo == '' or len(modelo) > 20:
        #Si el modelo no es valido se retorna como un string vacio
        print('Modelo no valido. Ingrese un modelo de maximo 20 caracteres')
    else:
        #Se busca el avion segun el modelo y se retorna el serial del avion
        return
        # for avion in aviones:
        #     if modelo == avion.modelo:
        #         serial = avion.serial
        #         break

    return serial
        
