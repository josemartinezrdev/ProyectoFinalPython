from tabulate import tabulate
from modules.activos_module import add_activos
from modules.personas_module import add_personas
from modules.zonas_module import add_zonas
from modules.asignacion_module import add_asignacion
from modules.reports_module import report_all_actives, report_list_category
from modules.movimientos_module import retorno_activo
from modules.core_files import edit_file_apz, delete_data_apz, search_data_apza, pause_screen, clear_screen


def create_menu(inventario: dict):
    clear_screen()
    title = """
++++++++++++++++++++++++++++++++++++
+  SISTEMA DE G & C DE INVENTARIO  +
++++++++++++++++++++++++++++++++++++
"""

    # 1. ACTIVOS #¿ Jose
    # 2. PERSONAL #¿ Jose
    # 3. ZONAS #¡ Danna
    # 4. ASIGNACIÓN DE ACTIVOS #- Eliza
    # 5. REPORTES #- Eliza
    # 6. MOVIMIENTOS DE ACTIVOS #¡ Danna
    # 7. SALIR #¿ Jose

    clear_screen()
    print(title)

    opts = (['1', 'ACTIVOS'], ['2', 'PERSONAL'], ['3', 'ZONAS'], ['4', 'ASIGNACIÓN DE ACTIVOS'], [
            '5', 'REPORTES'], ['6', 'MOVIMIENTO DE ACTIVOS'], ['7', 'SALIR'])
    print(tabulate(opts, tablefmt='grid'))

    options = ['1', '2', '3', '4', '5', '6', '7']

    opt = input('Ingrese la opción:\n-> ')
    if opt not in options:
        clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        pause_screen()
        clear_screen()
        create_menu(inventario)
    else:
        if opt == '1':
            nombre = 'ACTIVOS'
            create_menu_apz(nombre, inventario)
            create_menu(inventario)
        elif opt == '2':
            nombre = 'PERSONAL'
            create_menu_apz(nombre, inventario)
            create_menu(inventario)
        elif opt == '3':
            nombre = 'ZONAS'
            create_menu_apz(nombre, inventario)
            create_menu(inventario)
        elif opt == '4':
            create_menu_asignar(inventario)
            create_menu(inventario)
        elif opt == '5':
            create_menu_reportes()
            create_menu(inventario)
        elif opt == '6':
            create_menu_movimientos()
            create_menu(inventario)
        elif opt == '7':
            return


def create_menu_apz(nombre: str, inventario: dict):
    clear_screen()
    title = f"""
    ++++++++++++++++++++++++++++
    +       MENÚ {nombre}       +
    ++++++++++++++++++++++++++++
    """
    options = ['1', '2', '3', '4', '5']

    print(title)

    opts = (['1', 'AGREGAR'], ['2', 'EDITAR'], ['3', 'ELIMINAR'],
            ['4', 'BUSCAR'], ['5', 'REGRESAR AL MENÚ PRINCIPAL'])
    print(tabulate(opts, tablefmt='grid'))

    opt = input('Ingrese la opción:\n-> ')

    if opt not in options:
        clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        pause_screen()
        clear_screen()
        create_menu_apz(nombre, inventario)
    else:
        clear_screen()
        if opt == '1':
            if nombre == 'ACTIVOS':
                add_activos()
                create_menu_apz(nombre, inventario)
            elif nombre == 'PERSONAL':
                add_personas()
                create_menu_apz(nombre, inventario)
            elif nombre == 'ZONAS':
                add_zonas()
                create_menu_apz(nombre, inventario)

        elif opt == '2':
            if nombre == 'ACTIVOS':
                edit_file_apz(nombre)
                create_menu_apz(nombre, inventario)
            elif nombre == 'PERSONAL':
                edit_file_apz(nombre)
                create_menu_apz(nombre, inventario)
            elif nombre == 'ZONAS':
                edit_file_apz(nombre)
                create_menu_apz(nombre, inventario)

        elif opt == '3':
            if nombre == 'ACTIVOS':
                delete_data_apz(nombre)
                create_menu_apz(nombre, inventario)
            elif nombre == 'PERSONAL':
                delete_data_apz(nombre)
                create_menu_apz(nombre, inventario)
            elif nombre == 'ZONAS':
                delete_data_apz(nombre)
                create_menu_apz(nombre, inventario)

        elif opt == '4':
            if nombre == 'ACTIVOS':
                search_data_apza(nombre)
                create_menu_apz(nombre, inventario)
            elif nombre == 'PERSONAL':
                search_data_apza(nombre)
                create_menu_apz(nombre, inventario)
            elif nombre == 'ZONAS':
                search_data_apza(nombre)
                create_menu_apz(nombre, inventario)

        elif opt == '5':
            pass
    return True


def create_menu_asignar(inventario: dict):
    clear_screen()
    title = f"""
    ++++++++++++++++++++++++++++
    +       MENÚ ASIGNACIÓN    +
    ++++++++++++++++++++++++++++
    """
    options = ['1', '2', '3']

    print(title)

    opts = (['1', 'CREAR ASIGNACION'], ['2', 'BUSCAR'],
            ['3', 'REGRESAR AL MENÚ PRINCIPAL'])
    print(tabulate(opts, tablefmt='grid'))

    opt = input('Ingrese la opción:\n-> ')
    if opt not in options:
        clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        pause_screen()
        clear_screen()
        create_menu_asignar(inventario)
    else:

        if opt == '1':
            add_asignacion()
        elif opt == '2':
            nombre = 'ASIGNACIONES'
            search_data_apza(nombre)
        elif opt == '3':
            create_menu(inventario)


def create_menu_reportes():
    clear_screen()
    title = f"""
    ++++++++++++++++++++++++++
    +       MENÚ REPORTES    +
    ++++++++++++++++++++++++++
    """
    options = ['1', '2', '3', '4', '5']

    print(title)

    opts = (['1', 'LISTAR TODOS LOS ACTIVOS'], ['2', 'LISTAR ACTIVOS POR CATEGORIA'],
            ['3', 'LISTAR ACTIVOS DADOS DE BAJA POR DAÑO'], [
                '4', 'LISTAR ACTIVOS Y ASIGNACION'],
            ['5', 'REGRESAR AL MENU PRINCIPAL'])
    print(tabulate(opts, tablefmt='grid'))

    opt = input('Ingrese la opción:\n-> ')

    if opt not in options:
        clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        pause_screen()
        clear_screen()
        create_menu_reportes()
    else:

        if opt == '1':
            report_all_actives()
            create_menu_reportes()
        if opt == '2':
            report_list_category()
            create_menu_reportes()
        if opt == '3':
            pass

        if opt == '4':
            pass

        if opt == '5':
            pass


def create_menu_movimientos():
    clear_screen()
    title = f"""
    +++++++++++++++++++++++++++++++
    +       MENÚ MOVIMIENTOS      +
    +++++++++++++++++++++++++++++++
    """
    options = ['1', '2', '3', '4', '5']

    print(title)

    opts = (['1', 'CREAR ASIGNACION'], ['2', 'BUSCAR'],
            ['3', 'REGRESAR AL MENÚ PRINCIPAL'])
    print(tabulate(opts, tablefmt='grid'))

    opt = input('Ingrese la opción:\n-> ')
    if opt not in options:
        clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        pause_screen()
        clear_screen()
    else:
        if opt == '1':
            retorno_activo()
            create_menu_movimientos()
        elif opt == '2':
            pass
        elif opt == '3':
            pass
        elif opt == '4':
            pass
        elif opt == '5':
            return
