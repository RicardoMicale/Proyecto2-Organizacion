# Proyecto 2 - Organizacion del computador
from Hashtable import Hashtable
from Piloto import Piloto
from Avion import Avion
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
pilotos = []


hashtable = Hashtable()

def validarNumeros(string):
    for char in string:
        if char in letras:
            return True
    return False

def crearAvion():
    serial = ''
    modelo = ''
    nombre = ''
    #Validacion del serial
    while True:
        serial = input('Ingrese el serial del avion: ')
        if len(serial) > 9:
            print('Serial no valido. Debe tener maximo 9 caracteres, empezando con 1 letra seguida de 8 numeros')
        elif serial[0] not in letras:
            print('El primer caracter del serial debe ser una letra')
        elif validarNumeros(serial):
            print('El primer caracter del serial debe ser una letra')
        elif serial == '':
            print('Serial no valido')
        else:
            break
    
    #Validacion del modelo
    while True:
        modelo = input('Introduzca el modelo del avion: ')
        if len(modelo) > 20:
            print('Modelo no valido, debe tener como maximo 20 caracteres')
        elif modelo == '':
            print('Modelo no valido')
        else:
            break
    
    #Validacion del nombre
    while True:
        nombre = input('Introduzca el nombre del avion: ')
        if len(nombre) > 12:
            print('Nombre no valido. El nombre puede ser de hasta 12 caracteres')
        elif nombre == '':
            print('nombre no valido')
        else:
            break
    
    #Se crea el avion
    avion = Avion(serial, modelo, nombre)
    #Se agrega al hash table
    hashtable.agregar(serial[1:], avion) 

def crearPiloto():
    nombre = ''
    #Validacion del nombre
    while True:
        nombre = input('Ingrese el nombre del piloto: ')
        if len(nombre) > 15:
            print('Nombre muy largo. Introduzca un nombre menor a 15 caracteres')
        elif nombre == '':
            print('Nombre no valido')
        else:
            break
    
    #Se crea el piloto
    piloto = Piloto(nombre)
    #Se agrega a la lista de pilotos
    pilotos.append(piloto)

def registrarPiloto(nombre):
    serial = input('Introduzca el serial completo del avion al que le quiere asignar el piloto: ')
    avion = hashtable.buscar(serial[1:])

    for piloto in pilotos:
        if nombre == piloto.nombre:
            avion.piloto = piloto
            break
    else:
        print('Piloto no encontrado')

def retirarPiloto():
    serial = input('Introduzca el serial completo del avion al que le quiere asignar el piloto: ')
    avion = hashtable.buscar(serial[1:])
    avion.piloto = None

def borrarAvion():
    serial = input('Ingrese el serial completo del avion que quiera borrar: ')
    hashtable.borrar(serial[1:])

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

# def buscarAvionNombre(nombre):
#     '''Busca el avion por nombre'''
#     serial = ''
#     #Se declara serial como string vacio por defecto

#     if nombre == '' or len(nombre) > 12:
#         #Si el nombre no es valido se retorna como string vacio
#         print('Nombre no valido. Ingrese un nombre de maximo 12 caracteres')
#     else:
#         #Se busca el avion segun el nombre y se retorna el serial del avion
#         return

#         # for avion in aviones:
#         #     if nombre == avion.nombre:
#         #         serial = avion.serial
#         #         break

#     return serial

# def buscarAvionModelo(modelo):
#     '''Busca el avion por modelo'''
#     serial = ''
#     #Se declara serial como string vacio por defecto

#     if modelo == '' or len(modelo) > 20:
#         #Si el modelo no es valido se retorna como un string vacio
#         print('Modelo no valido. Ingrese un modelo de maximo 20 caracteres')
#     else:
#         #Se busca el avion segun el modelo y se retorna el serial del avion
#         return
#         # for avion in aviones:
#         #     if modelo == avion.modelo:
#         #         serial = avion.serial
#         #         break

#     return serial
        
