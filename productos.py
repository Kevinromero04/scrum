import Pro_carga_guarda as car
import json
def crear():
    bibli = car.cargar()
    nuevo = str(input("Que productos deseas colocar: "))
    bibli[nuevo]={}
    car.guardar(bibli)



#crear()












def menu_dis():
    muestra = car.cargar()
    for categoria, items in muestra.items():
        print("Productos", categoria)

def cambi_cel():
    file = open("Productos.json")
    regis = json.load(file)
    for llave, clave in regis["Celulares"].items():
        print(llave)
def cambi_PC():
    file = open("Productos.json")
    regis = json.load(file)
    for llave, clave in regis["PC"].items():
        print(llave)

def cambi_tablets(electrodomestico):
    file = open("Productos.json")
    regis = json.load(file)
    for llave, clave in regis[electrodomestico].items():
        print(llave)


def cambi_referencia():
    file = open("Productos.json")
    regis = json.load(file)
    for llave, clave in regis["Celulares"].items():
        for uno in clave:
            print(uno)





def menu_cambio():
    cambio = ["1. Precio", "2. Cantidad", "3. Salir"]
    for k in cambio:
        print(k)


def agregar_producto():
    bibli = car.cargar()
    menu_dis()
    produc = str(input("Introduzca el electrodomestico al que quieres agregar el dispositivo: "))
    if produc in bibli:
        numero = int(input("Marca 1 para crearlo desde 0, Marca 2 para agregar referencia: "))
        if numero ==1:
            Marca = input("Dgigite la marca del caelular que quieres agregar: ")
            Referencia= input("Coloca la referecia que quieres agregar: ")
            bibli[produc][Marca] ={}
            car.guardar(bibli)
            bibli[produc][Marca][Referencia]={}
            car.guardar(bibli)
            datos ={}
            datos["Precio"] = int(input("Digite el precio: "))
            datos["Cantidad"] = int(input("Digite la cantidad: "))
            bibli[produc][Marca][Referencia] = datos
            car.guardar(bibli)
            print("Producto guardado")
            print("*******************************************")
        elif numero ==2:
            car.guardar(bibli)
            Marca = input("Digite la marca que quieres agregar la referencia: ")
            if Marca in bibli[produc]:
                Referencia= input("Coloca la referecia que quieres agregar: ")
                bibli[produc][Marca][Referencia]={}
                car.guardar(bibli)
                datos ={}
                datos["Precio"] = int(input("Digite el precio: "))
                datos["Cantidad"] = int(input("Digite la cantidad: "))
                bibli[produc][Marca][Referencia] = datos
                car.guardar(bibli)
                print("Producto guardado")
                print("*******************************************")

    else:
        print("Este electrodomestico no existe o no colocaste bien el nombre")
        print("*******************************************")


#agregar_producto()



















def modificar_producto():
    bibli = car.cargar()
    menu_dis()
    electrodomestico = str(input("Introduzca el producto al que quiere modificar: "))
    if electrodomestico in bibli:
        cambi_tablets(electrodomestico)
        Marca = str(input("Introduzca la marca que quieres modificar o cantidad: "))
        if Marca in bibli[electrodomestico]:
            cambi_referencia()
            referencia =str(input("Introduzca la referencia: "))
            if referencia in bibli[electrodomestico][Marca]:
                menu_cambio()
                cambiar = int(input("Digite una opcion: "))
                if cambiar == 1:
                    nueva = int(input("Digite el nuevo precio: "))
                    bibli[electrodomestico][Marca][referencia]["Precio"] = nueva
                    car.guardar(bibli)

                elif cambiar ==2:
                    nueva = int(input("Digite la cantidad que quieres agregar: "))
                    bibli[electrodomestico][Marca][referencia]["Cantidad"] = nueva
                    car.guardar(bibli)

                elif cambiar ==3:
                    print("Saliendo..")
            else:
                print("Digite una opcion valida")
        else:
            print("Coloca bien el nombre")
    else:
        print("Coloca bien el nombre del producto")

#modificar_producto()