import json
import sys, os

BASE = 'data/'
global count
count = 0

# PANTALLA

def clear_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")


def pause_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")

# GENERALES

def check_file(archivo: str, data):
    if (not (os.path.isfile(BASE + archivo))):
        with open(BASE + archivo, "w") as bw:
            json.dump(data, bw, indent=4)

def read_file(archivo: str):
    with open(BASE+archivo, 'r') as rf:
        inventario = json.load(rf)
    return inventario

def update_file(archivo, data):
    with open(BASE + archivo, 'w') as fw:
        json.dump(data, fw, indent=4)

def edit_file_apz(nombre):

    if nombre == 'ACTIVOS':
        msg = 'Ingrese el "Código Campus" del activo que va a editar\n-> '
    elif nombre == 'PERSONAL':
        msg = 'Ingrese el "id" de la persona que va a editar\n-> '
    elif nombre == 'ZONAS':
        msg = 'Ingrese el "Número de zona" de la zona que va a editar\n-> '

    inventario = read_file('inventario.json')

    palabra = input(msg)
    
    if nombre.lower() in inventario:
        if palabra in inventario[nombre.lower()]:
            data = inventario[nombre.lower()][palabra]

            for key, value in data.items():
                if key not in ['cod_campus', 'nro_formulario', 'estado', 'id', 'Nro Zona', 'Ex CPU', 'Ex MON', 'Ex MOU', 'Ex TEC']:
                    if type(data[key]) == dict:
                        if(type(data[key]) == dict):
                            for key2 in data[key].keys():
                                if input(f'Desea modificar el {key2}? s(si) / Enter(no)\n-> ').lower() == 's':
                                    os.system('cls')
                                    data[key][key2] = input(f'Ingrese el nuevo valor para {key2} :')
                                    os.system('cls')
                    else:
                        if input(f'Desea modificar el {key}? s(si) / Enter(no)\n-> ').lower() == 's':
                            os.system('cls')
                            data[key] = input(f'Ingrese el nuevo valor para {key}:\n-> ')
                            os.system('cls')

            inventario[nombre.lower()][palabra] = data
            update_file('inventario.json', inventario)
            os.system('pause')
        else:
            print(f'No existe en {nombre.lower()}: {palabra}')

def delete_data_apz(nombre):
    os.system('clear')

    if nombre == 'ACTIVOS':
        msg = 'Ingrese el "Código campus" del activo que va a eliminar\n-> '
    elif nombre == 'PERSONAL':
        msg = 'Ingrese el "id" de la persona que va a eliminar\n-> '
    elif nombre == 'ZONAS':
        msg = 'Ingrese el "Número de zona" de la zona que va a eliminar\n-> '

    inventario = read_file('inventario.json')

    delete_value = input(msg)

    if delete_value not in inventario[nombre.lower()]:
        global count
        count += 1
        print(f'El dato que ingresó no esta registrado | Intento {count}/3')
        os.system('pause')
        if count > 2:
            count = 0
            return
        delete_data_apz(nombre)
    else:
        inventario[nombre.lower()].pop(delete_value)
        update_file('inventario.json', inventario)

def search_data_apz(nombre):

    if nombre == 'ACTIVOS':
        msg = 'Ingrese el "Código campus" del activo que va a buscar\n-> '
    elif nombre == 'PERSONAL':
        msg = 'Ingrese el "id" de la persona que va a buscar\n-> '
    elif nombre == 'ZONAS':
        msg = 'Ingrese el "Número de zona" de la zona que va a buscar\n-> '

    inventario = read_file('inventario.json')

    search_value = input(msg)

    if search_value not in inventario[nombre.lower()]:
        global count
        count += 1
        print(f'El dato que ingresó no esta registrado | Intento {count}/3')
        os.system('pause')
        if count > 2:
            count = 0
            return
        search_data_apz(nombre)
    else:
        print('VALORES\n')
        for item, value in (inventario[nombre.lower()][search_value]).items():
            if type(value) == dict:
                print(f'{item}:\n')
                for item2, value2 in value.items():
                    print(f'    {item2}: {value2}\n')
            else:
                print(f'{item}: {value}\n')
        print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n')
        os.system('pause')