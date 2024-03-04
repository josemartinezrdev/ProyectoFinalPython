from modules.menu import create_menu
from modules.core_files import check_file, clear_screen

inventario = {
    'activos': {},
    'personal': {},
    'zonas': {},
    'asignaciones': {}
}

def main():
    clear_screen()
    check_file("inventario.json", inventario)
    create_menu()
    clear_screen()
if __name__ == "__main__":


    main()