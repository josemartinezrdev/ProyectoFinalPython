import modules.core_files as cf
from modules.activos_module import clear_screen


def add_zonas():

    inventario = cf.read_file('inventario.json')
    try:
        nro_zona = input('Ingrese el número de la zona: ')
        clear_screen()
        if nro_zona in inventario['zonas']:
            print ('Zona ya registrada')
            add_zonas()
        if (nro_zona.find('-') != -1):
            print('Dato inválido')
            add_zonas()
        # if (nro_zona.isalpha):
        #     print('Dato invalido')
        #     add_zonas()
    except ValueError:
        print('Dato inválido')
        add_zonas()
    try:
        nombre_zona = input('Ingrese el nombre de la zona: ')
        if nombre_zona in inventario['zonas']:
            print ('Nombre de zona ya registrado')
            add_zonas()
    except ValueError:
        print('Dato inválido')
    else:
        capacidad_zona = int(input('Ingrese la capacidad de la zona: ')) #definir si debe tener un limite
        clear_screen()


        zona = {
            'Nro Zona': nro_zona,
            'Nombre Zona': nombre_zona,
            'Capacidad Zona': capacidad_zona,
            'Ex CPU': 0,
            'Ex MON': 0,
            'Ex MOU': 0,
            'Ex TEC': 0
        }

        inventario.get('zonas').update({nro_zona:zona})
        cf.update_file('inventario.json', inventario)

        return