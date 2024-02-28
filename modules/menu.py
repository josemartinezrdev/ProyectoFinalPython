from tabulate import tabulate
import modules.activos_module as acm
import modules.personas_module as pem


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
            o = create_menu_apz(nombre, inventario)
            return o
        elif opt == '2':
            nombre = 'PERSONAL'
            o = create_menu_apz(nombre, inventario)
            return o
        elif opt == '3':
            nombre = 'ZONAS'
            o = create_menu_apz(nombre, inventario)
            return o
        elif opt == '4':
            create_menu_asignar()
        elif opt == '5':
            create_menu_reportes()
        elif opt == '6':
            create_menu_movimientos()
        elif opt == '7':
            return False


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
                # zom.add_zonas()
                pass
        
        elif opt == '5':
            return True
    return True

def create_menu_zonas():
    pass


def create_menu_asignar():
    pass


def create_menu_reportes():
    pass


def create_menu_movimientos():
    pass
