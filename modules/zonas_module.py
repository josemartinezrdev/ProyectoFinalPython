import modules.core_files as cf
from modules.activos_module import clear_screen


def add_zonas():

    inventario = cf.read_file('inventario.json')

    nro_zona = input('Ingrese el número de la zona: ')
    clear_screen()
    nombre_zona = input('Ingrese el nombre de la zona: ')
    clear_screen()
    capacidad_zona = input('Ingrese la capacidad de la zona: ')
    clear_screen()

    zona = {
        'Nro Zona': nro_zona,
        'Nombre Zona': nombre_zona,
        'Capacidad Zona': capacidad_zona
    }

    inventario.get('zonas').update({nro_zona:zona})
    cf.update_file('inventario.json', inventario)

    return