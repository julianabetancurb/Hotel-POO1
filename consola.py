import sys
from hotel.mundo.hotel import Hotel


class Consola:

    def __init__(self):
        self.hotel = Hotel()
        self.opciones = {
            "1": self.realizar_reserva,
            "2": self.registrar_usuario,
            "3": self.cancelar_reserva,
            "4": self.reserva_restaurante,
            "5": self.reservar_zona_entretenimiento,
            "6": self.reserva_servicio_turismo,
            "7": self.reserva_vehiculo,
            "8": self.reserva_servicios_salon_belleza,
            "9": self.reserva_servicio_lavanderia,
            "10": self.servicio_check_out,
            "11": self.servicio_limpieza_cuarto,
            "12": self.escribir_sugerencias,
            "13": self.salir
        }

    def mostrar_menu(self):
        print("""
            \n
            BIENVENIDO A EL HOTEL POO
            ===================================
            Menú de opciones:\n
            1. Realizar reserva
            2. Registrar usuario
            3. Cancelar reserva
            4. Reservar restaurante
            5. Reservar zonas de entretenimiento
            6. Comprar servicios de turismo
            7. Alquilar vehículos 
            8. Agendar servicios de belleza
            9. Agendar uso de la lavandería 
            10.Agendar servicio de limpieza cuarto
            11.Realizar check-out
            12.Escribir sugerencias
            13.Salir
            
            ===================================
            """)

    def registrar_usuario(self):
        print("\n>>> REGISTRAR USUARIO")
        cedula = input("Ingrese la cédula: ")
        nombre = input("Ingrese el nombre: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
        numero_habitacion = input("Ingrese el número de habitación: ")
        if self.hotel.registrar_usuario(cedula, nombre, fecha_nacimiento, numero_habitacion):
            print("INFO: El usuario se registró exitosamente")
        else:
            print(f"ERROR: Ya existe un usuario con la cédula {cedula}")

    def realizar_reserva(self):
        print("\n>>> REALIZAR RESERVA")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        nombre = input("Ingrese su nombre: ")
        cantidad_noches = int(input("Ingrese la cantidad de noches de estadía: "))
        cantidad_personas = int(input("Ingrese la cantidad de personas que harán parte de la reserva: "))
        numero_habitacion = self.hotel.numero_habitacion
        if self.hotel.realizar_reserva(cedula, nombre, cantidad_noches, cantidad_personas):
            print(f"INFO: La reserva se ha completado exitosamente y su número de habitación es {numero_habitacion} ")
        else:
            print("INFO: No se pudo completar la reserva ya que la cédula ingresada se encuentra registrada")

    def cancelar_reserva(self):
        print("\n>>> CANCELAR RESERVA")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        if self.hotel.cancelar_reserva(cedula):
            print(f"INFO: La reserva ha sido cancelada con exito")
        else:
            print(f"INFO: La reserva no ha podido ser cancelada")

    def reserva_restaurante(self):
        print("\n>>> REALIZAR RESERVA DE RESTAURANTE")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        hora_reserva = input("Ingrese la hora de la reserva: ")
        cantidad_personas = int(input("Ingrese la cantidad de personas que asistirán a la reserva: "))
        if self.hotel.reservar_restaurante(cedula, hora_reserva, cantidad_personas):
            print(f"INFO: La reserva se ha completado exitosamente")
        else:
            print(f"INFO: No se pudo completar la reserva ya que la cédula ingresada no se encuentra registrada")

    def reservar_zona_entretenimiento(self):
        print("\n>>> REALIZAR RESERVA DE ZONA DE ENTRETENIMIENTO")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        hora_reserva = input("Ingrese la hora de la reserva: ")
        cantidad_personas = int(input("Ingrese la cantidad de personas que asistirán a la reserva de zona de entretenimiento: "))
        self.opciones= print("Seleccione una opción:"), input(
        {
            "1": "zona_píscina",
            "2": "zona_juegos",
            "3": "zona_gimnasio"
        })
        if self.hotel.reservar_zona_entretenimiento(cedula, hora_reserva, cantidad_personas):
            print(f"INFO: La reserva se ha completado exitosamente")
        else:
            print(f"INFO: No se pudo completar la reserva ya que la cédula ingresada no se encuentra registrada")

    def reserva_servicio_turismo(self):
        print("\n>>> REALIZAR RESERVA DE SERVICIO DE TURISMO")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        hora_reserva = input("Ingrese la hora de la reserva: ")
        cantidad_personas = int(input("Ingrese la cantidad de personas que asistirán a el recorrido: "))
        self.opciones = print("Seleccione una opción:"), input({
            "1": "turismo_museo",
            "2": "turismo_isla",
            "3": "turismo_recorrido_ciudad"
        })
        if self.hotel.reserva_servicio_turismo(cedula, hora_reserva, cantidad_personas):
            print(f"INFO: La reserva se ha completado exitosamente")
        else:
            print(f"INFO: No se pudo completar la reserva ya que la cédula ingresada no se encuentra registrada")

    def reserva_vehiculo(self):
        print("\n>>> REALIZAR RESERVA DE ALQUILER DE VEHÍCULO")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        hora_reserva = input("Ingrese la hora de la reserva: ")
        cantidad_personas = int(input("Ingrese la cantidad de personas que asistirán a la reserva: "))
        self.opciones = print("Seleccione una opción"), input({
            "1": "toyota_corolla",
            "2": "Chevrolet_Sail",
            "3": "Renault Dupstep",
            "4": "Honda PCX",
            "5": "BMW G 310 R"
        })
        if self.hotel.reserva_vehiculo(cedula, hora_reserva, cantidad_personas, datos_tarjeta_bancaria):
            print(f"INFO: La reserva se ha completado exitosamente")
        else:
            print(f"INFO: No se pudo completar la reserva ya que la cédula ingresada no se encuentra registrada")

    def reserva_servicios_salon_belleza(self):
        print("\n>>> REALIZAR RESERVA DE SERVICIOS DE SALON BELLEZA")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        hora_reserva = input("Ingrese la hora de la reserva: ")
        cantidad_personas = int(input("Ingrese la cantidad de personas que asistirán a la reserva: "))
        self.opciones = print("Seleccione una opción"), input({
            "1": "Masaje",
            "2": "limpieza_facial"
        })
        if self.hotel.reserva_servicios_salon_belleza(cedula, hora_reserva, cantidad_personas):
            print(f"INFO: La reserva se ha completado exitosamente")
        else:
            print(f"INFO: No se pudo completar la reserva ya que la cédula ingresada no se encuentra registrada")
    def reserva_servicio_lavanderia(self):
        print("\n>>> REALIZAR RESERVA DE SERVICIOS DE LAVANDERÍA")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        hora_reserva = input("Ingrese la hora de la reserva: ")
        if self.hotel.reserva_servicio_lavanderia(cedula, hora_reserva):
            print(f"INFO: La reserva se ha completado exitosamente")
        else:
            print(f"INFO: No se pudo completar la reserva ya que la cédula ingresada no se encuentra registrada")
    def servicio_check_out(self):
        print("\n>>> REALIZAR CHECK-OUT")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        if self.hotel.servicio_check_out(cedula):
            print(f"INFO: El check-out se ha completado exitosamente")
        else:
            print(f"INFO: No se pudo completar el check-out ya que la cédula ingresada no se encuentra registrada")

    def servicio_limpieza_cuarto(self):
        print("\n>>> REALIZAR RESERVA DE SERVICIO DE LIMPIEZA DE CUARTO")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        hora_reserva = input("Ingrese la hora de la reserva: ")
        if self.hotel.servicio_limpieza_cuarto(cedula, hora_reserva):
            print(f"INFO: La reserva se ha completado exitosamente")
        else:
            print(f"INFO: No se pudo completar la reserva ya que la cédula ingresada no se encuentra registrada")
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f"ERROR: {opcion} no es una opción válida")

    def salir(self):
        print("\nMUCHAS GRACIAS POR USAR NUESTRA APLICACIÓN")
        sys.exit(0)
