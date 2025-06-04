class Libro:
    __titulo: str
    __autor: str
    __isbn: str
    __genero: str

    def __init__(self,t,a,i,g):
        self.__titulo = t
        self.__autor = a
        self.__isbn = i
        self.__genero = g

    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getIsbn(self):
        return self.__isbn
    def getGenero(self):
        return self.__genero
    def __del__(self):
        print(f"Libro {self.__titulo} borrado.")
        