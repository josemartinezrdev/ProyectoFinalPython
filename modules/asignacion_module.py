from modules.core_files import read_file, update_file, clear_screen, pause_screen
# valida el tipo de asignaciones
def val_tipo_asignacion():

    try:
        print('Ingrese el tipo de asignación que desea registrar: ')
        print('1. Personal \n2. Zona')
        opt = input('-')
        if opt == '1':
            tipo_asignacion = 'Personal'
            return tipo_asignacion
        elif opt =='2':
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
    
    if ('z'+str( opcion_zona).zfill(3)) in inventario['zonas']:
        
        return opcion_zona
    else:
        print('Opción Incorrecta, Rectifique el número de zona')
        pause_screen()
        clear_screen()
        validar_zona_asignada()


def validar_activo():
    inventario = read_file('inventario.json')
    asignados = []
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
            if estado == '0':
                asignados.append(CodCampus)
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
    fecha_asignacion = str(input('Ingrese la Fecha de la asignación: '))
    tipo_asignacion = val_tipo_asignacion()
    activos_asignados = validar_activo()
    for i in activos_asignados:
        inventario['activos'][i]['estado'] = '1'
    if tipo_asignacion == 'Personal':
        id = validar_id()
        nombre = inventario['personal'][id]['name']
    else:
        id = 'z'+((validar_zona_asignada()).zfill(3))
        nombre = inventario['zonas'][id]['nombre_zona']
    asignacion = {
        'fecha_asignacion': fecha_asignacion,
        'tipo_asignacion ': tipo_asignacion,
        'asignado_a': [id, nombre.capitalize()],
        'activos_asignados': activos_asignados
    }
    inventario.get('asignaciones').update({id: asignacion})
    update_file('inventario.json', inventario)
