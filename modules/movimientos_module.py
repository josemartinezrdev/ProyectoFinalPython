from modules.core_files import read_file, clear_screen, pause_screen


def retorno_activo():
    inventario = read_file('inventario.json')

    act_return = input('Ingrese el "Código Campus" del activo que quiere retornar')
    
    estado = inventario('activos').get(act_return).get('estado')

    if (estado == '2'):
        print('El dispositivo se encuentra dado de Baja')
    elif (estado == '3'):
        print('El dispositivo se encuentra en reparación')
    else:
        opt = input('ingrese el "id" / "número de zona" de la persona / zona donde se encuentra asignado el activo')

