import modules.core_files as cf
from modules.activos_module import clear_screen, pause_screen

def validar_num_zona():
    inventario = cf.read_file('inventario.json')
    nro_zona = int(input('Ingrese el número de la zona:\n-> '))
    nombre_zona = ''
    
    try:
        if nro_zona <= 0:
            print('Dato inválido')
            pause_screen()
            clear_screen()
            validar_num_zona()
        else: 
            nro_zona = str(nro_zona)
            if nro_zona in inventario['zonas']:
                print('Zona ya registrada')
                pause_screen()
                clear_screen()
                validar_num_zona()
            else: 
                nombre_zona = input('Ingrese el nombre de la zona:\n-> ').capitalize()
                # if nombre_zona in inventario['zonas'][nro_zona]['']:
                #     print ('Nombre de zona ya registrado')
                #     pause_screen()
                #     clear_screen()
                #     validar_nZona()    
    except ValueError:
        print('Dato inválido')
        pause_screen()
        clear_screen()
        validar_num_zona()
    return nro_zona, nombre_zona

def validar_capacidad():
    capacidad_zona = int(input('Ingrese la capacidad de la zona:\n-> '))
    try:
        if capacidad_zona <= 0:
            print('Numero Errado')
            pause_screen()
            clear_screen()
            validar_capacidad()
    except ValueError:
        print('Numero Errado')
        pause_screen()
        clear_screen()
        validar_capacidad()
    return capacidad_zona

def add_zonas():
    inventario = cf.read_file('inventario.json')
    nro_zona, nombre_zona = validar_num_zona()
    capacidad_zona = validar_capacidad()
    
    zona = {
        'nro_zona': nro_zona,
        'nombre_zona': nombre_zona.capitalize(),
        'capacidad_zona': capacidad_zona,
        'ex_cpu': 0,
        'ex_mon': 0,
        'ex_mou': 0,
        'ex_tec': 0
    }

    inventario.get('zonas').update({nro_zona:zona})
    cf.update_file('inventario.json', inventario)
    return
