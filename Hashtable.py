class Hashtable():
#     def __init__(self, length=3):
#         self.lista = [None] * length #Inicia el hashtable vacio

#     def hash(self, llave):
#         '''Busca el indice de la llave en la lista'''
#         length = len(self.lista)
#         return hash(llave) % length
    
#     def agregar(self, llave, valor):
#         '''Agrega elementos a la tabla'''
#         indice = self.hash(llave)
#         if self.lista[indice] is not None:
#             #En este indice ya hay elementos, hasta un maximo de dos aviones
#             for kvp in self.lista[indice]:
#                 #Busca la llave para actualizar la informacion con el nuevo valor
#                 if kvp[0] == llave:
#                     kvp[1] = valor
#                     break
#             #De lo contrario entra en esta condicion para agregar la llave nueva con su valor
#             else:
#                 self.lista[indice].append([llave, valor])
        
#         else:
#             #Se inicializa la lista como vacia en ese indice
#             self.lista[indice] = []
#             #Se agrega el valor con su llave en la lista vacia
#             self.lista[indice].append([llave, valor])

#     def get(self, llave):
#         '''Busca elementos en la tabla segun la llave'''
#         indice = self.hash(llave)
#         if self.lista[indice] is None:
#             #En este caso la lista esta llena de valores None 
#             print('No hay datos en la tabla')
#             raise KeyError()
#         else:
#             #En el caso contrario se recorren los pares llave-valor
#             for kvp in self.lista[indice]:
#                 if kvp[0] == llave:
#                     #Si se encuentra la llave retorna el valor
#                     return kvp[1]
#             #De lo contrario se muestra un mensaje de error
#             print('No se encontraron los datos')
#             raise KeyError()

#     def isFull(self):
#         '''Revisa si es necesario expandir la tabla'''
#         if len(self.lista) == 9:
#             #El registro de aviones permite 3 grupos de 2 aviones como
#             #capacidad regular y tiene 6 grupos extra por si hay un overflow
#             #Al llegar a esa capacidad se muestra un mensaje de error
#             print('Capacidad maxima alcanzada')
#             return None

#         items = 0
#         #Variable para contar la cantidad de pares llave-valor en la tabla
#         for item in self.lista:
#             if item is not None:
#                 items += 1
        
#         #Retorna un booleano dependiendo de que tan llena esta la tabla
#         #True si es mayor que la mitad, False si es menor
#         return items == len(self.lista)

#     def agrandar(self):
#         '''Agranda el tamaño de la lista'''
#         hashtable2 = Hashtable(length=len(self.lista) + 1)

#         for i in range(len(self.lista)):
#             if self.lista[i] is None:
#                 continue

#             #Al ser una lista de mayor longitud hay que volver a agregar los pares
#             #Para que tengan el valor correcto de la llave
#             for kpv in self.lista[i]:
#                 hashtable2.agregar(kpv[0], kpv[1])

#         #Se reemplaza la lista de la tabla actual por la de la 
#         #lista actualizada
#         self.lista = hashtable2.lista

    def __init__(self, length=3):
        #Se crea una lista de listas, cada sublista representa un grupo
        self.lista = [[]] * length 

    def hash(self, llave):
        return llave % len(Hashtable) #Se hace una funcion hash con el modulo entre la llave y la longitud de la lista  

    def agregar(self, llave, valor):
        #Se define el indice como el valor de la funcion hash
        indice = hash(llave)
        #El kvp (Key Value Pair) se define como una tupla cuyos valores son la llave y el valor que representa
        kvp = (llave, valor)
        if len(self.lista[indice]) < 6: 
            #Si ya hay 6 tuplas en la sublista (2 aviones + 4 aviones del overflow)
            #se muestra un mensaje de error
            self.lista[indice].append(kvp)
        else:
            print('Limite de aviones agregados en este grupo debe eliminar uno para seguir agragando')

    def buscar(self, llave):
        if len(self.lista) != 0:
            #Si la longitud de la lista es distinto de cero, se procede a la busqueda
            indice = hash(llave)
            if len(self.lista[indice]) == 0:
                #Si la longitud de la sublista es 0 quiere decir que no hay aviones registrados
                #en ese indice de la tabla
                print('No se encontraron los datos')
                return None
            else:
                #Si hay elementos en la sublista, se recorre
                # esta en busqueda de la llave dentro de las tuplas
                sublista = self.lista[indice]
                
                for i in range(len(sublista)):
                    tupla = sublista[i]
                    if llave == tupla[0]:
                        return tupla[1] 
                #Si no se encuentra el avion qioere decir que no esta registrado
                else:
                    print('No existe el avion')
        else:
            #Si la longitud es cero, quiere decir que la base esta vacia
            print('La base de datos esta vacia')
