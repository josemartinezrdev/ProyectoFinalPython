import modules.core_files as cf
from modules.activos_module import clear_screen 
# valida el numero de asignacion
def validar_Nasignacion():
    inventario = cf.read_file('inventario.json')
    try:
        numero_asignacion = int(input('Ingrese el numero de la asignacion: '))
        if numero_asignacion in inventario['asignacion'] :
            print('El numero de asignacion ya se encuentra reguistrado')
            clear_screen()
            return crear_asignacion()
        if numero_asignacion < 0: 
            print('Numero de asignacion Invalido')
            clear_screen()
            return crear_asignacion()

    except ValueError:
        print('Numero invalido')
        clear_screen()
        return crear_asignacion()
    return numero_asignacion


def crear_asignacion():
    
    numero_asignacion=validar_Nasignacion()
    fecha_asignacion=str(input('Ingrese la Fecha de la asignacion'))
    asignacion={
        'nAsignacion':str(numero_asignacion).zfill(3),
        'FechaAsignación':fecha_asignacion,
        'TipoAsignacion ':'',
        'AsignadoA':'',
        'Activos':''
    }


    