import modules.core_files as cf

def add_personas():

    inventario = cf.read_file(cf.BASE+'inventario.json')

    id = input('Ingrese id/cc de la persona\n-> ')
    name = input('Ingrese nombre de la persona\n-> ')
    email = input(f'Ingrese el email de {name}\n-> ')
    tel_movil = input(f'Ingrese teléfono movil de {name}\n-> ')
    tel_casa = input(f'Ingrese teléfono fijo de {name}\n-> ')
    tel_personal = input(f'Ingrese teléfono personal de {name}\n-> ')
    tel_oficina = input(f'Ingrese teléfono oficina de {name}\n-> ')

    persona = {
        'id': id,
        'name': name,
        'email': email,
        'tel_movil': tel_movil,
        'tel_casa': tel_casa,
        'tel_personal': tel_personal,
        'tel_oficina': tel_oficina
    }

    inventario.get('personal').update({id:persona})
    cf.update_file('inventario.json', inventario)


def edit_personas():
    pass


def delete_personas():
    pass


def search_personas():
    pass


#' Usar este código cuando necesite añadir o editar el estado.

# print("""
#             0. No asignado
#             1. Asignado
#             2. Dado de baja / daño
#             3. En reparación / garantía
#         """)
#         opt = input('Ingrese el número del estado\n-> ')
#         if opt == '0':
#             estado = 'no_asignado'
#         elif opt == '1':
#             estado = 'asignado'
#         elif opt == '2':
#             estado = 'dañado'
#         elif opt == '3':
#             estado = 'reparacion'
#         else:
#             print(f'La opción {opt} no es valida')
#             return
#         clear_screen()