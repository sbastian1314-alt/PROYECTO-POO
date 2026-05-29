from pago import Pago


class Gimnasio:

    def __init__(self):

        self.lista_clientes = []
        self.lista_entrenadores = []
        self.lista_rutinas = []
        self.lista_pagos = []

    #BUSCAR CLIENTE POR ID

    def buscar_cliente(self, id_cliente):

        for cliente in self.lista_clientes:

            if cliente.id_cliente == id_cliente:
                return cliente

        return None

    #BUSCAR CLIENTE POR NOMBRE

    def buscar_cliente_por_nombre(self, nombre):

        clientes_encontrados = []

        for cliente in self.lista_clientes:

            if cliente.nombre.lower() == nombre.lower():

                clientes_encontrados.append(cliente)

        return clientes_encontrados

    #BUSCAR ENTRENADOR POR ID

    def buscar_entrenador(self, id_entrenador):

        for entrenador in self.lista_entrenadores:

            if (
                entrenador.id_entrenador
                == id_entrenador
            ):

                return entrenador

        return None

    #BUSCAR ENTRENADOR POR NOMBRE

    def buscar_entrenador_por_nombre(
        self,
        nombre
    ):

        entrenadores_encontrados = []

        for entrenador in self.lista_entrenadores:

            if entrenador.nombre.lower() == nombre.lower():

                entrenadores_encontrados.append(
                    entrenador
                )

        return entrenadores_encontrados

    #BUSCAR RUTINA

    def buscar_rutina(self, nombre_rutina):

        for rutina in self.lista_rutinas:

            if (
                rutina.nombre_rutina.lower()
                == nombre_rutina.lower()
            ):

                return rutina

        return None

    #REGISTRAR CLIENTE

    def registrar_cliente(self, cliente):

        if self.buscar_cliente(
            cliente.id_cliente
        ):

            print(
                "XX-Error: el cliente ya existe-XX"
            )

            return

        self.lista_clientes.append(cliente)

        print(
            "¡Cliente registrado correctamente!"
        )

    #EDITAR CLIENTE

    def editar_cliente(
        self,
        id_cliente,
        nuevo_nombre,
        nueva_edad,
        nueva_contrasena
    ):

        cliente = self.buscar_cliente(
            id_cliente
        )

        if not cliente:

            print(
                "¡Cliente no encontrado!"
            )

            return

        cliente.nombre = nuevo_nombre
        cliente.edad = nueva_edad
        cliente.contrasena = nueva_contrasena

        print(
            "¡Cliente actualizado correctamente!"
        )

    #ELIMINAR CLIENTE

    def eliminar_cliente(self, id_cliente):

        cliente = self.buscar_cliente(
            id_cliente
        )

        if not cliente:

            print(
                "¡Cliente no encontrado!"
            )

            return

        self.lista_clientes.remove(cliente)

        print(
            "¡Cliente eliminado correctamente!"
        )

    #REGISTRAR ENTRENADOR

    def registrar_entrenador(
        self,
        entrenador
    ):

        if self.buscar_entrenador(
            entrenador.id_entrenador
        ):

            print(
                "¡Error: el entrenador ya existe!"
            )

            return

        self.lista_entrenadores.append(
            entrenador
        )

        print(
            "¡Entrenador registrado correctamente!"
        )

    #EDITAR ENTRENADOR

    def editar_entrenador(
        self,
        id_entrenador,
        nuevo_nombre,
        nueva_especialidad
    ):

        entrenador = self.buscar_entrenador(
            id_entrenador
        )

        if not entrenador:

            print(
                "¡Entrenador no encontrado!"
            )

            return

        entrenador.nombre = nuevo_nombre
        entrenador.especialidad = (
            nueva_especialidad
        )

        print(
            "¡Entrenador actualizado correctamente!"
        )

    # ===== ELIMINAR ENTRENADOR =====

    def eliminar_entrenador(
        self,
        id_entrenador
    ):

        entrenador = self.buscar_entrenador(
            id_entrenador
        )

        if not entrenador:

            print(
                "¡Entrenador no encontrado!"
            )

            return

        self.lista_entrenadores.remove(
            entrenador
        )

        print(
            "¡Entrenador eliminado correctamente!"
        )

    #CREAR RUTINA

    def crear_rutina(self, rutina):

        if self.buscar_rutina(
            rutina.nombre_rutina
        ):

            print(
                "XX-Error: la rutina ya existe-XX"
            )

            return

        self.lista_rutinas.append(rutina)

        print(
            "¡Rutina creada correctamente!"
        )

    #ASIGNAR RUTINA

    def asignar_rutina(
        self,
        id_cliente,
        nombre_rutina
    ):

        cliente = self.buscar_cliente(
            id_cliente
        )

        rutina = self.buscar_rutina(
            nombre_rutina
        )

        if not cliente:

            print(
                "¡Cliente no encontrado!"
            )

            return

        if not rutina:

            print(
                "¡Rutina no encontrada!"
            )

            return

        cliente.asignar_rutina(rutina)

        print(
            "¡Rutina asignada correctamente!"
        )

    #REGISTRAR PAGO

    def registrar_pago(
        self,
        id_cliente,
        valor,
        fecha
    ):

        cliente = self.buscar_cliente(
            id_cliente
        )

        if not cliente:

            print(
                "Cliente no encontrado"
            )

            return

        pago = Pago(
            cliente,
            valor,
            fecha
        )

        self.lista_pagos.append(pago)

        cliente.actualizar_pago()

        print(
            "¡Pago registrado correctamente!"
        )

    #MOSTRAR CLIENTES

    def mostrar_clientes(self):

        if not self.lista_clientes:

            print(
                "¡No hay clientes registrados!"
            )

            return

        for cliente in self.lista_clientes:

            cliente.mostrar_info()

    #MOSTRAR ENTRENADORES

    def mostrar_entrenadores(self):

        if not self.lista_entrenadores:

            print(
                "¡No hay entrenadores registrados!"
            )

            return

        for entrenador in self.lista_entrenadores:

            entrenador.mostrar_info()

    #MOSTRAR RUTINAS

    def mostrar_rutinas(self):

        if not self.lista_rutinas:

            print(
                "¡No hay rutinas registradas!"
            )

            return

        for rutina in self.lista_rutinas:

            rutina.mostrar_rutina()

    #MOSTRAR PAGOS

    def mostrar_pagos(self):

        if not self.lista_pagos:

            print(
                "¡No hay pagos registrados!"
            )

            return

        for pago in self.lista_pagos:

            pago.mostrar_pago()

    #MOSTRAR ESTADÍSTICAS

    def mostrar_estadisticas(self):

        total_clientes = len(
            self.lista_clientes
        )

        total_entrenadores = len(
            self.lista_entrenadores
        )

        total_rutinas = len(
            self.lista_rutinas
        )

        total_pagos = len(
            self.lista_pagos
        )

        dinero_recaudado = 0

        for pago in self.lista_pagos:

            dinero_recaudado += pago.valor

        membresias_activas = 0
        membresias_vencidas = 0

        total_multas = 0

        for cliente in self.lista_clientes:

            cliente.verificar_membresia()

            if cliente.estado_membresia == "Activa":

                membresias_activas += 1

            elif (
                cliente.estado_membresia
                == "Vencida"
            ):

                membresias_vencidas += 1

            total_multas += cliente.multa

        print(
            "------------ ESTADISTICAS ------------"
        )

        print(
            f"Total clientes: {total_clientes}"
        )

        print(
            f"Total entrenadores: {total_entrenadores}"
        )

        print(
            f"Total rutinas: {total_rutinas}"
        )

        print(
            f"Pagos registrados: {total_pagos}"
        )

        print(
            f"Dinero recaudado: ${dinero_recaudado}"
        )

        print(
            f"Membresias activas: {membresias_activas}"
        )

        print(
            f"Membresias vencidas: {membresias_vencidas}"
        )

        print(
            f"Total multas: ${total_multas}"
        )

        print(
            "------------------------------"
        )