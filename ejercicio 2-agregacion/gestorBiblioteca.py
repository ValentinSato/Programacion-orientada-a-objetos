from claseBiblioteca import Biblioteca
from claseLibro import Libro
import csv

class gestorB:
    __listab: list

    def __init__(self):
        self.__listab = []

    def agregarBiblioteca(self,unabiblioteca):
        self.__listab.append(unabiblioteca)

    def test(self):

        i = -1
        archivo = open("Biblioteca.csv")
        reader = csv.reader(archivo, delimiter=";")
        
        for fila in reader:
            if len(fila) == 3:
                unabiblioteca = Biblioteca(fila[0],fila[1],fila[2])
                self.agregarBiblioteca(unabiblioteca)
                i+=1
            else:
                unlibro = Libro(fila[0],fila[1],fila[2],fila[3])

                self.__listab[i].agregarLibro(unlibro)
        archivo.close()

    def buscarbiblioteca(self,xbiblioteca):
        i=0
        longitud = len(self.__listab)
        bandera = False
        while i < longitud and not bandera:
            if xbiblioteca.strip().lower() == self.__listab[i].getNombre().strip().lower():
                bandera = True
            else:
                i+=1
        return i

    def inciso1(self,xbiblioteca):
        i = self.buscarbiblioteca(xbiblioteca)
        titulo = input("Ingresa el titulo:")
        autor = input("Ingresa el autor:")
        isbn = input("Ingresa el isbn:")
        genero = input("Ingresa el genero:")
        self.__listab[i].agregarLibro(Libro(titulo,autor,isbn,genero))
                
            
    def inciso2(self,xbiblioteca):
        i = self.buscarbiblioteca(xbiblioteca)
        xlibro = input("Ingresar el libro que desea eliminar:")
        self.__listab[i].deletelibro(xlibro)
    
    def inciso3(self,xtitulo):
        datos = False
        for biblio in self.__listab:
            libro = biblio.datoslibro(xtitulo)
            if libro:
                if not datos:
                    print(f"Autor: {libro.getAutor()} \nGenero: {libro.getGenero()}")
                print(biblio.getNombre())

    def inciso4(self):
        for book in self.__listab:
            book.listaLibros()
        