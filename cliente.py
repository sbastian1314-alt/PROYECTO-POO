from datetime import datetime, timedelta


class Cliente:

    def __init__(
        self,
        id_cliente,
        nombre,
        edad,
        contrasena
    ):

        #VALIDAR ID

        if not id_cliente.strip():
            raise ValueError(
                "El ID no puede estar vacío"
            )

        if not id_cliente.isdigit():
            raise ValueError(
                "El ID debe contener solo números"
            )

        #VALIDAR NOMBRE

        if not nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío"
            )

        if not nombre.replace(" ", "").isalpha():
            raise ValueError(
                "El nombre solo debe contener letras"
            )

        #VALIDAR EDAD

        if not isinstance(edad, int):
            raise TypeError(
                "La edad debe ser un número entero"
            )

        if edad <= 0 or edad > 120:
            raise ValueError(
                "La edad debe estar entre 1 y 120"
            )

        #VALIDAR CONTRASEÑA

        if not contrasena.strip():
            raise ValueError(
                "La contraseña no puede estar vacía"
            )

        if len(contrasena) < 4:
            raise ValueError(
                "La contraseña debe tener mínimo 4 caracteres"
            )

        #ATRIBUTOS

        self.id_cliente = id_cliente
        self.nombre = nombre
        self.edad = edad
        self.contrasena = contrasena

        self.pago_activo = False
        self.rutina_asignada = None

        #MEMBRESÍA

        self.estado_membresia = "Inactiva"

        self.fecha_vencimiento = None

        self.multa = 0

    #ACTUALIZAR PAGO

    def actualizar_pago(self):

        self.pago_activo = True

        self.estado_membresia = "Activa"

        self.fecha_vencimiento = (
            datetime.now() + timedelta(days=30)
        )

        self.multa = 0

    #VERIFICAR MEMBRESÍA

    def verificar_membresia(self):

        if (
            self.fecha_vencimiento
            and datetime.now() > self.fecha_vencimiento
        ):

            self.estado_membresia = "Vencida"

            self.multa = 20000

    #ASIGNAR RUTINA

    def asignar_rutina(self, rutina):

        self.rutina_asignada = rutina

    #MOSTRAR INFORMACIÓN

    def mostrar_info(self):

        self.verificar_membresia()

        rutina = (
            self.rutina_asignada.nombre_rutina
            if self.rutina_asignada
            else "Sin rutina"
        )

        estado_pago = (
            "Activo"
            if self.pago_activo
            else "Pendiente"
        )

        vencimiento = (
            self.fecha_vencimiento.strftime("%d/%m/%Y")
            if self.fecha_vencimiento
            else "No disponible"
        )

        print("\n------- CLIENTE -------")
        print(f"ID: {self.id_cliente}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Pago: {estado_pago}")
        print(f"Rutina: {rutina}")

        print(
            f"Membresía: {self.estado_membresia}"
        )

        print(
            f"Vencimiento: {vencimiento}"
        )

        print(f"Multa: ${self.multa}")

        print("------------------------")