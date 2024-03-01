from modules.core_files import read_file, update_file, clear_screen

def add_personas():

    inventario = read_file('inventario.json')


    id = input('Ingrese id/cc de la persona\n-> ') 
    clear_screen()
    opt = input('Elija si es persona natural: "1", o persona jurídica: "2"\n-> ')
    if opt == "1":
        tipo = 'Natural'
    elif opt == "2":
        tipo = "Juridica"
    clear_screen()
    name = input('Ingrese nombre de la persona\n-> ')
    clear_screen()
    email = input(f'Ingrese el email de {name}\n-> ')
    clear_screen()

    if input('Tiene teléfono móvil? Si(s) / No(Enter) \n-> ').lower() == 's':
        tel_movil = input(f'Ingrese teléfono móvil de {name}\n-> ')
        clear_screen()
    else: 
        tel_movil = 'No aplica'
    if input('Tiene teléfono en casa? Si(s) / No(Enter) \n-> ').lower() == 's':
        tel_casa = input(f'Ingrese número del teléfono de casa para {name}\n-> ')
        clear_screen()
    else: 
        tel_casa = 'No aplica'
    if input('Tiene teléfono personal? Si(s) / No(Enter) \n-> ').lower() == 's':
        tel_personal = input(f'Ingrese teléfono personal de {name}\n-> ')
        clear_screen()
    else: 
        tel_personal = 'No aplica'
    if input('Tiene teléfono de oficina? Si(s) / No(Enter) \n-> ').lower() == 's':
        tel_oficina = input(f'Ingrese teléfono de oficina de {name}\n-> ')
        clear_screen()
    else: 
        tel_oficina = 'No aplica'

    persona = {
        'id': id,
        'tipo': tipo,
        'name': name,
        'email': email,
        'telefonos': {
            'tel_movil': tel_movil,
            'tel_casa': tel_casa,
            'tel_personal': tel_personal,
            'tel_oficina': tel_oficina
            }
        }

    inventario.get('personal').update({id:persona})
    update_file('inventario.json', inventario)


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