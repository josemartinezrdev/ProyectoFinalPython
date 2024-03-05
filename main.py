from modules.menu import create_menu
from modules.core_files import check_file, clear_screen
from modules.add_activos import agregar_activos

inventario = {
    'activos': {},
    'personal': {},
    'zonas': {},
    'asignaciones': {}
}

def main():
    clear_screen()
    check_file("inventario.json", inventario)
    agregar_activos()
    create_menu()
    clear_screen()
if __name__ == "__main__":
    

    main()