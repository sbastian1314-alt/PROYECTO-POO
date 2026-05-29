class Entrenador:

    def __init__(self, id_entrenador, nombre, especialidad):

        #VALIDAR ID

        if not id_entrenador.strip():
            raise ValueError("El ID no puede estar vacío")

        if not id_entrenador.isdigit():
            raise ValueError("El ID debe contener solo números")

        #VALIDAR NOMBRE

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if not nombre.replace(" ", "").isalpha():
            raise ValueError(
                "El nombre solo debe contener letras"
            )

        #VALIDAR ESPECIALIDAD

        if not especialidad.strip():
            raise ValueError(
                "La especialidad no puede estar vacía"
            )

        if not especialidad.replace(" ", "").isalpha():
            raise ValueError(
                "La especialidad solo debe contener letras"
            )

        #ATRIBUTOS

        self.id_entrenador = id_entrenador
        self.nombre = nombre
        self.especialidad = especialidad

    #MOSTRAR INFO 

    def mostrar_info(self):

        print("-------- ENTRENADOR --------")
        print(f"ID: {self.id_entrenador}")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print("----------------------------")