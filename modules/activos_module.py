from modules.core_files import read_file, update_file, clear_screen, pause_screen
import re

#AÑADIR HISTORIAL CUANDO ESTÉ ASIGNACIÓN

def add_activos():
    inventario = read_file('inventario.json')
    
    cod_campus = input('Ingrese el "Código de Campus del activo"\n-> ')
    
    #     print('Dato inválido\nDebes ingresar para :\n\tCPU -> CPU\n\tMonitor -> MON\n\tMouse -> MOU\n\tTeclado -> TEC\n¡Cualquiera acompañado de 1 a 3 números!')
    clear_screen()

    if cod_campus in inventario.get('activos'):
        print('El código que tratas de ingresar ya existe')
        pause_screen()
    else:
        cod_transaccion = input('Ingrese el "Código de Transacción"\n-> ')
        clear_screen()

        nro_formulario = input('Ingrese el "Número de Formulario"\n-> ')
        clear_screen()

        if nro_formulario in inventario.get('activos'):
            print('El número de formulario que tratas de ingresar ya existe')
            pause_screen()

        else:

            nro_serial = input('Ingrese el "Número Serial"\n-> ')
            clear_screen()
            name_activo = input('Ingrese el "Nombre" del activo\n-> ')
            clear_screen()

            clear_screen()

            marca = input('Ingrese la "Marca"\n-> ')
            clear_screen()
            categoria = input('Ingrese la "Categoría"\n(Equipo de computo, Electrodomestico, Juego)\n-> ')
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
                    tipo = input('Ingrese el "Tipo" de activo\n(Monitor, CPU, Teclado, Mouse,Aire Acondicionado,Portatil,Impresora)\n-> ')

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