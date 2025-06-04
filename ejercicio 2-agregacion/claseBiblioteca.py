class Biblioteca:
    __nombre: str
    __direccion:str
    __telefono:str
    __listaL: list

    def __init__(self,n,d,t):
        self.__nombre = n
        self.__direccion = d
        self.__telefono = t
        self.__listaL = []

    def agregarLibro(self,unlibro):
        self.__listaL.append(unlibro)
    
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def getListaL(self):
        return self.__listaL
    
    def buscarlibro(self,xlibro):
        i=0
        longitud = len(self.__listaL)
        bandera = False
        while i<longitud and not bandera:
            if xlibro.strip().lower() == self.__listaL[i].getTitulo().strip().lower():
                bandera = True
            else:
                i+=1
        return i

    def deletelibro(self,xlibro):
        indice = self.buscarlibro(xlibro)
        del self.__listaL[indice]

    def datoslibro(self,xtitulo):
        libro = None
        i = self.buscarlibro(xtitulo)
        if 0 <= i < len(self.__listaL):
            libro = self.__listaL[i]
        return libro
    
    def listaLibros(self):
        for book in self.__listaL:
            print(f"Titulo: {book.getTitulo()} Autor: {book.getAutor()} isbn: {book.getIsbn()} Genero: {book.getGenero()}")
            