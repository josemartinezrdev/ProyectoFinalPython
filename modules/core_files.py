import json
import os

BASE = 'data/'

data = {}
srcData = {}

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
        msg = 'Ingrese el "Código campus" del activo que va a editar\n-> '
    elif nombre == 'PERSONAL':
        msg = 'Ingrese el "id" de la persona / proveedor que va a editar\n-> '
    elif nombre == 'ZONAS':
        msg = 'Ingrese el "Número de zona" de la zona que va a editar\n-> '

    inventario = read_file('inventario.json')

    palabra = input(msg)
    
    if nombre.lower() in inventario:
        if palabra in inventario[nombre.lower()]:
            data = inventario[nombre.lower()][palabra]

            for key, value in data.items():
                if key not in ['cod_campus', 'nro_formulario', 'estado', 'id', 'Nro Zona']:
                    if input(f'Desea modificar {key}? s(si) / Enter(no)\n-> ').lower() == 's':
                        os.system('cls')
                        nuevo_valor = input(f'Ingrese el nuevo valor para {key}:\n-> ')
                        os.system('cls')
                        data[key] = nuevo_valor

            inventario[nombre.lower()][palabra] = data
            update_file('inventario.json', inventario)
        else:
            print(f'No existe en {nombre.lower()}: {palabra}')
def update_data(archivo: str, data):
    pass

def edit_zonas():  #-> memorize this
    if (len(data) <=0):
        print('No se encontro información')
        os.system('pause')
    else:
        for key in data.keys():
            if(key != 'Nro Zona') :
                if(type(data[key]) == dict):
                    for key2 in data[key].keys():
                        if(bool(input(f'Desea modificar el {key2} s(si) o Enter No'))):
                            os.system('cls')
                            data[key][key2] = input(f'Ingrese el nuevo valor para {key2} :')
                
        srcData['zonas'].update({data['Nro Zona']:data})
        update_file('inventario.json',srcData)
    os.system('pause')