import json
import os

BASE = 'data/'


def check_file(archivo: str, data):
    if (not (os.path.isfile(BASE + archivo))):
        with open(BASE + archivo, "w") as bw:
            json.dump(data, bw, indent=4)

def read_file(archivo: str):
    with open(archivo, 'r') as rf:
        inventario = json.load(rf)
    return inventario

def update_file(archivo, data):
    with open(BASE + archivo, 'w') as fw:
        json.dump(data, fw, indent=4)

def updateData(data,srcData):
    if (len(data) <=0):
        print('😎 No se encontró información 😎')
        os.system('pause')
    else:
        for key in data.keys():
            if(key != 'nit'):
                if(type(data[key]) == dict):
                    for key2 in data[key].keys():
                        if(bool(input(f'Desea modificar el {key2} s(si) o Enter No'))):
                            os.system('cls')
                            data[key][key2] = input(f'Ingrese el nuevo valor para {key2} :')
                else:
                    if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                        os.system('cls')
                        data[key] = input(f'Ingrese el nuevo valor para {key} :')
        srcData['proveedores'].update({data['nit']:data})
        ('inventario.json',srcData)
    os.system('pause')



