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
    with open(archivo, 'r') as rf:
        inventario = json.load(rf)
    return inventario

def update_file(archivo, data):
    with open(BASE + archivo, 'w') as fw:
        json.dump(data, fw, indent=4)


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
                #     for key2 in data[key].keys():
                #         if(bool(input(f'Desea modificar el {key2} s(si) o Enter No'))):
                #             os.system('cls')
                #             data[key][key2] = input(f'Ingrese el nuevo valor para {key2} :')
                 if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                        os.system('cls')
                        data[key] = input(f'Ingrese el nuevo valor para {key} :')
                
        srcData['zonas'].update({data['Nro Zona']:data})
        update_file('inventario.json',srcData)
    os.system('pause')

def eliminar_zona(data):
    elim_dato = input("Ingrese la zona que desea borrar -> ")
    data['zonas'].pop(elim_dato)
    elim_dato('inventario.json',data)

def buscar_zona(data):
    valor = input("Ingrese la zona a buscar -> ")
    result= data['zonas'].get(valor)
    nro_zona,nombre_zona,capacidad_zona,  = result.values()
    print(f'{result}')
    os.system('pause')