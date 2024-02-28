from tabulate import tabulate
import os

def main_menu():

    titulo = """
+++++++++++++++++++++++++++++++++++++++++
+ SISTEMA G&C DE INVENTARIO CAMPUSLANDS +
+++++++++++++++++++++++++++++++++++++++++
”"""
    print(titulo)

    menu = (['1', 'ACTIVOS'], ['2', 'PERSONAL'], ['3', 'ZONAS'], ['4', 'ASIGNACIÓN DE ACTIVOS'], ['5', 'REPORTES'], ['6', 'MOVIMIENTO DE ACTIVOS'], ['7', 'SALIR'])
    print(tabulate(menu, tablefmt='grid'))
    op = input('\n>>')

    if op == "1":
       menu_activos()
    elif op == "2":
        menu_personal()
    elif op == "3":
        menu_zonas()
    elif op == "4":
        menu_asignacion_activos()
    elif op == "5":
        menu_reportes
    elif op == '6':
        menu_movimiento_activos()
    elif op == '7':
        pass
    else:
        main_menu()

def menu_activos():

    titulo = """
+++++++++++++++++++++
+    MENU ACTIVOS   +
+++++++++++++++++++++
”"""
    print(titulo)

    menu = (['1', 'AGREGAR'], ['2', 'EDITAR'], ['3', 'ELIMINAR'], ['4', 'BUSCAR'], ['5', 'REGRESAR AL MENU PRINCIPAL'])
    print(tabulate(menu, tablefmt='grid'))
    op = input('\n>>')

    if op == "1":
       pass
    elif op == "2":
        pass
    elif op == "3":
        pass
    elif op == "4":
        pass
    elif op == "5":
        pass
    else:
        menu_activos()

def menu_personal():

    titulo = """
++++++++++++++++++++++
+    MENU PERSONAL   +
++++++++++++++++++++++
”"""
    print(titulo)

    menu = (['1', 'AGREGAR'], ['2', 'EDITAR'], ['3', 'ELIMINAR'], ['4', 'BUSCAR'], ['5', 'REGRESAR AL MENU PRINCIPAL'])
    print(tabulate(menu, tablefmt='grid'))
    op = input('\n>>')

    if op == "1":
       pass
    elif op == "2":
        pass
    elif op == "3":
        pass
    elif op == "4":
        pass
    elif op == "5":
        pass
    else:
        menu_personal()

def menu_zonas():

    titulo = """
+++++++++++++++++++
+    MENU ZONAS   +
+++++++++++++++++++
”"""
    print(titulo)

    menu = (['1', 'AGREGAR'], ['2', 'EDITAR'], ['3', 'ELIMINAR'], ['4', 'BUSCAR'], ['5', 'REGRESAR AL MENU PRINCIPAL'])
    print(tabulate(menu, tablefmt='grid'))
    op = input('\n>>')

    if op == "1":
       pass
    elif op == "2":
        pass
    elif op == "3":
        pass
    elif op == "4":
        pass
    elif op == "5":
        pass
    else:
        menu_zonas()

def menu_asignacion_activos():

    titulo = """
++++++++++++++++++++++++++++++++
+    MENU ASIGNACION ACTIVOS   +
++++++++++++++++++++++++++++++++
”"""
    print(titulo)

    menu = (['1', 'CREAR ASIGNACION'], ['2', 'BUSCAR ASIGNACION'], ['3', 'REGRESAR AL MENU PRINCIPAL'])
    print(tabulate(menu, tablefmt='grid'))
    op = input('\n>>')

    if op == "1":
       pass
    elif op == "2":
        pass
    elif op == "3":
        pass
    else:
        menu_asignacion_activos()

def menu_reportes():

    titulo = """
+++++++++++++++++++++
+    MENU REPORTES  +
+++++++++++++++++++++
”"""
    print(titulo)

    menu = (['1', 'LISTAR TODOS LOS ACTIVOS'], ['2', 'LISTAR ACTIVOS POR CATEGORIA'], ['3', 'LISTAR ACTIVOS DADOS DE BAJA POR DAÑO'], ['4', 'LISTAR ACTIVOS Y ASIGNACION'], ['5', 'LISTAR HISTORIAL DE MOV. DE ACTIVO'], ['6', 'REGRESAR AL MENU PRINCIPAL'])
    print(tabulate(menu, tablefmt='grid'))
    op = input('\n>>')

    if op == "1":
       pass
    elif op == "2":
        pass
    elif op == "3":
        pass
    elif op == "4":
        pass
    elif op == "5":
        pass
    elif op == '6':
        pass
    else:
        menu_reportes()

def menu_movimiento_activos():

    titulo = """
+++++++++++++++++++++++++++++++++++
+    MENU MOVIMIENTO DE ACTIVOS   +
+++++++++++++++++++++++++++++++++++
”"""
    print(titulo)

    menu = (['1', 'RETORNO DE ACTIVO'], ['2', 'DAR DE BAJA ACTIVO'], ['3', 'CAMBIAR ASIGNACION DE ACTIVO'], ['4', 'ENVIAR A GARANTIA ACTIVO'], ['5', 'REGRESAR AL MENU PRINCIPAL'])
    print(tabulate(menu, tablefmt='grid'))
    op = input('\n>>')

    if op == "1":
       pass
    elif op == "2":
        pass
    elif op == "3":
        pass
    elif op == "4":
        pass
    elif op == "5":
        pass
    else:
        menu_movimiento_activos()