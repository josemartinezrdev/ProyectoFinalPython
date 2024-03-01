from modules.core_files import read_file, update_file, clear_screen, pause_screen

#AÑADIR HISTORIAL CUANDO ESTÉ ASIGNACIÓN

def add_activos():

    inventario = read_file('inventario.json')

    cod_campus = input('Ingrese el "Código de Campus"\n-> ')
    clear_screen()
    cod_transaccion = input('Ingrese el "Código de Transacción"\n-> ')
    clear_screen()
    nro_formulario = input('Ingrese el "Número de Formulario"\n-> ')
    clear_screen()
    nro_serial = input('Ingrese el "Número Serial"\n-> ')
    clear_screen()
    name_activo = input('Ingrese el "Nombre" del activo\n-> ')
    clear_screen()

    clear_screen()

    marca = input('Ingrese la "Marca"\n-> ')
    clear_screen()
    categoria = input('Ingrese la "Categoría#\n-> ')
    clear_screen()
    # , Estado

    proveedor = input('Ingrese el "Nombre del Proveedor" del activo\n-> ')
    if proveedor.isalpha() == False:
        print('El "Proveedor" debe ser de tipo texto.')
        pause_screen()
        add_activos()
    else:
        clear_screen()
        try:
            valor = int(input('Ingrese el "Valor Unitario"\n-> '))
        except ValueError:
            print('El "Valor Unitario" debe ser de tipo entero')
            pause_screen()
            add_activos()
        else:
            clear_screen()
            empresa_resp = input('Ingrese la "Empresa Responsable" del activo\n-> ')
            clear_screen()
            tipo = input('Ingrese el "Tipo" de activo\n-> ')

        activo = {
            'cod_campus': cod_campus,
            'cod_transaccion': cod_transaccion,
            'nro_formulario': nro_formulario,
            'nro_serial': nro_serial,
            'name_activo': name_activo,
            'ubicacion_activo': 'no_asignada',
            'marca': marca,
            'categoria': categoria,
            'estado': '0',
            'proveedor': proveedor,
            'valor': valor,
            'empresa_resp': empresa_resp,
            'tipo': tipo,
            'historial': {}
        }

        inventario.get('activos').update({cod_campus: activo}) 
        update_file('inventario.json', inventario)

        return True