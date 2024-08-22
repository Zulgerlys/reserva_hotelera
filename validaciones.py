from datetime import datetime, timedelta
FORMATO_FECHA = "%d/%m/%Y"
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

def obtener_info_usuario():
    nombre = validar_texto("Ingrese nombre: ")
    apellido = validar_texto("Ingrese apellido: ")
    cedula = validar_texto("Ingrese cédula: ")
    edad = validar_entero("Ingrese edad: ")
    telf = validar_texto("Ingrese teléfono: ")
    fecha_entrada = validar_fecha_entrada("Ingrese fecha de entrada: ")
    fecha_salida = validar_fecha_salida("Ingrese fecha de salida: ",fecha_entrada)
    return nombre, apellido, cedula, edad, telf, fecha_entrada, fecha_salida

