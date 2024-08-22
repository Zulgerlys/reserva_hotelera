from csv import reader, writer
from os import name as osname, system, path
from datetime import datetime, timedelta
# Ruta al archivo CSV
RUTA_ARCHIVO = "nuevo_usuarioh.csv"
FORMATO_FECHA = "%d/%m/%Y"
# Función para verificar si un número de habitación existe en el archivo CSV
def verificar_existencia(num_hab, fecha_entrada, fecha_salida):
    with open(RUTA_ARCHIVO, mode="r") as archivo_csv:
        lector_csv = reader(archivo_csv)
        for fila in lector_csv:
            fecha_final_csv = datetime.strptime(fila[6], FORMATO_FECHA)
            fecha_inicial_csv = datetime.strptime(fila[5], FORMATO_FECHA)
            fe = datetime.strptime(fecha_entrada, FORMATO_FECHA)
            fs = datetime.strptime(fecha_salida, FORMATO_FECHA)
            if (fe <= fecha_final_csv and fe >= fecha_inicial_csv or fs <= fecha_final_csv and fs >= fecha_inicial_csv) and fila[7] == num_hab:
                return True
    return False


def validar_fecha_entrada(texto):
    fecha = "01/01/2024"
    while True:
        try:
             fecha = input(texto)
             d = datetime.strptime(fecha, FORMATO_FECHA)
             if d < (datetime.now() - timedelta(days=1)):
                 print("Por favor ingrese una fecha posterior al dia de hoy.")
                 continue
             break
        except ValueError:
            print("Por ingrese una fecha con el formato día/mes/año, ejemplo: 24/07/1995")
    return fecha

def validar_fecha_salida(texto, fecha_entrada):
    fecha = "02/01/2024"
    while True:
        try:
             fecha = input(texto)
             fs = datetime.strptime(fecha, FORMATO_FECHA)
             fe = datetime.strptime(fecha_entrada, FORMATO_FECHA)
             if fe >= fs:
                 print(f"Por favor ingrese una fecha posterior al {fecha_entrada}")
                 continue
             break
        except ValueError:
            print("Por ingrese una fecha con el formato día/mes/año, ejemplo: 24/07/1995")
    return fecha

def validar_entero(texto):
    while True:
        try:
            num = int(input(texto))
            if(num < 0):
                print("Por favor ingrese un número entero positivo.")
                continue
            break
        except ValueError:
            print("Por favor ingrese un número entero positivo.")
    return num

#Funcion para Validar Texto
def validar_texto(mensaje):
    while True:
        try:
            texto = input(mensaje)
            if texto == "":
                raise ValueError
            else: break
        except ValueError:
            print("Introduce un texto valido.")
    return texto

# Función para solicitar información del usuario
def obtener_info_usuario():
    nombre = validar_texto("Ingrese nombre: ")
    apellido = validar_texto("Ingrese apellido: ")
    cedula = validar_texto("Ingrese cédula: ")
    edad = validar_entero("Ingrese edad: ")
    telf = validar_texto("Ingrese teléfono: ")
    fecha_entrada = validar_fecha_entrada("Ingrese la fecha de entrada: ")
    fecha_salida = validar_fecha_salida("Ingrese la fecha de salida: ", fecha_entrada)
    return nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida

# Función para obtener el número de habitación deseado
def obtener_numero_habitacion(fecha_entrada, fecha_salida):
    num_hab = input("Ingrese número de habitación que desea: ")
    while verificar_existencia(num_hab,fecha_entrada, fecha_salida) or int(num_hab) > 50 or int(num_hab) <= 0:
        if verificar_existencia(num_hab,fecha_entrada, fecha_salida):
            print(f"La habitación {num_hab} ya está ocupada.")
        elif int(num_hab) <= 0:
            print("Las habitaciones empiezan a partir de la 1.")
        elif int(num_hab) > 50:
            print("Solo tenemos 50 habitaciones.")
        num_hab = input("Ingrese número de habitación que desea: ")
    return num_hab

# Función para guardar la reservacion en el archivo CSV
def hacer_reserva(usuario_reserva):
    with open(RUTA_ARCHIVO, mode="a", newline="") as archivo_csv:
        escritor_csv = writer(archivo_csv)
        escritor_csv.writerow(usuario_reserva)

def borrar_reserva():
    num_fila = int(mostrar_reservas())
    nuevoRegistro = list()
    registro:int = -1
    while registro > num_fila or registro < 0:
        registro = validar_entero("¿Cual reserva desea borrar? (solo el numero) - 0: Para volver al menu. ")
    
    if registro != 0:
        with open(RUTA_ARCHIVO, mode="r") as archivo_csv:
            lector_csv = reader(archivo_csv)
            print(f"Borrando registro #:{registro}")
            newNum_Fila:int = 0
            for fila in lector_csv:
                if newNum_Fila != registro-1:
                    nuevoRegistro.append(fila)
                newNum_Fila = newNum_Fila + 1                    
        
        with open(RUTA_ARCHIVO, mode="w+", newline='') as archivo_csv:
            archivo_csv.truncate()
            escritor_csv = writer(archivo_csv)
            escritor_csv.writerows(nuevoRegistro)

        print("Reserva borrada exitosamente.")

def mostrar_reservas():
    limpiar_pantalla()
    print('''***RESERVACIONES***''')
    with open(RUTA_ARCHIVO, mode="r") as archivo_csv:
        lector_csv = reader(archivo_csv)
        num_fila:int = 0
        for fila in lector_csv:
            print(f"Reserva {num_fila + 1}: [Cliente: {fila[0]} {fila[1]}, Cedula: {fila[2]}, Edad: {fila[3]}, Tel: {fila[4]}, FE: {fila[5]}, FS: {fila[6]}, Hab: #{fila[7]}]")
            num_fila += 1
    return num_fila

#Funcion para limpiar la pantalla
def limpiar_pantalla():
    if osname == "nt":
        system("cls")
    else:
        system("clear")

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

def prepararReserva():
    limpiar_pantalla()

    nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida = obtener_info_usuario()
    num_hab = obtener_numero_habitacion(fecha_entrada, fecha_salida)
    reserva = [nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida, num_hab]

    hacer_reserva(reserva)
    print(f"Reserva realizada exitosamente. La fecha de entrada es {fecha_entrada} 10:00am y la de salida es {fecha_salida} 9:00am.")

#Funcion para verificar si el archivo existe
def verificar_archivo():
    archivo_existe = path.exists(RUTA_ARCHIVO)
    if not archivo_existe:
        with open(RUTA_ARCHIVO, 'w', newline='') as file:
            writer(file)


if __name__ == "__main__":
    verificar_archivo()
    menu()