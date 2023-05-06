# test(), que creará las instancias de las clases con datos de prueba, para validar que las funcionalidades fueron testeadas en su totalidad, con datos correctos e incorrectos

import Email
import csv


def test():

    idCuenta = str(input("Ingrese el id de la cuenta: "))
    dominio = str(input("Ingrese el dominio: "))
    tipodom = str(input("Ingrese el tipo de dominio: "))
    contrasena = str(input("Ingrese la contraseña: "))
    email1 = Email.eMail(idCuenta, dominio, tipodom, contrasena)
    print(email1.retornaEmail())

    nombre = str(input("Ingrese su nombre: "))
    direccionCorreo = str(input("Ingrese su direccion de correo electronico: "))
    email2 = Email.eMail()
    email2.crearCuenta(direccionCorreo)
    print("Estimado"+ nombre + ", te enviaremos tus mensajes a la direccion " + email2.retornaEmail())

    contrasenaActual = str(input("Ingrese su contraseña actual: "))
    email3 = Email.eMail ()
    email3.cambiarContrasena(contrasenaActual)

    email4 = Email.eMail()
    direccionCorreo4 = "informatica.fcefn@gmail.com"
    email4.crearCuenta(direccionCorreo4)
    print(email4.retornaEmail())

def archivoEmails():
    emailvalido = []
    archivo = open('emails.csv')    
    reader = csv.reader(archivo)
    for fila in reader: 
        if "@" in fila[0] and "." in fila[0]:
            
            print("Direccion de email correcta: {}" .format(fila[0]))
            emails = Email.eMail()
            emails.crearCuenta(fila[0])
            emailvalido.append(emails)

        else:
            print("Direccion de email incorrecta: {}".format(fila[0]))

    archivo.close()

    bdominio= str(input("Ingrese un dominio a buscar: "))
    emaildominio = 0
    email = Email.eMail()
    for email in emailvalido:
        if bdominio == email.getDominio():
            emaildominio += 1
    print("Hay {} direcciones de email con el dominio {}." .format(emaildominio, bdominio))



if __name__== '__main__':
    
    #test()
    archivoEmails()
