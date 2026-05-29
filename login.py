#LOGIN ADMINISTRADOR

def login_admin(usuario, contrasena):

    ADMIN_USUARIO = "admin"
    ADMIN_CONTRASENA = "admin123"

    return (
        usuario == ADMIN_USUARIO
        and contrasena == ADMIN_CONTRASENA
    )


#LOGIN CLIENTE

def login_cliente(lista_clientes, usuario, contrasena):

    for cliente in lista_clientes:

        if (
            cliente.id_cliente == usuario
            and cliente.contrasena == contrasena
        ):

            return cliente

    return None