import modules.menu as mn
import modules.core_files as cf
import modules.activos_module as acm


if __name__ == "__main__":

    inventario = {
        'activos': {},
        'personal': {},
        'zonas': {}
    }

    cf.check_file("inventario.json",inventario)

    isRunning = True
    while isRunning:
        
        acm.clear_screen()
        o = mn.create_menu(inventario)
        isRunning = o