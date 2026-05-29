from datetime import datetime


class Pago:

    def __init__(self, cliente, valor, fecha):

        #VALIDAR CLIENTE 

        if cliente is None:
            raise ValueError(
                "El cliente no puede estar vacío"
            )

        #VALIDAR VALOR

        if not isinstance(valor, (int, float)):
            raise TypeError(
                "El valor debe ser numérico"
            )

        if valor <= 0:
            raise ValueError(
                "El valor del pago debe ser mayor a 0"
            )

        #VALIDAR FECHA

        if not fecha.strip():
            raise ValueError(
                "La fecha no puede estar vacía"
            )

        try:
            datetime.strptime(fecha, "%d/%m/%Y")

        except ValueError:
            raise ValueError(
                "La fecha debe tener formato DD/MM/YYYY"
            )

        #ATRIBUTOS

        self.cliente = cliente
        self.valor = valor
        self.fecha = fecha
        self.estado = "Pagado"

    #MOSTRAR INFORMACIÓN 

    def mostrar_pago(self):

        print("----------- PAGO -----------")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Valor: ${self.valor}")
        print(f"Fecha: {self.fecha}")
        print(f"Estado: {self.estado}")
        print("-----------------------------")