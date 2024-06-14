import pickle
import os

# Inicializamos los asientos - TRUE: representa los asientos disponibles, FALSE: representa asiento ocupado
asientos = [True] * 42
# Diccionario para almacenar los datos de los pasajeros
datosPasajeros = {}

#AQUI SE MUESTRAN LOS ASIENTOS DISPONIBLES
def mostrarAsientos():
    print("Estos son los asientos del avion (X = Ocupado, O = Disponible):")
    for fila in range(7):
        for columna in range(6):
            numeroAsiento = fila * 6 + columna
            estado = "O" if asientos[numeroAsiento] else "X"
            print(f"{numeroAsiento + 1:2}: {estado}", end="  ")
        print()

#VALIDAR RUT DE 9 DIGITOS
def validarRut(rut):
    return rut.isdigit() and len(rut) == 9

#VALIDAR TELEFONO QUE EMPIECE CON 9 Y SEA DE 9 DIGITOS
def validarTelefono(telefono):
    return telefono.isdigit() and len(telefono) == 9 and telefono.startswith("9")

#COMPRA DE PASAJES
def comprarAsiento():
    nombre = input("Ingrese su nombre: ")

    rut = input("Ingrese su RUT sin punto ni guiones (9 dígitos): ")
    while not validarRut(rut):
        print("RUT inválido. Debe tener 9 dígitos.")
        rut = input("Ingrese su RUT (9 dígitos): ")

    telefono = input("Ingrese su teléfono (Debe empezar con el numero 9): ")
    while not validarTelefono(telefono):
        print("Teléfono inválido. Debe tener 9 dígitos y empezar con 9.")
        telefono = input("Ingrese su teléfono (9 dígitos, empieza con 9): ")

    banco = input("Ingrese su banco: ")
    
#ASIENTOS DISPONIBLES A LA HORA DE COMPRA
    mostrarAsientos()
    numeroAsiento = int(input("Seleccione el número de asiento que desea comprar: ")) - 1
    
    if not (0 <= numeroAsiento < 42):
        print("Número de asiento inválido.")
        return
    
    if not asientos[numeroAsiento]:
        print("Asiento no disponible.")
        return
    
    if numeroAsiento >= 30:  # Asientos VIP
        precio = 240000
    else:  # Asientos normales
        precio = 78900
    
    if banco.lower() == "bancoduoc":
        precio *= 0.85  # Aplicar 15% de descuento
    
    print(f"El valor del pasaje es: ${precio:.2f}")
    
#CONFIRMACION DE COMPRA O CANCELAR
    confirmacion = input("¿Desea confirmar la compra? (s/n): ")
    if confirmacion.lower() == "s":
        asientos[numeroAsiento] = False
        datosPasajeros[numeroAsiento] = {
            "nombre": nombre,
            "rut": rut,
            "telefono": telefono,
            "banco": banco
        }
        print("Compra realizada con éxito.")
    else:
        print("Compra cancelada.")
    
    print()

#ANULAR VUELOS
def anularVuelo():
    numeroAsiento = int(input("Ingrese el número de asiento que desea anular: ")) - 1
    
    if not (0 <= numeroAsiento < 42):
        print("Número de asiento inválido.")
        return
    
    if asientos[numeroAsiento]:
        print("El asiento ya está disponible.")
        return
    
    asientos[numeroAsiento] = True
    del datosPasajeros[numeroAsiento]
    print("Vuelo anulado con éxito.")
    
    print()


#MODIFICAR DATOS DEL CLIENTE

def modificarDatos():
    numeroAsiento = int(input("Ingrese el número de asiento: ")) - 1
    rut = input("Ingrese el RUT del pasajero: ")
    
    if not (0 <= numeroAsiento < 42):
        print("Número de asiento inválido.")
        return
    
    if asientos[numeroAsiento]:
        print("El asiento está disponible, no hay datos para modificar.")
        return
    
    pasajero = datosPasajeros.get(numeroAsiento)
    if pasajero["rut"] != rut:
        print("RUT no coincide con el registrado.")
        return
    
    print("1. Modificar nombre")
    print("2. Modificar teléfono")
    opcion = input("Seleccione la opción que desea modificar: ")
    print()
    
    if opcion == "1":
        nuevoNombre = input("Ingrese el nuevo nombre: ")
        pasajero["nombre"] = nuevoNombre
    elif opcion == "2":
        nuevoTelefono = input("Ingrese el nuevo teléfono (9 dígitos, empieza con 9): ")
        while not validarTelefono(nuevoTelefono):
            print("Teléfono inválido. Debe tener 9 dígitos y empezar con 9.")
            nuevoTelefono = input("Ingrese el nuevo teléfono (9 dígitos, empieza con 9): ")
        pasajero["telefono"] = nuevoTelefono
    else:
        print("Opción inválida.")
    
    datosPasajeros[numeroAsiento] = pasajero
    print("Datos modificados con éxito.")
    
    print()


#INICIIALIZAR SISTEMA Y AGREGAR EL GUARDADO DE DATOS CON PICKLE 

def inicializarSistema():
    global asientos, datosPasajeros
    if os.path.exists("datosVuelos.pkl"):
        with open("datosVuelos.pkl", "rb") as f:
            asientos, datosPasajeros = pickle.load(f)
    else:
        asientos = [True] * 42
        datosPasajeros = {}

def guardarDatos():
    with open("datosVuelos.pkl", "wb") as f:
        pickle.dump((asientos, datosPasajeros), f)
