import modules.core_files as cf
from modules.activos_module import clear_screen


def add_zonas():

    inventario = cf.read_file('inventario.json')
    try:
        nro_zona = input('Ingrese el número de la zona: ')
        if nro_zona in inventario['zonas']:
            print ('Zona ya registrada')
        clear_screen()
        if nro_zona <= 0:
            print('Dato inválido')
    except ValueError:
        print('Dato inválido')

    try:
        nombre_zona = input('Ingrese el nombre de la zona: ')
        if nombre_zona in inventario['zonas']:
            print ('Nombre de zona ya registrado')
        clear_screen()
        if nombre_zona <= 0:
            print('Dato inválido')
    except ValueError:
        print('Dato inválido')
        
        capacidad_zona = input('Ingrese la capacidad de la zona: ') #definir si debe tener un limite
        clear_screen()

    zona = {
        'Nro Zona': nro_zona,
        'Nombre Zona': nombre_zona,
        'Capacidad Zona': capacidad_zona
    }

    inventario.get('zonas').update({nro_zona:zona})
    cf.update_file('inventario.json', inventario)

    return