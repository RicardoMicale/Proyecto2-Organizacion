# Proyecto 2 - Organizacion del computador
# Ricardo Micale y Eduardo Curiel
from Hashtable import Hashtable
from Piloto import Piloto
from Avion import Avion
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
aviones = []
todosLosAviones = []

hashtable = Hashtable()

def validarNumeros(string):
    '''Valida los numeros del serial'''
    for char in string:
        if char in letras:
            return True
    return False

def crearAvion():
    '''Crea el objeto avion'''
    serial = ''
    modelo = ''
    nombre = ''
    #Validacion del serial
    while True:
        serial = input('Ingrese el serial del avion: ').title()
        if len(serial) > 9:
            print('Serial no valido. Debe tener maximo 9 caracteres, empezando con 1 letra seguida de 8 numeros')
        elif serial[0].lower() not in letras:
            print('El primer caracter del serial debe ser una letra')
        elif validarNumeros(serial[1:]):
            print('El primer caracter del serial debe ser una letra')
        elif serial == '':
            print('Serial no valido')
        else:
            break
    
    #Validacion del modelo
    while True:
        modelo = input('Introduzca el modelo del avion: ').title()
        if len(modelo) > 20:
            print('Modelo no valido, debe tener como maximo 20 caracteres')
        elif modelo == '':
            print('Modelo no valido')
        else:
            break
    
    #Validacion del nombre
    while True:
        nombre = input('Introduzca el nombre del avion: ').title()
        if len(nombre) > 12:
            print('Nombre no valido. El nombre puede ser de hasta 12 caracteres')
        elif nombre == '':
            print('nombre no valido')
        else:
            break
    
    #Se crea el avion
    avion = Avion(serial, modelo, nombre)
    #Se agrega al hash table
    hashtable.agregar(int(serial[1:]), avion)
    return Avion(serial, modelo, nombre)

def crearPiloto():
    '''Crea el objeto piloto'''
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
    return piloto

def registrarPiloto():
    '''Registra el piloto en el avion'''
    serial = input('Introduzca el serial completo del avion al que le quiere asignar el piloto: ')
    if serial == '' or len(serial) > 9 or type(serial[0]) != str:
        #Si no es valido, retorna none
        print('Serial no valido. Ingrese un serial de maximo 9 caracteres donde el primero sea una letra')
        return None
    avion = hashtable.buscar(int(serial[1:]))
    avion.piloto = crearPiloto()

def retirarPiloto():
    '''Elimina el piloto del avion'''
    serial = input('Introduzca el serial completo del avion al que le quiere retirar el piloto: ')
    if serial == '' or len(serial) > 9 or type(serial[0]) != str:
        #Si no es valido, retorna none
        print('Serial no valido. Ingrese un serial de maximo 9 caracteres donde el primero sea una letra')
        return None
    avion = hashtable.buscar(int(serial[1:]))
    avion.piloto = None

def borrarAvion():
    '''Borra el avion de la base de datos'''
    serial = input('Ingrese el serial completo del avion que quiera borrar: ')
    hashtable.borrar(int(serial[1:]))

def buscarAvionSerial():
    '''Busca el avion por serial'''
    serial = input('Introduzca el serial completo del avion que quiere buscar: ')
    if serial == '' or len(serial) > 9 or type(serial[0]) != str:
        #Si no es valido, retorna none
        print('Serial no valido. Ingrese un serial de maximo 9 caracteres donde el primero sea una letra')
        return None
    else:
        #De lo contrario se busca el avion
        avion = hashtable.buscar(int(serial[1:]))
        if avion != None:
            return avion.infoAvion()
        else:
            print('Avion no encontrado')

def conversionBinaria(string):
    '''Convierte strings a codigo binario y despues a integers'''
    binario = ''.join(format(i, '08b') for i in bytearray(string, encoding='utf8'))
    print(binario)
    numero = int(binario, 2)
    print(numero)
    return numero

def buscarAvionNombre(aviones):
    '''Busca el avion por nombre'''
    nombre = input('Introduzca el nombre del avion que quiere buscar: ').title()
    serial = ''
    if nombre == '' or len(nombre) > 12:
        #Si no es valido, retorna none
        print('Nombre no valido. Ingrese un Nombre de maximo 12 caracteres.')
        return None
    else:
        # infoAviones = aviones
        #De lo contrario se busca el avion
        llave = conversionBinaria(nombre)
        # for x in aviones:
        #     infoAviones = [x[0], x[2]]
        #     if llave in infoAviones:
        #         serial = x[0]

        serial = busquedaBinaria(llave, 2)
        avion = hashtable.buscar(int(serial[1:]))

        if avion != None:
            return avion.infoAvion()
        else:
            print('Avion no encontrado')

        # avion = hashtable.buscar(int(serial[1:]))
        # if avion != None:
        #     return avion.infoAvion()
        # else:
        #     print('Avion no encontrado')

