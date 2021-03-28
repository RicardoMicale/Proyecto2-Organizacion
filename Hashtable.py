class Hashtable():
    def __init__(self, length=3):
        self.lista = [None] * length #Inicia el hashtable vacio

    def hash(self, llave):
        '''Busca el indice de la llave en la lista'''
        length = len(self.lista)
        return hash(llave) % length
    
    def agregar(self, llave, valor):
        '''Agrega elementos a la tabla'''
        indice = self.hash(llave)
        if self.lista[indice] is not None:
            #En este indice ya hay elementos, hasta un maximo de dos aviones
            for kvp in self.lista[indice]:
                #Busca la llave para actualizar la informacion con el nuevo valor
                if kvp[0] == llave:
                    kvp[1] = valor
                    break
            #De lo contrario entra en esta condicion para agregar la llave nueva con su valor
            else:
                self.lista[indice].append([llave, valor])
        
        else:
            #Se inicializa la lista como vacia en ese indice
            self.lista[indice] = []
            #Se agrega el valor con su llave en la lista vacia
            self.lista[indice].append([llave, valor])

    def get(self, llave):
        '''Busca elementos en la tabla segun la llave'''
        indice = self.hash(llave)
        if self.lista[indice] is None:
            #En este caso la lista esta llena de valores None 
            print('No hay datos en la tabla')
            raise KeyError()
        else:
            #En el caso contrario se recorren los pares llave-valor
            for kvp in self.lista[indice]:
                if kvp[0] == llave:
                    #Si se encuentra la llave retorna el valor
                    return kvp[1]
            #De lo contrario se muestra un mensaje de error
            print('No se encontraron los datos')
            raise KeyError()

    def isFull(self):
        '''Revisa si es necesario expandir la tabla'''
        if len(self.lista) == 9:
            #El registro de aviones permite 3 grupos de 2 aviones como
            #capacidad regular y tiene 6 grupos extra por si hay un overflow
            #Al llegar a esa capacidad se muestra un mensaje de error
            print('Capacidad maxima alcanzada')
            return None

        items = 0
        #Variable para contar la cantidad de pares llave-valor en la tabla
        for item in self.lista:
            if item is not None:
                items += 1
        
        #Retorna un booleano dependiendo de que tan llena esta la tabla
        #True si es mayor que la mitad, False si es menor
        return items == len(self.lista)

    def doblar(self):
        '''Dobla el tamaño de la lista'''
        hashtable2 = Hashtable(length=len(self.lista) * 2)

        for i in range(len(self.lista)):
            if self.lista[i] is None:
                continue

            #Al ser una lista de mayor longitud hay que volver a agregar los pares
            #Para que tengan el valor correcto de la llave
            for kpv in self.lista[i]:
                hashtable2.agregar(kpv[0], kpv[1])

        #Se reemplaza la lista de la tabla actual por la de la 
        #lista actualizada
        self.lista = hashtable2.lista

                