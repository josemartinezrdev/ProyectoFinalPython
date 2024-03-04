from modules.core_files import read_file, pause_screen, update_file
from modules.asignacion_module import add_asignacion

def movimiento(action):

    if action == 'retorno':
        msg = 'Ingrese el "Código Campus" del activo que quiere retornar\n-> '
        state = '0'
    elif action == 'baja':
        msg = 'Ingrese el "Código Campus" del activo que quiere dar de baja\n-> '
        state = '2'
    elif action == 're':
        msg = 'Ingrese el "Código Campus" del activo que quiere reasignar\n-> '
        state = '1'
    elif action == 'gar':
        msg = 'Ingrese el "Código Campus" del activo que quiere enviar a garantía\n-> '
        state = '3'

    inventario = read_file('inventario.json')

    if action != 're':
        fecha_movimiento = input('Ingrese la fecha del movimiento')

    act_return = input(msg)
    estado = inventario.get('activos').get(act_return).get('estado')

    if estado != '0':

        inventario['activos'][act_return]['estado'] = state
        inventario['activos'][act_return]['ubicacion_activo'] = 'no_asignada'

        if estado == '1':
            ubicacion = input('Ingrese el "ID" / "Número Zona" de la persona / zona en la cual se encuentra asignado el activo\n-> ')

            if ubicacion not in inventario.get('asignaciones'):
                print('La ubicacion ingresada no existe')
                pause_screen()
                movimiento()
            else:
                inv = inventario['asignaciones'][ubicacion]['activos_asignados']

                for idx, item in enumerate(inv):
                    if item == act_return:
                        inventario['asignaciones'][ubicacion]['activos_asignados'].pop(idx)
                        if action == 're':
                            inventario['activos'][act_return]['estado'] = '0'
                            inventario['activos'][act_return]['ubicacion_activo'] = 'no_asignada'
                            update_file('inventario.json', inventario)
                            add_asignacion(act_return, True)
    update_file('inventario.json', inventario)
