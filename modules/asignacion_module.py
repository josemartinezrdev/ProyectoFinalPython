from modules.core_files import read_file, update_file, clear_screen, pause_screen

# valida el numero de asignación

def validar_num_asignacion():

    inventario = read_file('inventario.json')
    try:
        num_asignacion = int(input('Ingrese el número de la asignación: '))
        if num_asignacion in inventario['asignaciones']:
            print('El número de asignación ya se encuentra registrado')
            pause_screen()
            clear_screen()
            return validar_num_asignacion()
        if num_asignacion < 0:
            print('Número de asignación inválido')
            pause_screen()
            clear_screen()
            return validar_num_asignacion()

    except ValueError:
        print('Numero inválido')
        pause_screen()
        clear_screen()
        return validar_num_asignacion()
    return num_asignacion


# valida el tipo de asignaciones
def val_tipo_asignacion():

    try:
        print('Ingrese el tipo de asignación que desea registrar: ')
        print('1. Personal \n 2. Zona')
        opt = input('-')
        if opt == '1':
            tipo_asignacion = 'Personal'
            return tipo_asignacion
        elif opt == '2':
            tipo_asignacion = 'zona'
            return tipo_asignacion
        else:
            print('Opción Incorrecta')
            pause_screen()
            clear_screen()
            val_tipo_asignacion()
    except ValueError:
        print('Opción Incorrecta')
        pause_screen()
        clear_screen()
        val_tipo_asignacion()
# valida el id de la persona que adquiere el activo (Falso positivo)

def validar_id():
    inventario = read_file('inventario.json')
    id_persona = input('Ingrese el Id de la persona')
    if id_persona in inventario['personal']:
        nombre = inventario.get('personal').get(id_persona).get('name')
        print(nombre)
        return id_persona
    else:
        print('El Id no se encuentra registrado')
        pause_screen()
        clear_screen()
        validar_id()

def validar_zona_asignada():
    inventario = read_file('inventario.json')
    opcion_zona = input('Ingrese el número de la zona: ')
    if opcion_zona in inventario['zonas']:
        return opcion_zona
    else:
        print('Opción Incorrecta, Rectifique el número de zona')
        pause_screen()
        clear_screen()
        validar_zona_asignada()


def validar_activo():
    inventario = read_file('inventario.json')
    asignados = {}
    assign = True
    while assign:
        CodCampus = input('Ingrese el "Código Campus" del activo')
        if CodCampus not in inventario['activos']:
            print('El código ingresado no corresponde a ningún activo')
            pause_screen()
            clear_screen()
            validar_activo()
        else:
            estado = inventario['activos'][CodCampus]['estado']
            nombre = inventario['activos'][CodCampus]['name_activo']
            if estado == '0':

                inventario['activos'][CodCampus]['estado'] = '1'
                asignados.update({CodCampus: nombre})
                assign = bool(input('Desea agregar otro activo? s(si) enter(no)'))
            else:
                if estado == '1':
                    print('El activo ya se encuentra "Asignado"')
                    pause_screen()
                    clear_screen()
                    validar_activo()
                elif estado == '2':
                    print('El activo se encuentra "Dado de Baja"')
                    pause_screen()
                    clear_screen()
                    validar_activo()
                elif estado == '3':
                    print('El activo se encuentra "En Reparacion y/o Garantía"')
                    pause_screen()
                    clear_screen()
                    validar_activo()

    return asignados


def add_asignacion():

    inventario = read_file('inventario.json')
    num_asignacion = validar_num_asignacion()
    fecha_asignacion = str(input('Ingrese la Fecha de la asignación'))
    tipo_asignacion = val_tipo_asignacion()
    if tipo_asignacion == 'Personal':
        id = validar_id()
        nombre = inventario['personal'][id]['name']
    else:
        id = validar_zona_asignada()
        nombre = inventario['zonas'][id]['NombreZona']
    activos_asignados = validar_activo()

    # NO SE DEBE PERMITIR ASIGNAR ACTIVOS(FALSOS POSITIVOS) QUE SE ENCUENTREN DADOS DE BAJA
    # PARA ASIGNAR UN EQUIPO ESTE DEBE ESTAR EN ESTADO NO ASIGNADO.
    # CodCampus=validar_activo

    asignacion = {
        'num_asignacion': str(num_asignacion).zfill(3),
        'fecha_asignacion': fecha_asignacion,
        'tipo_asignacion ': tipo_asignacion,
        'asignado_a': [id, nombre.capitalize()],
        'activos_asignados': activos_asignados
    }
    inventario.get('asignaciones').update(
        {str(num_asignacion).zfill(3): asignacion})
    update_file('inventario.json', inventario)