def buscarAvionModelo(aviones):
    '''Busca el avion por Modelo'''
    modelo = input('Introduzca el Modelo del avion que quiere buscar: ').title()
    serial = ''
    if modelo == '' or len(modelo) > 20:
        #Si no es valido, retorna none
        print('Modelo no valido. Ingrese un Nombre de maximo 12 caracteres.')
        return None
    else:
        # infoAviones = aviones
        #De lo contrario se busca el avion
        llave = conversionBinaria(modelo)
        # for x in aviones:
        #     infoAviones = [x[0], x[1]]
        #     if llave in infoAviones:
        #         serial = x[0]
        serial = busquedaBinaria(llave, 1)
        avion = hashtable.buscar(int(serial[1:]))

        if avion != None:
            return avion.infoAvion()
        else:
            print('Avion no encontrado')

        # if avion != None:
        #     return avion.infoAvion()
        # else:
        #     print('Avion no encontrado')


#Leer archivo de texto
def leerTxt():
    datos = [] #Lista para los datos del archivo de texto
    with open('datos.txt', 'r') as f: #Se guardan las lineas del txt como sublistas con cada dato del avion
        lista = f.read().splitlines() 
        for line in lista:
            datosAvion = line.split('-')
            datos.append(datosAvion)
            todosLosAviones.append(datosAvion)
            # Guarda los datos del txt en la lista para las busquedas
            datosAvion2 = line.split('-')
            datosAvion2[1] = conversionBinaria(datosAvion2[1])
            datosAvion2[2] = conversionBinaria(datosAvion2[2])
            aviones.append(datosAvion2)
    
    for i in range(len(datos)):
        sublista = datos[i]
        avion = Avion(sublista[0], sublista[1], sublista[2])
        hashtable.agregar(int(avion.serial[1:]), avion)

def busquedaBinaria(llave, indice):
    primero = 0
    ultimo = len(aviones) - 1
    encontrado = False

    while not encontrado and primero <= ultimo:
        mitad = (primero + ultimo) // 2
        listaMedio = aviones[mitad]
        valorMedio = listaMedio[indice]
        if llave in listaMedio:
            encontrado = True
            return listaMedio[0]
        else:
            if llave < valorMedio:
                ultimo = mitad - 1
            else:
                primero = mitad + 1
    
    return None

