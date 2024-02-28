import os, sys
import modules.core_files as cf

#AÑADIR HISTORIAL CUANDO ESTÉ ASIGNACIÓN

def clear_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")


def pause_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")


def add_activos():

    inventario = cf.read_file(cf.BASE+'inventario.json')

    cod_campus = input('Ingrese el código de campus\n-> ')
    clear_screen()
    cod_transaccion = input('Ingrese el código de transacción\n-> ')
    clear_screen()
    nro_formulario = input('Ingrese el número de formulario\n-> ')
    clear_screen()
    nro_serial = input('Ingrese el número serial\n-> ')
    clear_screen()
    name_activo = input('Ingrese el nombre del activo\n-> ')
    clear_screen()

    #! Validar zonas

    ubicacion_activo = input('Ingrese la ubicación del activo\n-> ')
    clear_screen()

    
    marca = input('Ingrese la marca\n-> ')
    clear_screen()
    categoria = input('Ingrese la categoría\n-> ')
    clear_screen()
    # , Estado

    proveedor = input('Ingrese el ID del proveedor del activo\n-> ')
    if proveedor not in inventario.get('personal'):
        print('El proveedor no se encuentra registrado.')
        pause_screen()
        return
    else:
        # proveedor = inventario.get('personal').get(proveedor)['name']
        clear_screen()
        try:
            valor = int(input('Ingrese el valor unitario\n-> '))
        except ValueError:
            print('Los valores deben ser de tipo entero')
            pause_screen()
            add_activos()
        else:
            clear_screen()
            empresa_resp = input('Ingrese la empresa responsable del activo\n-> ')
            clear_screen()
            tipo = input('Ingrese el tipo de activo\n-> ')

        activo = {
            'cod_campus': cod_campus,
            'cod_transaccion': cod_transaccion,
            'nro_formulario': nro_formulario,
            'nro_serial': nro_serial,
            'name_activo': name_activo,
            'ubicacion_activo': ubicacion_activo,
            'marca': marca,
            'categoria': categoria,
            'estado': 'no_asignado',
            'proveedor': proveedor,
            'valor': valor,
            'empresa_resp': empresa_resp,
            'tipo': tipo
        }

        inventario.get('activos').update({name_activo: activo}) 
        cf.update_file('inventario.json', inventario)

        return True


def edit_activos():
    pass


def delete_activos():
    pass


def search_activos():
    pass
