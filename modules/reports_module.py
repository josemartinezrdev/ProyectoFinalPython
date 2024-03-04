from modules.core_files import read_file, clear_screen, pause_screen
import os

def report_all_actives():
    inventario = read_file('inventario.json')

    for key, value in (inventario.get('activos')).items():
        print(f'{key}:')
        for key2, value2 in value.items():
            if type(value2) == dict:
                print(f'    {key2}:')
                for key3, value3 in value2.items():
                    print(f'        {key3}: {value3}') 
            else:
                print(f'    {key2}: {value2}')
    pause_screen()

def report_list_category():
    clear_screen()
    inventario = read_file ('inventario.json')

    category = input('Ingrese el nombre de la categoría que desea ver: ').lower()

    for key, value in (inventario.get('activos')).items():
        for key2, value2 in value.items():
            if key2 == 'cod_campus':
                cod = value2
            if key2 == 'name_activo':
                name = value2
            if key2 == 'categoria':
                if value2 == category:
                    print(f'{cod} | {name}')
    pause_screen()
    clear_screen()

def report_baja_daños():
    clear_screen()
    inventario = read_file('inventario.json')

    activos_dados_de_baja = False

    for key, value in inventario.get('activos').items():
        for key2, value2 in value.items():
            if key2 == 'estado' and value2 == '2':
                print('ACTIVOS DADOS DE BAJA')
                print(f'\n{key}:\n') 
                for key3, value3 in value.items():
                    if key3 == 'cod_campus':
                        print(f'Código Campus: {value3}')
                    if key3 == 'name_activo':
                        print(f'Nombre Activo: {value3}')
                activos_dados_de_baja = True

    if not activos_dados_de_baja:
        print('No hay activos dados de baja')
                        
    pause_screen()
    clear_screen()



def report_list_activ_asig():
    clear_screen()
    inventario = read_file('inventario.json')

    for key, value in (inventario.get('asignaciones')).items():
        print(f'{key}:')
        for key2, value2 in value.items():
            if type(value2) == dict:
                print(f'    {key2}:')
                for key3, value3 in value2.items():
                    print(f'        {key3}: {value3}') 
            else:
                print(f'    {key2}: {value2}')
    pause_screen()
    clear_screen()
