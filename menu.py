from os import name, system
from archivo_operaciones import borrar_reserva, mostrar_reservas, prepararReserva
from pantalla import limpiar_pantalla
#Funciuon para mostrar el menu
def menu():
    while True:
        limpiar_pantalla()
        print('''
                BIENVENIDO AL HOTEL MEJIAS °''', '''°''')
        print('''
                ***MENU DE SELECCION***''')
        print('Elije una de las siguientes opciones:')
        print('\n[r].Reservar habitación \n[b].Borrar reservación \n[v].Ver reservaciones \n[x].Salir\n')
        opcion = input('Introduce la opción deseada: ')
        opcion = opcion.lower()
        if opcion == "x" or opcion == "salir":
            break
        elif opcion == "b" or opcion == "borrar":
            borrar_reserva()
            input("Presione Enter para volver al menu principal")
        elif opcion == "v" or opcion == "ver":
            mostrar_reservas()
            input("Presione Enter para volver al menu principal")
        elif opcion == "r" or opcion == "reservar":
            prepararReserva()
            input("Presione Enter para volver al menu principal")
