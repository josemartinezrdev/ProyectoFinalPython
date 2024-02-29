from tabulate import tabulate
import modules.activos_module as acm
import modules.personas_module as pem
import modules.zonas_module as zom
import modules.core_files as cf


def create_menu(inventario:dict):
    title = """
++++++++++++++++++++++++++++++++++++
+  SISTEMA DE G & C DE INVENTARIO  +
++++++++++++++++++++++++++++++++++++
"""

    # opts = """
    # 1. ACTIVOS #¿ Jose
    # 2. PERSONAL #¿ Jose
    # 3. ZONAS #¡ Danna
    # 4. ASIGNACIÓN DE ACTIVOS #- Eliza
    # 5. REPORTES #- Eliza
    # 6. MOVIMIENTOS DE ACTIVOS #¡ Danna
    # 7. SALIR #¿ Jose
    # """

    print(title)

    opts = (['1', 'ACTIVOS'], ['2', 'PERSONAL'], ['3', 'ZONAS'], ['4', 'ASIGNACIÓN DE ACTIVOS'], ['5', 'REPORTES'], ['6', 'MOVIMIENTO DE ACTIVOS'], ['7', 'SALIR'])
    print(tabulate(opts, tablefmt='grid'))

    options = ['1', '2', '3', '4', '5', '6', '7', ]


    opt = input('Ingrese la opción:\n-> ')
    if opt not in options:
        acm.clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        acm.pause_screen()
        acm.clear_screen()
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


def create_menu_apz(nombre:str, inventario:dict):
    acm.clear_screen()
    title = f"""
    ++++++++++++++++++++++++++++
    +       MENÚ {nombre}       +
    ++++++++++++++++++++++++++++
    """

    # opts = """
    # 1. AGREGAR
    # 2. EDITAR
    # 3. ELIMINAR
    # 4. BUSCAR
    # 5. REGRESAR
    # """
    options = ['1', '2', '3', '4', '5']
    
    print(title)

    opts = (['1', 'AGREGAR'], ['2', 'EDITAR'], ['3', 'ELIMINAR'], ['4', 'BUSCAR'], ['5', 'REGRESAR AL MENU PRINCIPAL'])
    print(tabulate(opts, tablefmt='grid'))


    opt = input('Ingrese la opción:\n-> ')

    
    if opt not in options:
        acm.clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        acm.pause_screen()
        acm.clear_screen()
        create_menu_apz(nombre, inventario)
    else:
        acm.clear_screen()
        if opt == '1':
            if nombre == 'ACTIVOS':
                acm.add_activos()
                return True
            elif nombre == 'PERSONAL':
                pem.add_personas()
                return True
            elif nombre == 'ZONAS':
                zom.add_zonas()

        elif opt == '2':
            if nombre == 'ACTIVOS':
                cf.edit_file_apz(nombre)
                return True
            elif nombre == 'PERSONAL':
                cf.edit_file_apz(nombre)
                return True
            elif nombre == 'ZONAS':
                cf.edit_file_apz(nombre)
        elif opt == '5':
            create_menu(inventario)
    return True


def create_menu_asignar(inventario:dict):
    acm.clear_screen()
    title = f"""
    ++++++++++++++++++++++++++++
    +       MENÚ ASIGNACIÓN    +
    ++++++++++++++++++++++++++++
    """
    options = ['1', '2', '3']
    
    print(title)

    opts = (['1', 'CREAR ASIGNACION'], ['2', 'BUSCAR'], ['3', 'REGRESAR AL MENU PRINCIPAL'])
    print(tabulate(opts, tablefmt='grid'))

    opt = input('Ingrese la opción:\n-> ')
    if opt not in options:
        acm.clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        acm.pause_screen()
        acm.clear_screen()
        create_menu_asignar(inventario)
    else:
        if opt=='1':
            pass
        elif opt=='2':
            pass
        elif opt=='3':
            create_menu(inventario)
        

    


def create_menu_reportes():
    pass


def create_menu_movimientos():
    pass
