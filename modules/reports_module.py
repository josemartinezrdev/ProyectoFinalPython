from modules.core_files import read_file, clear_screen, pause_screen

def list_activos():
    inventario = read_file('inventario.json')

    for key, value in (inventario.get('activos')).items():
        print(key, value)
    pause_screen()