from datetime import datetime
from os.path import exists
from csv import reader, writer
from validaciones import validar_entero, obtener_info_usuario
from pantalla import limpiar_pantalla
FORMATO_FECHA = "%d/%m/%Y"
RUTA_ARCHIVO = "nuevo_usuarioh.csv"
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

def hacer_reserva(usuario_reserva):
    with open(RUTA_ARCHIVO, mode="a", newline="") as archivo_csv:
        escritor_csv = writer(archivo_csv)
        escritor_csv.writerow(usuario_reserva)

def borrar_reserva():
    num_fila:int = mostrar_reservas()
    nuevoRegistro = list()
    registro:int = -1
    while registro > num_fila or registro < 0:
        registro = validar_entero("¿Cual reserva desea borrar? (solo el numero) - 0: Para volver al menu. ")
    
    if registro != 0:
        with open(RUTA_ARCHIVO, mode="r") as archivo_csv:
            lector_csv = reader(archivo_csv)
            numeroFilas:int = 0
            print("Borrando registro #: ",registro)
            for fila in lector_csv:
                if numeroFilas != registro-1:
                    nuevoRegistro.append(fila)
                numeroFilas = numeroFilas + 1                    
        
        with open(RUTA_ARCHIVO, mode="w+", newline='') as archivo_csv:
            archivo_csv.truncate()
            escritor_csv = writer(archivo_csv)
            escritor_csv.writerows(nuevoRegistro)

        print("Reserva borrada exitosamente.")


def mostrar_reservas():
    limpiar_pantalla()
    print('''***RESERVACIONES***''')
    with open(RUTA_ARCHIVO, mode="r") as archivo_csv:
        num_fila:int = 0
        lector_csv = reader(archivo_csv)
        for fila in lector_csv:
            print(f"Reserva {num_fila + 1}: [Cliente: {fila[0]} {fila[1]}, Cedula: {fila[2]}, Edad: {fila[3]}, Tel: {fila[4]}, FE: {fila[5]}, FS: {fila[6]}, Hab: #{fila[7]}]")
            num_fila += 1
    return num_fila

#Funcion para verificar si el archivo existe
def verificar_archivo():
    archivo_existe = exists(RUTA_ARCHIVO)
    if not archivo_existe:
        with open(RUTA_ARCHIVO, 'w', newline='') as file:
            writer(file)

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

#Funcion para preparar la reserva
def prepararReserva():
    limpiar_pantalla()

    nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida = obtener_info_usuario()
    num_hab = obtener_numero_habitacion(fecha_entrada, fecha_salida)
    reserva = [nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida, num_hab]

    hacer_reserva(reserva)
    print(f"Reserva realizada exitosamente. La fecha de entrada es {fecha_entrada} 10:00am y la de salida es {fecha_salida} 9:00am.")