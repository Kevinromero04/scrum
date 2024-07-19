import cargar_guardar as car
def ingreso():
    while True:
        try:
            bibli = car.cargar()
            contra = str(input("Digite la contraseña: "))
            if str(contra) in bibli["Administrador"]:
                print("Bienvenido Administrador")
            else:
                print("Contraseña incorrecta")
        except Exception:
            print("Algo salio mal intenta de nuevo")

def regis_admin():
    while True:
        try: 

            bibli = car.cargar()
            datos = {}
            documento = int(input("Digite su cedula: "))
            contraseña = input("Agregar contraseña: ")
            datos["documento"] = documento
            if str(documento) in bibli["Usuarios"]:
                print("Ya hay un usuario registrado con ese documento")
            else:
                datos["Nombres"] = str(input("Digite sus nombres: "))
                datos["Apellidos"] = str(input("Digite sus apellidos: "))
                datos["Telefono"] = int(input("Digite su numero de telefono: "))
                bibli["Administrador"][contraseña] = datos
                car.guardar(bibli)
                print("Felicitaciones su usuario se ha creado satisfactoriamente ")
                print("*******************************************")
        except Exception:
                    print("Porfavor ingrese sus datos bien, algo salio mal")


