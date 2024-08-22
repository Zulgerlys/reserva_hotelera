from os import name, system
#funcion para limpiar la pantalla
def limpiar_pantalla():
    if name == "nt":
        system("cls")
    else:
        system("clear")