# MENU 
def main():
    leerTxt()
    avionTemp = []
    while True:
        opcion = input("\n\t\tBienvenido a Aviocc Airlines!\n1. Inserción de un Nuevo Avión.\n2. Búsqueda de un Avión.\n3. Asignación de Piloto a un Avión Libre.\n4. Liberación de un Avión.\n5. Eliminación de un Avión.\n6. Salir.\n")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        # Prueba para ver la lista de aviones agregados
        print(aviones)
        # PRIMERA OPCION (CREACION AVION)
        if opcion == "1":
            while True:
                opcion = input("\t\tInserción de un Nuevo Avión\n1. Crear Avión.\n2. Salir.\n")
                print("------------------------------------------------------------------------------------------------------------------------------------")
                if opcion =="1":
                    # FUNCION PARA CREAR AVION
                    print("Entraste para crear un nuevo avion!")
                    print("------------------------------------------------------------------------------------------------------------------------------------")
                    avionTemp = crearAvion()
                    aviones.extend([[avionTemp.serial,conversionBinaria(avionTemp.modelo),conversionBinaria(avionTemp.nombre)]])
                elif opcion == "2":
                    # SALIR AL MENU NUEVAMENTE
                    break
                else:
                    # ERROR SI SE INGRESA OTRA OPCION
                    print("ERROR.Ingrese una opcion valida.")
                    print("------------------------------------------------------------------------------------------------------------------------------------")
        # SEGUNDA OPCION (BUSQUEDA)
        elif opcion == "2":
            while True:
                opcion = input("\t\tBúsqueda de un Avión\n1. Búsqueda por Serial.\n2. Búsqueda por Modelo.\n3. Búsqueda por Nombre.\n4. Salir.\n")
                print("------------------------------------------------------------------------------------------------------------------------------------")
                if opcion =="1":
                    # FUNCION PARA BUSCAR POR SERIAL
                    print("Entraste a buscar por Serial!")
                    print("------------------------------------------------------------------------------------------------------------------------------------")
                    buscarAvionSerial()
                elif opcion == "2":
                    # FUNCION PARA BUSCAR POR MODELO
                    print("Entraste a buscar por Modelo!")
                    print("------------------------------------------------------------------------------------------------------------------------------------")
                    buscarAvionModelo(aviones)
                elif opcion == "3":
                    # FUNCION PARA BUSCAR POR NOMBRE
                    print("Entraste a buscar por Nombre!")
                    print("------------------------------------------------------------------------------------------------------------------------------------")
                    buscarAvionNombre(aviones)
                elif opcion == "4":
                    # SALIR AL MENU NUEVAMENTE
                    break
                else:
                    # ERROR SI SE INGRESA OTRA OPCION
                    print("ERROR.Ingrese una opcion valida.")
                    print("------------------------------------------------------------------------------------------------------------------------------------")
        # TERCERA OPCION (ASIGNACION DE PILOTO)
        elif opcion == "3":
            while True:
                opcion = input("\t\tAsignación de Piloto a un Avión Libre\n1. Agregar Piloto.\n2. Salir.\n")
                print("------------------------------------------------------------------------------------------------------------------------------------")
                if opcion == "1":
                    # FUNCION PARA LLENAR EL CAMPO PILOTO DE UN AVION BUSCANDOLOS POR SERIAL,MODELO O NOMBRE
                    # IDEA --> IMPRIMIR UNA LISTA DE LOS AVIONES CON EL CAMPO PILOTO VACIO LUEGO SE SELECCIONA EL AVION QUE SE DESEE   
                    print("Entraste a asignar un piloto!")
                    print("------------------------------------------------------------------------------------------------------------------------------------")     
                    registrarPiloto()
                elif opcion == "2":
                    break
                else:
                    print("ERROR.Ingrese una opcion valida.")
                    print("------------------------------------------------------------------------------------------------------------------------------------")
        # CUARTA OPCION (LIBERACION DE AVION "ELIMINAR CAMPO PILOTO")
        elif opcion == "4":
            while True:
                opcion = input("\t\tLiberación un Avión\n1. Liberar Avión.\n2. Salir.\n")
                print("------------------------------------------------------------------------------------------------------------------------------------")
                if opcion == "1":
                    # FUNCION PARA VACIAR EL CAMPO PILOTO DE UN AVION.
                    # IDEA --> IMPRIMIR UNA LISTA DE LOS AVIONES CON EL CAMPO PILOTO LLENO LUEGO SE SELECCIONA EL AVION QUE SE DESEE Y SE LIMPIA ESE ESPACIO 
                    print("Entraste a Liberar un Avión!")  
                    print("------------------------------------------------------------------------------------------------------------------------------------")    
                    retirarPiloto()
                elif opcion == "2":
                    break
                else:
                    print("ERROR.Ingrese una opcion valida.")
                    print("------------------------------------------------------------------------------------------------------------------------------------")
        # QUINTA OPCION (ELIMINAR AVION)
        elif opcion == "5":
            while True:
                opcion = input("\t\tEliminación de un Avión\n1. Eliminar Avión.\n2. Salir.\n")
                print("------------------------------------------------------------------------------------------------------------------------------------")
                if opcion == "1":
                    # FUNCION PARA ELIMINAR UN AVION.
                    # IDEA --> IMPRIMIR UNA LISTA DE LOS AVIONES CON EL CAMPO PILOTO LLENO LUEGO SE SELECCIONA EL AVION QUE SE DESEE Y SE LIMPIA ESE ESPACIO 
                    print("Entraste a Eliminar Avión!")
                    print("------------------------------------------------------------------------------------------------------------------------------------")      
                    borrarAvion()
                elif opcion == "2":
                    break
                else:
                    print("ERROR.Ingrese una opcion valida.")
                    print("------------------------------------------------------------------------------------------------------------------------------------")
        # SEXTA OPCION SALIR DEL PROGRAMA
        elif opcion == "6":
            print("Gracias, Vuelva pronto!")
            print("------------------------------------------------------------------------------------------------------------------------------------")
            break
        # ERROR SI SE INGRESA OTRA OPCION
        else:
            print("ERROR.Ingrese una opcion valida.")
            print("------------------------------------------------------------------------------------------------------------------------------------")

main()

