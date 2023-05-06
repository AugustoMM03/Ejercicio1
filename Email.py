class eMail:
    __idCuenta = ''
    __dominio =  ''
    __tipodom = ''
    __contrasena = ''
    def __init__(self="", idcuenta="", dominio="", tipodom="", contrasena=""):
        self.__idCuenta = idcuenta
        self.__dominio = dominio
        self.__tipodom = tipodom
        self.__contrasena = contrasena
    
    def retornaEmail(self):
        return(self.__idCuenta + "@" + self.__dominio + '.' + self.__tipodom)

    def getDominio(self):
        return("El dominio es: ()", self.__dominio)

    def crearCuenta(self, direccionCorreo):
        partes = direccionCorreo.split("@")
        self.__idCuenta = partes[0]
        partes2 = partes[1].split(".")
        self.__dominio = partes2[0]
        self.__tipodom = partes2[1]
        self.__contrasena = str(input("Ingrese una contraseña para la cuenta: "))


    def cambiarContrasena(self, contrasenaV):
        if(contrasenaV == self.__contrasena):
            self.__contrasena = str(input("Ingrese la nueva contraseña "))
        else:
            ("La contraseña ingresada no coincide con la contraseña de la cuenta.")

    def fromAddress(cls, direccion):
        idCuenta, dominio, tipoDominio = direccion.split("@")
        return cls(idCuenta, dominio, tipoDominio, "")