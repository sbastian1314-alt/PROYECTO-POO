from gimnasio import Gimnasio
from cliente import Cliente
from entrenador import Entrenador
from rutina import Rutina

from login import (
    login_admin,
    login_cliente
)


gimnasio = Gimnasio()


#MENÚ ADMIN

def menu_admin():

    while True:

        print("------------------------------------")
        print("          MENÚ ADMIN")
        print("------------------------------------")
        print("1. Registrar cliente")
        print("2. Registrar entrenador")
        print("3. Crear rutina")
        print("4. Asignar rutina")
        print("5. Registrar pago")
        print("6. Ver clientes")
        print("7. Ver rutinas")
        print("8. Ver entrenadores")
        print("9. Ver pagos")
        print("10. Buscar cliente")
        print("11. Buscar entrenador")
        print("12. Ver estadísticas")
        print("13. Editar cliente")
        print("14. Eliminar cliente")
        print("15. Editar entrenador")
        print("16. Eliminar entrenador")
        print("17. Cerrar sesion")
        print("------------------------------------")

        opcion = input(
            "Seleccione una opcion: "
        ).strip()

        #REGISTRAR CLIENTE

        if opcion == "1":

            try:

                id_cliente = input(
                    "ID del cliente: "
                ).strip()

                nombre = input(
                    "Nombre del cliente: "
                ).strip()

                edad_input = input(
                    "Edad: "
                ).strip()

                if not edad_input:
                    raise ValueError(
                        "La edad no puede estar vacia"
                    )

                if not edad_input.isdigit():
                    raise ValueError(
                        "La edad debe contener solo numeros"
                    )

                edad = int(edad_input)

                if edad <= 0:
                    raise ValueError("La edad debe ser mayor a 0")

                contrasena = input(
                    "Contraseña: "
                ).strip()

                cliente = Cliente(
                    id_cliente,
                    nombre,
                    edad,
                    contrasena
                )

                gimnasio.registrar_cliente(cliente)

            except ValueError as error:
                print(f"XX-Error: {error}-XX")

        #REGISTRAR ENTRENADOR

        elif opcion == "2":

            try:

                id_entrenador = input(
                    "ID del entrenador: "
                ).strip()

                nombre = input(
                    "Nombre del entrenador: "
                ).strip()

                especialidad = input(
                    "Especialidad: "
                ).strip()

                entrenador = Entrenador(
                    id_entrenador,
                    nombre,
                    especialidad
                )

                gimnasio.registrar_entrenador(
                    entrenador
                )

            except ValueError as error:
                print(f"XX-Error: {error}-XX")

        #CREAR RUTINA

        elif opcion == "3":

            try:

                nombre_rutina = input(
                    "Nombre de la rutina: "
                ).strip()

                objetivo = input(
                    "Objetivo: "
                ).strip()

                duracion_input = input(
                    "Duracion en minutos: "
                ).strip()

                if not duracion_input:
                    raise ValueError(
                        "La duracion no puede estar vacia"
                    )

                if not duracion_input.isdigit():
                    raise ValueError(
                        "La duracion debe contener solo numeros"
                    )

                duracion = int(duracion_input)

                if duracion <= 0:
                    raise ValueError(
                        "La duracion debe ser mayor a 0"
                    )

                rutina = Rutina(
                    nombre_rutina,
                    objetivo,
                    duracion
                )

                gimnasio.crear_rutina(rutina)

            except ValueError as error:
                print(f"XX-Error: {error}-XX")

        #ASIGNAR RUTINA

        elif opcion == "4":

            id_cliente = input(
                "ID del cliente: "
            ).strip()

            if not id_cliente.isdigit():

                print("XX-El ID debe contener solo números-XX")

                continue

            nombre_rutina = input("Nombre de la rutina: ").strip()

            gimnasio.asignar_rutina(
                id_cliente,
                nombre_rutina
            )

        #REGISTRAR PAGO

        elif opcion == "5":

            try:

                id_cliente = input("ID del cliente: ").strip()

                if not id_cliente.isdigit():

                    raise ValueError("El ID debe contener solo números")

                valor_input = input("Valor del pago: ").strip()

                if not valor_input:
                    raise ValueError("El valor no puede estar vacío")

                if not valor_input.replace(".", "").isdigit():

                    raise ValueError(
                        "El valor debe contener solo números"
                    )

                valor = float(valor_input)

                if valor <= 0:
                    raise ValueError(
                        "El valor debe ser mayor a 0"
                    )

                fecha = input(
                    "Fecha (DD/MM/YYYY): "
                ).strip()

                gimnasio.registrar_pago(
                    id_cliente,
                    valor,
                    fecha
                )

            except ValueError as error:
                print(f"XX-Error: {error}-XX")

        #MOSTRAR CLIENTES

        elif opcion == "6":

            gimnasio.mostrar_clientes()

        #MOSTRAR RUTINAS

        elif opcion == "7":

            gimnasio.mostrar_rutinas()

        #MOSTRAR ENTRENADORES 

        elif opcion == "8":

            gimnasio.mostrar_entrenadores()

        #MOSTRAR PAGOS

        elif opcion == "9":

            gimnasio.mostrar_pagos()

        #BUSCAR CLIENTE

        elif opcion == "10":

            while True:

                print("------- BUSCAR CLIENTE -------")
                print("1. Buscar por ID")
                print("2. Buscar por nombre")
                print("3. Volver")

                tipo_busqueda = input(
                    "Seleccione una opción: "
                ).strip()

                #BUSCAR POR ID

                if tipo_busqueda == "1":

                    id_cliente = input(
                        "Ingrese el ID: "
                    ).strip()

                    if not id_cliente.isdigit():

                        print("XX-El ID debe contener solo números-XX")

                        continue

                    cliente = gimnasio.buscar_cliente(
                        id_cliente
                    )

                    if cliente:

                        cliente.mostrar_info()

                    else:

                        print(
                            "XX-Cliente no encontrado-XX"
                        )

                #BUSCAR POR NOMBRE

                elif tipo_busqueda == "2":

                    nombre = input(
                        "Ingrese el nombre: "
                    ).strip()

                    if not nombre:

                        print(
                            "XX-El nombre no puede estar vacío-XX"
                        )

                        continue

                    clientes = (
                        gimnasio.buscar_cliente_por_nombre(
                            nombre
                        )
                    )

                    if clientes:

                        for cliente in clientes:

                            cliente.mostrar_info()

                    else:

                        print("XX-Cliente no encontrado-XX")

                #VOLVER

                elif tipo_busqueda == "3":

                    break

                else:

                    print("XX-Opción inválida-XX")

        #BUSCAR ENTRENADOR

        elif opcion == "11":

            while True:

                print("------- BUSCAR ENTRENADOR -------")
                print("1. Buscar por ID")
                print("2. Buscar por nombre")
                print("3. Volver")

                tipo_busqueda = input("Seleccione una opcion: ").strip()

                #BUSCAR POR ID

                if tipo_busqueda == "1":

                    id_entrenador = input(
                        "Ingrese el ID: "
                    ).strip()

                    if not id_entrenador.isdigit():

                        print("XX-El ID debe contener solo números-XX")

                        continue

                    entrenador = (
                        gimnasio.buscar_entrenador(
                            id_entrenador
                        )
                    )

                    if entrenador:

                        entrenador.mostrar_info()

                    else:

                        print("XX-Entrenador no encontrado-XX")

                #BUSCAR POR NOMBRE 

                elif tipo_busqueda == "2":

                    nombre = input(
                        "Ingrese el nombre: "
                    ).strip()

                    if not nombre:

                        print("XX-El nombre no puede estar vacío-XX")

                        continue

                    entrenadores = (
                        gimnasio.buscar_entrenador_por_nombre(
                            nombre
                        )
                    )

                    if entrenadores:

                        for entrenador in entrenadores:

                            entrenador.mostrar_info()

                    else:

                        print("XX-Entrenador no encontrado-XX")

                #VOLVER

                elif tipo_busqueda == "3":

                    break

                else:

                    print(
                        "XX-Opción inválida-XX"
                    )

        #VER ESTADÍSTICAS

        elif opcion == "12":

            gimnasio.mostrar_estadisticas()

        #EDITAR CLIENTE

        elif opcion == "13":

            try:

                id_cliente = input(
                    "ID del cliente a editar: "
                ).strip()

                if not id_cliente.isdigit():

                    raise ValueError("¡El ID debe contener solo números!")

                cliente = gimnasio.buscar_cliente(
                    id_cliente
                )

                if not cliente:

                    print("XX-Cliente no encontrado-XX")

                    continue

                nuevo_nombre = input("Nuevo nombre: ").strip()

                if not nuevo_nombre.replace(" ","").isalpha():

                    raise ValueError("¡El nombre solo debe contener letras!")

                nueva_edad_input = input("Nueva edad: ").strip()

                if not nueva_edad_input.isdigit():

                    raise ValueError("¡La edad debe contener solo números!")

                nueva_edad = int(nueva_edad_input)

                if nueva_edad <= 0:

                    raise ValueError("La edad debe ser mayor a 0")

                nueva_contrasena = input("Nueva contraseña: ").strip()

                if len(nueva_contrasena) < 4:

                    raise ValueError("La contraseña debe tener mínimo 4 caracteres")

                gimnasio.editar_cliente(
                    id_cliente,
                    nuevo_nombre,
                    nueva_edad,
                    nueva_contrasena
                )

            except ValueError as error:

                print(f"XX-Error: {error}-XX")

        #ELIMINAR CLIENTE

        elif opcion == "14":

            id_cliente = input("ID del cliente a eliminar: ").strip()

            if not id_cliente.isdigit():

                print("XX-El ID debe contener solo números-XX")

                continue

            gimnasio.eliminar_cliente(
                id_cliente
            )

        #EDITAR ENTRENADOR

        elif opcion == "15":

            try:

                id_entrenador = input("ID del entrenador a editar: ").strip()

                if not id_entrenador.isdigit():

                    raise ValueError("!El ID debe contener solo números¡")

                entrenador = gimnasio.buscar_entrenador(
                    id_entrenador
                )

                if not entrenador:

                    print("XX-Entrenador no encontrado-XX")

                    continue

                nuevo_nombre = input("Nuevo nombre: ").strip()

                if not nuevo_nombre.replace(" ","").isalpha():

                    raise ValueError("El nombre solo debe contener letras")

                nueva_especialidad = input("Nueva especialidad: ").strip()

                if not nueva_especialidad.replace(" ","").isalpha():

                    raise ValueError("¡La especialidad solo debe contener letras!")

                gimnasio.editar_entrenador(
                    id_entrenador,
                    nuevo_nombre,
                    nueva_especialidad
                )

            except ValueError as error:

                print(f"XX-Error: {error}-XX")

        #ELIMINAR ENTRENADOR

        elif opcion == "16":

            id_entrenador = input("ID del entrenador a eliminar: ").strip()

            if not id_entrenador.isdigit():

                print("XX-El ID debe contener solo números-XX")

                continue

            gimnasio.eliminar_entrenador(id_entrenador)

        #CERRAR SESIÓN

        elif opcion == "17":

            print("Cerrando sesión...")
            break

        else:

            print("XX-Opción inválida-XX")


