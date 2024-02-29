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
    cf.check_file("inventario.json",inventario)
    create_menu(cf.read_file("inventario.json"))

    isRunning = True
    while isRunning:
        
        acm.clear_screen()
        o = create_menu(inventario)
        isRunning = o

if __name__ == "__main__":
    main()
