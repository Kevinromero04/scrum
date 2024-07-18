import cargar_guardar as car
def ingreso():
    bibli = car.cargar()
    contra = str(input("Digite la contraseña "))
    if str(contra) in bibli["Administrador"]:
        print("Bienvenido Jefe")
    else:
        print("Contraseña incorrecta")

ingreso()