#MENÚ CLIENTE

def menu_cliente(cliente):

    while True:

        print("-----------------------------------")
        print(f"      BIENVENIDO {cliente.nombre}")
        print("-----------------------------------")
        print("1. Ver mi informacion")
        print("2. Cerrar sesion")
        print("------------------------------------")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":

            cliente.mostrar_info()

        elif opcion == "2":

            print("Cerrando sesión...")
            break

        else:

            print("XX-Opción inválida-XX")


#LOGIN PRINCIPAL

while True:

    print("------------------------------------")
    print("      SISTEMA DE GIMNASIO")
    print("------------------------------------")
    print("1. Iniciar sesion")
    print("2. Salir")
    print("------------------------------------")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":

        usuario = input(
            "Usuario: "
        ).strip()

        if not usuario:

            print(
                "¡El usuario no puede estar vacío!"
            )

            continue

        contrasena = input("Contraseña: ").strip()

        if not contrasena:

            print("La contraseña no puede estar vacía")

            continue

        if login_admin(
            usuario,
            contrasena
        ):

            print("Bienvenido administrador")

            menu_admin()

        else:

            cliente = login_cliente(
                gimnasio.lista_clientes,
                usuario,
                contrasena
            )

            if cliente:

                print(f"Bienvenido {cliente.nombre}")

                menu_cliente(cliente)

            else:

                print("Usuario o contraseña incorrectos")

    elif opcion == "2":

        print("Saliendo del sistema...")
        break

    else:

        print("XX-Opción inválida-XX")