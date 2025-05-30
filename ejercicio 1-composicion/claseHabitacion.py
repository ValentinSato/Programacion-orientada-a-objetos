class Habitacion:
    __numero: int
    __piso: int
    __tipo:str
    __precioxnoche: float
    __disponibilidad: bool

    def __init__(self,n,p,t,pxn,d):
        self.__numero = n
        self.__piso = p
        self.__tipo = t
        self.__precioxnoche = pxn
        self.__disponibilidad = d

    def setDisponibilidad(self, disp):
        self.__disponibilidad = disp

    def getNumero(self):
        return self.__numero
    
    def getPiso(self):
        return self.__piso
    
    def getTipo(self):
        return self.__tipo
    
    def getPrecioxnoche(self):
        return self.__precioxnoche
     
    def getDisp(self):
        return self.__disponibilidad
    
    
                       
        