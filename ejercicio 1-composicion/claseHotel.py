from claseHabitacion import Habitacion

class Hotel:
    __nombre: str
    __dire:str
    __tel:str
    __listaHabitaciones: list

    def __init__(self,n,d,t):
        self.__nombre = n
        self.__dire = d
        self.__tel = t
        self.__listaHabitaciones = []

    def agregarHabitacion(self,nro,piso,tipo,precioxnoche,disponibilidad):
        unahabitacion = Habitacion(nro,piso,tipo,precioxnoche,disponibilidad)
        self.__listaHabitaciones.append(unahabitacion)
        

    def __del__(self):
        print("Liberando una habitacion")
        

    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__dire
    def getTelefono(self):
        return self.__tel
    def getLista(self):
        return self.__listaHabitaciones
   
        