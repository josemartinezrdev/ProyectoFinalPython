import json
import os

BASE = 'data/'


def check_file(archivo: str, data):
    if (not (os.path.isfile(BASE + archivo))):
        with open(BASE + archivo, "w") as bw:
            json.dump(data, bw, indent=4)

# def createData(archivo,data):
#     with open(BASE+archivo,"w+") as rwf:
#         json.dump(data,rwf,indent=4)


def read_file(archivo: str):
    with open(archivo, 'r') as rf:
        inventario = json.load(rf)
    return inventario


def update_file(archivo, data):
    with open(BASE + archivo, 'w') as fw:
        json.dump(data, fw, indent=4)


def update_data(archivo: str, data):
    pass
