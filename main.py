import modules.menu as mn
import modules.core_files as cf
import modules.activos_module as acm


if __name__ == "__main__":

    inventario = {
        'activos': {},
        'personal': {},
        'zonas': {},
        'asignacion': {}
    }

    cf.check_file("inventario.json",inventario)

    acm.clear_screen()
    mn.create_menu(inventario)
