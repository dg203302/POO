class fecha:
    __fec_part: str
    __id_eq_local: str
    __id_eq_visit: str
    __cant_gol_loc: int
    __cant_gol_visit: int
    def __init__(self, fech, idloc,idvisit,cantgoll,cantgolv):
        self.__fec_part=fech
        self.__id_eq_local=idloc
        self.__id_eq_visit=idvisit
        self.__cant_gol_loc=cantgoll
        self.__cant_gol_visit=cantgolv
    def getidvisi(self):
        return self.__id_eq_visit
    def getidloc(self):
        return self.__id_eq_local
    def getidvisi(self):
        return self.__id_eq_visit
    def getcantgolloc(self):
        return self.__cant_gol_loc
    def getcantgolvis(self):
        return self.__cant_gol_visit
    def __del__(self):
        print('fecha borrada!')