from claseHotel import Hotel
import csv

class gestorH:
    __listaH: list

    def __init__(self):
        self.__listaH = []
    
    def agregarHotel(self,unhotel):
        self.__listaH.append(unhotel)

    def test(self):
        i = -1
        archivo = open("Hoteles.csv")
        reader = csv.reader(archivo, delimiter=";")
        
        for fila in reader:
            if len(fila) == 3:
                unhotel = Hotel(fila[0],fila[1],fila[2])
                self.agregarHotel(unhotel)
                i+=1
            else:
                nro = int(fila[0])
                piso = int(fila[1])
                tipo = fila[2]
                precioxnoche = float(fila[3])
                if fila[4].lower() == "true":
                        disponibilidad = True
                else:
                        disponibilidad = False
                self.__listaH[i].agregarHabitacion(nro,piso,tipo,precioxnoche,disponibilidad)
        archivo.close()

    def buscarHotel(self,xnom):
        i=0
        bandera=False
        aux=None

        while i < len(self.__listaH) and not bandera:
            if xnom.lower() == self.__listaH[i].getNombre().lower():
                aux = self.__listaH[i]
                bandera = True
            else:
                i+=1
        if bandera == True:
            print("Hotel encontrado.")
        return aux

    def inciso1(self,xnom):
        i=0
        bandera=False
        while i < len(self.__listaH) and not bandera:
            if xnom.strip().lower() == self.__listaH[i].getNombre().strip().lower():
                nro = int(input("\nIngresar en numero de habitacion: "))
                piso = int(input("\ningresar piso: "))
                tipo = input("\nIngresar tipo:")
                precioxnoche = float(input("\nIngresar precio:"))
                disponibilidad = True
                self.__listaH[i].agregarHabitacion(nro,piso,tipo,precioxnoche,disponibilidad)
                bandera = True
            else:
                i+=1
        if bandera == True:
            print("Habitacion agregada con exito!!")
        else:
            print("El hotel no existe.")
        
    
    def mostrar(self):
        i = 0
        lista = self.__listaH[i].getLista()
        print("Habitaciones en el hotel:")
        for h in lista:
            print(f"Número: {h.getNumero()}, Piso: {h.getPiso()}, Tipo: {h.getTipo()}, Precio: {h.getPrecioxnoche()}, Disponible: {h.getDisp()}")

    def inciso2(self,xhotel,xhabitacion):
        i=0
        bandera=False
        
        while i < len(self.__listaH) and not bandera:
            hotel = self.__listaH[i]
            if hotel.getNombre().strip().lower() == xhotel.strip().lower():
                lista = hotel.getLista()
                j=0
                while j < len(lista):
                    habitacion = lista[j]
                    if xhabitacion == habitacion.getNumero():
                        if habitacion.getDisp() == True:
                            habitacion.setDisponibilidad(False)
                            print("Se ha reservado la habitacion con exito!!")
                            bandera = True
                        else:
                            print("La habitacion ya esta reservada.")
                            bandera = True
                    j+=1
        i+=1
        if not bandera:
            print("No se encontro la habitacion")
    
    def inciso3(self,xhotel,xhabitacion):
        i=0
        bandera=False
        
        while i < len(self.__listaH) and not bandera:
            hotel = self.__listaH[i]
            if hotel.getNombre().strip().lower() == xhotel.strip().lower():
                lista = hotel.getLista()
                j=0
                while j < len(lista):
                    habitacion = lista[j]
                    if xhabitacion == habitacion.getNumero():
                        if habitacion.getDisp() == False:
                            habitacion.setDisponibilidad(True)
                            print("Se ha liberado la habitacion.")
                            bandera = True
                        else:
                            print("La habitacion ya esta liberada")
                            bandera = True
                    j+=1
        i+=1
        if not bandera:
            print("No se encontro la habitacion")

    def inciso4(self):
        xtipo = input("\nIngrese el tipo de habitacion:") 
        i = 0
        bandera = False
        while i < len(self.__listaH) and not bandera:
            hotel = self.__listaH[i]
            lista = hotel.getLista()
            j = 0
            while j < len(lista):
                habitacion = lista[j]
                if xtipo.lower() == habitacion.getTipo().lower():
                    print(f"Tipo: {xtipo}, NRO: {habitacion.getNumero()}, Piso: {habitacion.getPiso()}")
                    bandera=True
                j+=1
        i+=1
    
    def inciso5(self):
        xpiso = int(input("\nIngrese un piso:")) 
        i = 0
        bandera = False
        aux = 0
        while i < len(self.__listaH) and not bandera:
            hotel = self.__listaH[i]
            lista = hotel.getLista()
            j = 0
            while j < len(lista):
                habitacion = lista[j]
                if xpiso == habitacion.getPiso():
                    if habitacion.getDisp() == True:
                        aux+=1
                        bandera=True
                j+=1
        i+=1
        print(f"En el piso {xpiso} hay una cantidad de {aux} habitaciones libres")

    def inciso6(self):
        encabezado_mostrado = False
        xtipo = input("\nIngrese el tipo de habitacion:") 
        i = 0
        bandera = False
        while i < len(self.__listaH) and not bandera:
            hotel = self.__listaH[i]
            lista = hotel.getLista()
            j = 0
            while j < len(lista):
                habitacion = lista[j]
                if xtipo.lower() == habitacion.getTipo().lower():
                    if not encabezado_mostrado:
                        print(f"Tipo_de_habitacion: {xtipo}")
                        print("Numero\tPiso\tPrecio por noche\tDisponibilidad ")
                        encabezado_mostrado = True
                    disponibilidad = "Sí" if habitacion.getDisp() else "No"
                    print(f"{habitacion.getNumero()}\t{habitacion.getPiso()}\t{habitacion.getPrecioxnoche()}\t\t{disponibilidad}")
                    bandera=True
                j+=1
        i+=1
    

