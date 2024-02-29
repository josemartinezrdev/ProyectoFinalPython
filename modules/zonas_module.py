import modules.core_files as cf
from modules.activos_module import clear_screen, pause_screen

def validar_nZona():
    inventario = cf.read_file('inventario.json')
    nro_zona = int(input('Ingrese el número de la zona: '))
    nombre_zona=''
    try:
        
        if nro_zona <= 0:
            print('Dato inválido')
            pause_screen()
            clear_screen()
            validar_nZona()
        else: 
            nro_zona=str(nro_zona)
            if nro_zona in inventario['zonas']:
                print ('Zona ya registrada')
                pause_screen()
                clear_screen()
                validar_nZona()
            else: 
                nombre_zona = input('Ingrese el nombre de la zona: ')
                # if nombre_zona in inventario['zonas'][nro_zona]['']:
                #     print ('Nombre de zona ya registrado')
                #     pause_screen()
                #     clear_screen()
                #     validar_nZona()    
    except ValueError:
        print('Dato inválido')
        pause_screen()
        clear_screen()
        validar_nZona()
    return nro_zona,nombre_zona

def validar_capacidad():
    capacidad_zona=int(input('Ingrese la capacidad de la zona'))
    try:
        
        if capacidad_zona <= 0:
            print('Numero Errado:')
            pause_screen()
            clear_screen()
            validar_capacidad()
    except ValueError:
        print('Numero Errado:')
        pause_screen()
        clear_screen()
        validar_capacidad()
    return capacidad_zona
def add_zonas():
    inventario = cf.read_file('inventario.json')
    nro_zona,nombre_zona=validar_nZona()
    print(nro_zona,nombre_zona)
    pause_screen()
    capacidad_zona=validar_capacidad()
    
    zona = {
        'NroZona': nro_zona,
        'NombreZona': nombre_zona,
        'CapacidadZona': capacidad_zona,
        'ExCPU': 0,
        'ExMON': 0,
        'ExMOU': 0,
        'ExTEC': 0
    }

    inventario.get('zonas').update({nro_zona:zona})
    cf.update_file('inventario.json', inventario)

    return
