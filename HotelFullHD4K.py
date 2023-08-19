import csv
import datetime

# Ruta al archivo CSV
ruta_archivo = "nuevo_usuarioh.csv"

# Función para verificar si un número de habitación existe en el archivo CSV
def verificar_existencia(num_hab):
    with open(ruta_archivo, mode="r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if num_hab in fila:
                return True
    return False

# Función para solicitar información del usuario
def obtener_info_usuario():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    cedula = input("Ingrese cédula: ")
    edad = input("Ingrese edad: ")
    telf = input("Ingrese teléfono: ")
    fecha_entrada = input("Ingrese fecha de entrada: ")
    fecha_salida = input("Ingrese fecha de salida: ")
    return nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida

# Función para calcular los días transcurridos entre dos fechas
def dias_transcurridos(fecha_inicial, fecha_final):
    try:
        formato = "%d/%m/%Y"
        fecha1 = datetime.datetime.strptime(fecha_inicial, formato)
        fecha2 = datetime.datetime.strptime(fecha_final, formato)
        diferencia_dias = fecha2 - fecha1
        return diferencia_dias.days
    except ValueError:
        print("Por favor ingrese la fecha en el formato día/mes/año, ejemplo: 24/07/1995")
        return None

# Función para obtener el número de habitación deseado
def obtener_numero_habitacion():
    num_hab = input("Ingrese número de habitación que desea: ")
    while verificar_existencia(num_hab) or int(num_hab) > 50 or int(num_hab) <= 0:
        if verificar_existencia(num_hab):
            print(f"La habitación '{num_hab}' ya está ocupada.")
        elif int(num_hab) <= 0:
            print("Las habitaciones empiezan a partir de la 1.")
        elif int(num_hab) > 50:
            print("Solo tenemos 50 habitaciones.")
        num_hab = input("Ingrese número de habitación que desea: ")
    return num_hab

# Función para guardar la reservacion en el archivo CSV
def hacer_reserva(usuario_reserva):
    with open(ruta_archivo, mode="a", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(usuario_reserva)

# Función principal
def main():
    nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida = obtener_info_usuario()
    diferencia_dias = dias_transcurridos(fecha_entrada, fecha_salida)
    
    if diferencia_dias is not None:
        num_hab = obtener_numero_habitacion()

        reserva = [
            nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida, num_hab
        ]

        hacer_reserva(reserva)
        print("Reserva realizada exitosamente.")

if __name__ == "__main__":
    main()