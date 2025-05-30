from gestorHotel import gestorH
def menu():
    print("""
    1)Agregar una habitacion.
    2)Reservar una habitacion.
    3)Liberar una habitacion.
    4)Ingresar un tipo de habitacion y muestras todas las habitaciones de ese tipo.
    5)Mostrar la cantidad de habitaciones libres por piso.
    6)Ingresar un tipo de habitacion y muestra en detalle lo que contiene.
    7)Salir.
            """)
    op = int(input("\nSeleccione una opcion: "))
    while op != 7:
        if op == 1:
            xnom = input("Ingrese el hotel donde va a agregar una habitacion: ")
            gh.inciso1(xnom)
            gh.mostrar()
        elif op == 2:
            xhotel = input("\nIngrese el nombre del hotel donde quiere hacer una reserva: ")
            xhabitacion = int(input("\nIngrese el numero de la habitacion que quiere reservar: "))
            gh.inciso2(xhotel,xhabitacion)
            gh.mostrar()
        elif op == 3:
            xhotel = input("\nIngrese el nombre del hotel donde quiere hacer una reserva: ")
            xhabitacion = int(input("\nIngrese el numero de la habitacion que quiere reservar: "))
            gh.inciso3(xhotel,xhabitacion)
            gh.mostrar()
        elif op == 4:
            gh.inciso4()
        elif op == 5:
            gh.inciso5()
        elif op == 6:
            gh.inciso6()
        elif op == 7:
            print("\nSaliendo........")
if __name__ == "__main__":
    gh = gestorH()
    gh.test()
    menu()