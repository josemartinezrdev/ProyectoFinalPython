from modules.activos_module import clear_screen, pause_screen
from modules.core_files import read_file

def list_files_reports():
    inventario = read_file('inventario.json')

    for key, value in (inventario.get('activos')).items():
        print(key, value)
    pause_screen()