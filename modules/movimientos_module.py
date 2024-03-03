from core_files import read_file, clear_screen, pause_screen


def retorno_activo():
    inventario = read_file('inventario.json')

    act_return = input('Ingrese el "Código Campus" del activo que quiere retornar')
