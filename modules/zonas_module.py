import os, sys
import modules.core_files as cf
from modules.activos_module import clear_screen, pause_screen


def add_zonas():

    inventario = cf.read_file(cf.BASE+'inventario.json')

    nro_zona = input('Ingrese el número de la zona: ')
    clear_screen()
    nombre_zona = input('Ingrese el nombre de la zona: ')
    clear_screen()
    capacidad_zona = input('Ingrese la capacidad de la zona')
    clear_screen()

    zona = {
        'nro_zona': nro_zona,
        'nombre_zona': nombre_zona,
        'capacidad_zona': capacidad_zona
    }
    
    inventario.get('zonas').update({nro_zona:zona})
    cf.update_file('inventario.json', inventario)

    return True