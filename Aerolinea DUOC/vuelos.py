import funcionesVuelos as fv

def mostrarMenu():
    print("*" * 35)
    print("Bienvenidos a la aerolinea de DUOC")
    print("*" * 35)
    print("1. Ver los asientos disponibles")
    print("2. Comprar un asiento")
    print("3. Anular un vuelo")
    print("4. Modificar los datos del pasajero")
    print("5. Salir")
    print("*" * 35)

def main():
    fv.inicializarSistema()
    
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")
        
        try:
            if opcion == "1":
                fv.mostrarAsientos()
            elif opcion == "2":
                fv.comprarAsiento()
            elif opcion == "3":
                fv.anularVuelo()
            elif opcion == "4":
                fv.modificarDatos()
            elif opcion == "5":
                print("Guardando datos y saliendo del sistema...")
                fv.guardarDatos()
                break
            else:
                raise ValueError("Opción inválida. Intente de nuevo.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
