import csv
from os import name as osname, system
from datetime import datetime, timedelta
# Ruta al archivo CSV
RUTA_ARCHIVO = "nuevo_usuarioh.csv"
FORMATO_FECHA = "%d/%m/%Y"
# Función para verificar si un número de habitación existe en el archivo CSV
def verificar_existencia(num_hab, fecha_entrada, fecha_salida):
    with open(RUTA_ARCHIVO, mode="r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            fecha_final = datetime.strptime(fila[6], FORMATO_FECHA)
            fecha_inicial = datetime.strptime(fila[5], FORMATO_FECHA)
            fe = datetime.strptime(fecha_entrada, FORMATO_FECHA)
            fs = datetime.strptime(fecha_salida, FORMATO_FECHA)
            df = fs - fecha_final
            di = fe - fecha_inicial
            if (fe >= fecha_final or fe <= fecha_inicial) and fila[7] == num_hab:
                return True
    return False


def validar_fecha(texto):
    fecha = "01/01/2024"
    while True:
        try:
             fecha = input(texto)
             d = datetime.strptime(fecha, FORMATO_FECHA)
             if d < datetime.now() - timedelta(days=1):
                 print("Por favor ingrese una fecha posterior al dia de hoy.")
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
            if texto is "":
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
    fecha_entrada = validar_fecha("Ingrese fecha de entrada: ")
    fecha_salida = validar_fecha("Ingrese fecha de salida: ")
    while(fecha_salida < fecha_entrada):
        print("Por favor ingresa una fecha de salida posterior a la de entrada.")
        fecha_salida = validar_fecha("Ingrese fecha de salida: ")
    return nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida

# Función para calcular los días transcurridos entre dos fechas
def dias_transcurridos(fecha_inicial, fecha_final):
    try:
        fecha1 = datetime.strptime(fecha_inicial, FORMATO_FECHA)
        fecha2 = datetime.strptime(fecha_final, FORMATO_FECHA)
        diferencia_dias = fecha2 - fecha1
        return diferencia_dias.days
    except ValueError:
        print("Por favor ingrese la fecha en el formato día/mes/año, ejemplo: 24/07/1995")
        return None

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
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(usuario_reserva)

def borrar_reserva():
    num_fila = int(mostrar_reservas())
    newData = list()
    registro:int = -1
    newNum_Fila = 0
    while registro > num_fila or registro < 0:
        registro = validar_entero("¿Cual reserva desea borrar? (solo el numero) - 0: Para volver al menu. ")
    
    if registro != 0:
        with open(RUTA_ARCHIVO, mode="r") as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            print("BORRANDO REGISTRO NUM: ",registro)
            #escritor_csv = csv.writer(archivo_csv)
            for fila in lector_csv:
                if newNum_Fila != registro-1:
                    newData.append(fila)
                newNum_Fila = newNum_Fila + 1                    
        
        with open(RUTA_ARCHIVO, mode="w+", newline='') as archivo_csv:
            archivo_csv.truncate()
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(newData)

        print("Reserva borrada exitosamente.")

def mostrar_reservas():
    limpiar_pantalla()
    num_fila = 0
    print('''***RESERVACIONES***''')
    with open(RUTA_ARCHIVO, mode="r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
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
        else:
            continue

def prepararReserva():
    limpiar_pantalla()
    with open(RUTA_ARCHIVO, 'a', newline='') as file:
        writer = csv.writer(file)
    nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida = obtener_info_usuario()
    diferencia_dias = dias_transcurridos(fecha_entrada, fecha_salida)
    
    if diferencia_dias is not None:
        num_hab = obtener_numero_habitacion(fecha_entrada, fecha_salida)

        reserva = [
            nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida, num_hab
        ]

        hacer_reserva(reserva)
        print(f"Reserva realizada exitosamente. La fecha de entrada es {fecha_entrada} 10:00PM y la de salida es {fecha_salida} 9:00PM.")

# Función principal
def main():
    menu()

if __name__ == "__main__":
    main()