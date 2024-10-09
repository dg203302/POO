#-----------------------------------------COLUMNAS-----------------------------------------#
class sub_lista:
    __items_columnas: list
    __cantidad_columnas: int
    __tamano_columnas: int
    def __init__(self, tamano_columnas):
        self.__items_columnas = [None] * tamano_columnas
        self.__cantidad_columnas = 0
        self.__tamano_columnas = tamano_columnas
    def verificar(self):
        return self.__cantidad_columnas == self.__tamano_columnas
    def cargar(self, valor):
        if self.verificar():
            print('columna llena')
            return
        else:
            self.__items_columnas[self.__cantidad_columnas] = valor
            self.__cantidad_columnas += 1
    def get_item(self, indice):
        return self.__items_columnas[indice]
    def get_cantidad(self):
        return self.__cantidad_columnas
#-----------------------------------------FILAS-----------------------------------------#
#agregar area de overflow
class hash_bucket:
    __items_filas: list
    __tamano_filas: int
    __cantidad_filas: int

    def __init__(self, tamano_filas, tamano_columnas):
        self.__items_filas = [sub_lista(tamano_columnas) for _ in range(tamano_filas)]
        self.__tamano_filas = tamano_filas
        self.__cantidad_filas = 0

    def hasheo_modulo(self, clave):
        return clave % self.__tamano_filas

    def insertar(self, valor):
        if self.__tamano_filas == self.__cantidad_filas:
            print('Tabla llena')
            return
        else:
            indice = self.hasheo_modulo(valor)
            if self.__items_filas[indice].verificar():
                print('columna llena')
                return
            else:
                self.__items_filas[indice].cargar(valor)
                self.__cantidad_filas += 1

    def buscar(self, valor):
        indice = self.hasheo_modulo(valor)
        i = 0
        while i < self.__items_filas[indice].get_cantidad() and self.__items_filas[indice].get_item(i) != valor:
            i += 1
        if i == self.__items_filas[indice].get_cantidad():
            return False
        else:
            return True

    def recorrer(self):
        for i in range(self.__tamano_filas):
            cadena = '['
            for j in range(self.__items_filas[i].get_cantidad()):
                cadena += str(self.__items_filas[i].get_item(j)) + ','
            cadena = cadena.rstrip(',') + ']'
            print(f'{i} --> {cadena}')
#---------------------------------------------MAIN---------------------------------------------#
if __name__=='__main__':
    hasheo_bucket=hash_bucket(2,2)  #cambiar esto
    #caculo dimension+columnas + porcentaje overflow, rehacer todo
    hasheo_bucket.insertar(10)
    hasheo_bucket.insertar(20)
    hasheo_bucket.insertar(30)
    hasheo_bucket.recorrer()