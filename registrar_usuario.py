import cargar_guardar as car

def usuario():
    bibli = car.cargar()
    datos = {}
    documento = int(input("Digite su cedula "))
    datos["documento"] = documento
    if str(documento) in bibli["Usuarios"]:
        print("Ya hay un usuario registrado con ese documento")
    else:
        datos["Nombres"] = str(input("Digite sus nombres "))
        datos["Apellidos"] = str(input("Digite sus apellidos "))
    try:
        datos["Telefono"] = int(input("Digite su numero de telefono "))
    except Exception:
        print("numero invalido")
        bibli["Usuarios"][documento] = datos
        car.guardar(bibli)
        print("Felicitaciones su usuario se ha creado satisfactoriamente ")
        print("*******************************************")

