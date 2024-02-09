# Diccionarios para almacenar participantes y eventos
participantes = []
eventos = []

# Función para registrar un participante
def registrar_participante():
    documento = input("Ingrese el documento del participante: ")
    nombre = input("Ingrese el nombre del participante: ")
    edad = int(input("Ingrese la edad del participante: "))
    cargo = input("Ingrese el cargo del participante: ")
    participante = {"documento": documento, "nombre": nombre, "edad": edad, "cargo": cargo, "pago_realizado": False}
    participantes.append(participante)
    print("Participante registrado exitosamente.")

# Función para registrar un evento
def registrar_evento():
    nombre = input("Ingrese el nombre del evento: ")
    locacion = input("Ingrese la locación del evento: ")
    dia = input("Ingrese el día del evento: ")
    evento = {"nombre": nombre, "locacion": locacion, "dia": dia, "realizado": False}
    eventos.append(evento)
    print("Evento registrado exitosamente.")

# Función para quitar un participante del registro
def quitar_participante():
    documento = input("Ingrese el documento del participante que desea quitar: ")
    for participante in participantes:
        if participante["documento"] == documento:
            if participante["pago_realizado"]:
                print("Este participante ya ha pagado, no se puede quitar del registro.")
                return
            participantes.remove(participante)
            print("Participante eliminado del registro.")
            return
    print("No se encontró ningún participante con ese documento.")

# Función para eliminar o modificar un evento
def eliminar_modificar_evento():
    nombre = input("Ingrese el nombre del evento que desea eliminar/modificar: ")
    for evento in eventos:
        if evento["nombre"] == nombre:
            if evento["realizado"]:
                print("Este evento ya ha sido realizado, no se puede eliminar/modificar.")
                return
            opcion = input("¿Desea eliminar (E) o modificar (M) el evento? ").upper()
            if opcion == 'E':
                eventos.remove(evento)
                print("Evento eliminado exitosamente.")
            elif opcion == 'M':
                locacion = input("Ingrese la nueva locación del evento: ")
                dia = input("Ingrese el nuevo día del evento: ")
                evento["locacion"] = locacion
                evento["dia"] = dia
                print("Evento modificado exitosamente.")
            else:
                print("Opción no válida.")
            return
    print("No se encontró ningún evento con ese nombre.")

# Función para conocer empleados pendientes de pago
def empleados_pendientes_pago():
    pendientes = [participante for participante in participantes if not participante["pago_realizado"]]
    deuda_total = len(pendientes) * 50000
    print(f"Empleados pendientes de pago: {len(pendientes)}")
    print("Empleados pendientes:")
    for participante in pendientes:
        print(f"- {participante['nombre']}")
    print(f"Deuda total: {deuda_total} COP.")

# Función para marcar un evento como realizado
def marcar_evento_realizado():
    nombre = input("Ingrese el nombre del evento que desea marcar como realizado: ")
    for evento in eventos:
        if evento["nombre"] == nombre:
            evento["realizado"] = True
            print("Evento marcado como realizado exitosamente.")
            return
    print("No se encontró ningún evento con ese nombre.")

# Función principal para mostrar el menú y ejecutar las opciones
def menu_principal():
    while True:
        print("\n----- Menú Principal -----")
        print("1. Registrar participante")
        print("2. Registrar evento")
        print("3. Quitar participante del registro")
        print("4. Eliminar/Modificar evento")
        print("5. Empleados pendientes de pago")
        print("6. Marcar evento como realizado")
        print("7. Salir")
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        try:
            opcion = int(opcion)
            if opcion == 1:
                registrar_participante()
            elif opcion == 2:
                registrar_evento()
            elif opcion == 3:
                quitar_participante()
            elif opcion == 4:
                eliminar_modificar_evento()
            elif opcion == 5:
                empleados_pendientes_pago()
            elif opcion == 6:
                marcar_evento_realizado()
            elif opcion == 7:
                confirmacion = input("¿Está seguro que desea salir? (S/N): ").upper()
                if confirmacion == 'S':
                    print("¡Hasta luego!")
                    break
                elif confirmacion == 'N':
                    continue
                else:
                    print("Opción no válida.")
            else:
                print("Opción no válida. Ingrese un número del 1 al 7.")
        except ValueError:
            print("Por favor ingrese un número válido.")

# Ejecutar la función principal al iniciar el programa
if __name__ == "__main__":
    menu_principal()
