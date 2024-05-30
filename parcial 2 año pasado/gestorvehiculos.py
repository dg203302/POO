from nodo import *
from pasajeros import *
from carga import *
class gestorvehiculos:
    __cab=nodo
    __act=nodo
    __indi=int
    __tope=int
    def __init__(self,cab=None,act=None,indi=0,tope=0):
        self.__cab=cab
        self.__act=act
        self.__indi=indi
        self.__tope=tope
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indi==self.__tope:
            self.__act=self.__cab
            self.__indi=0
            raise StopIteration
        else:
            self.__indi+=1
            dat=self.__act.getdat()
            self.__act=self.__act.getsig()
            return dat
    def agreg(self,obje): #inciso a
        nueno=nodo(obje)
        if self.__cab==None:
            self.__cab=nueno
            self.__act=nueno
            self.__tope+=1
        else:
            nodau=self.__act
            while nodau.getsig()!=None:
                nodau=nodau.getsig()
            if nodau.getsig()==None:
                nodau.actsig(nueno)
                self.__tope+=1
    def b(self):
        for vehi in self:
            if isinstance(vehi,pasajeros) and vehi.getcantasient()>6:
                print(vehi)
    def c(self):
        marc=input('ingrese una marca para ver: ')
        c=0
        for vehi in self:
            if isinstance(vehi,carga) and vehi.getmarca()==marc:
                c+=1
        print(f'vehiculos de esa marca: {c}')
    def d(self):
        print('MARCA   MODELO   TIPO DE VEHICULO   KILOMETROS A RECORRER   TOTAL ALQUILER')
        for vehi in self:
            print(f'{vehi.getmarca()}   {vehi.getmodelo()}   {type(vehi).__name__}#importante!!!!!!   {vehi.getkm()}   {vehi.getimportealquiler()}')