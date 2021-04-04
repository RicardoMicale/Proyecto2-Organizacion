class Hashtable():

    def __init__(self, length=3):
        #Se crea una lista de listas, cada sublista representa un grupo
        self.length = length
        self.lista = [[] for _ in range(length)] 

    def hashFunc(self, llave):
        indice = llave % self.length
        return indice #Se hace una funcion hash con el modulo entre la llave y la longitud de la lista  

    def agregar(self, llave, valor):
        #Se define el indice como el valor de la funcion hash
        indice = self.hashFunc(llave)
        #El kvp (Key Value Pair) se define como una tupla cuyos valores son la llave y el valor que representa
        kvp = (llave, valor)
        if len(self.lista[indice]) < 14: 
            #Si ya hay 6 tuplas en la sublista (2 aviones + 12 aviones del overflow)
            #se muestra un mensaje de error
            self.lista[indice].append(kvp)
        else:
            print('Limite de aviones agregados en este grupo debe eliminar uno para seguir agragando')

    def buscar(self, llave):
        if len(self.lista) != 0:
            #Si la longitud de la lista es distinto de cero, se procede a la busqueda
            indice = self.hashFunc(llave)
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

    def borrar(self, llave):
        if len(self.lista) != 0:
            #Si la longitud de la lista es distinto de cero, se procede a la busqueda
            indice = self.hashFunc(llave)
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
                        sublista.remove(tupla)
                        break
                #Si no se encuentra el avion qioere decir que no esta registrado
                else:
                    print('No existe el avion')
        else:
            #Si la longitud es cero, quiere decir que la base esta vacia
            print('La base de datos esta vacia')
