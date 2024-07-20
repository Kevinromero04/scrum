import json
ruta = "Productos.json"

def guardar(datos):
    with open(ruta, "w") as file:
        json.dump(datos, file, indent=4)

def cargar():
    try:
        with open(ruta, "r") as leer:
            datos= json.load(leer)
            return datos
    except Exception:
        print("Error al guardar los datos")
