from personal import *
class personalapoyo(personal):
    __categoria:str
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria,carrera='', cargo='', catedra='', area_investigacion='', tipo_investigacion='', categoria_incentivos='', importe_extra=''):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, categoria, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        self.__categoria=categoria
    def tojson(self):
        d=dict(tipo=__class__.__name__,datos=dict(cuil=self._personal__cuil, apellido=self._personal__ape, nombre=self._personal__nom, sueldo_basico=self._personal__sueld_bas, antiguedad=self._personal__antig,categoria=self.__categoria))
        return d