class Rutina:

    def __init__(self, nombre_rutina, objetivo, duracion):

        #VALIDAR NOMBRE

        if not nombre_rutina.strip():
            raise ValueError(
                "El nombre de la rutina no puede estar vacio"
            )

        #VALIDAR OBJETIVO

        if not objetivo.strip():
            raise ValueError(
                "El objetivo no puede estar vacio"
            )

        if not objetivo.replace(" ", "").isalpha():
            raise ValueError(
                "¡El objetivo solo debe contener letras!"
            )

        #VALIDAR DURACIÓN

        if not isinstance(duracion, int):
            raise TypeError("La duracion debe ser un número entero")

        if duracion <= 0:
            raise ValueError("La duracion debe ser mayor a 0")

        #ATRIBUTOS

        self.nombre_rutina = nombre_rutina
        self.objetivo = objetivo
        self.duracion = duracion

    #MOSTRAR INFO

    def mostrar_rutina(self):

        print("---------- RUTINA ---------")
        print(f"Nombre: {self.nombre_rutina}")
        print(f"Objetivo: {self.objetivo}")
        print(f"Duración: {self.duracion} minutos")
        print("----------------------------")