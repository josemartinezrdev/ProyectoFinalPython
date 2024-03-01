from modules.menu import create_menu
import modules.core_files as cf
import modules.activos_module as acm


inventario = {
    'activos': {},
    'personal': {},
    'zonas': {},
    'asignaciones': {}
}

def main():
    acm.clear_screen()
    cf.check_file("inventario.json",inventario)
    create_menu(cf.read_file("inventario.json"))
    acm.clear_screen()
if __name__ == "__main__":
    main()
