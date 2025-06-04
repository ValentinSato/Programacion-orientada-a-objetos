from gestorBiblioteca import gestorB

def menu():
    print(""" 
    1)Agregar libro.
    2)Eliminar libro.
    3)Buscar libro.
    4)Listar libros.

    """)
    op = int(input("\nIngresa una opcion: "))
    while op != 5:
        if op == 1:
            xbiblioteca = input("Ingresar biblioteca que quiera agregar un libro:")
            gb.inciso1(xbiblioteca)
            print("Se ha agregado el libro con exito!!")
        elif op == 2:
            xbiblioteca = input("Ingresa la biblioteca donde quieras eliminar un libro:")
            gb.inciso2(xbiblioteca)
        elif op == 3:
            xtitulo = input("Ingresar el titulo de la obra:")
            gb.inciso3(xtitulo)
        elif op == 4:
            gb.inciso4()

        

if __name__ == "__main__":
    gb = gestorB()
    gb.test()
    menu()