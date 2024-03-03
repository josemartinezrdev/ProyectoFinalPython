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
            tipo_asignacion = 'Zona'
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
    asignados = []
    id_persona = input('Ingrese el Id de la persona: ')
    if id_persona in inventario['personal']:
        nombre = inventario.get('personal').get(id_persona).get('name')
        print(nombre)
        activo = validar_activo(asignados)
        op = True
        while op:
            list_opciones = ['s','n']                
            opcion = input('Desea agregar otro activo? s(Si) n(No)').lower()
            if opcion in list_opciones:
                if opcion == 's':
                        asignados.append(activo)
                        activo=validar_activo(asignados)
                else: 
                    if opcion == 'n':
                        asignados.append(activo)
                        op = False
            else: 
                print('Opcion Incorrecta')
                pause_screen()
                clear_screen()
        return id_persona, asignados
    else:
        print('El Id no se encuentra registrado')
        pause_screen()
        clear_screen()
        validar_id()

def validar_zona_asignada():
    inventario = read_file('inventario.json')
    opcion_zona = input('Ingrese el número de la zona: ')
    opcion_zona = str(opcion_zona).zfill(3)
    opcion_zona = 'z' + opcion_zona
    capacidad = inventario['zonas'][opcion_zona]['capacidad_zona']
    asignados = []
    if opcion_zona in inventario['zonas']:
        
        def validar_capacidad(): 
            global activo
            activo = validar_activo(asignados)
            if (activo[:2] == 'cp')and (inventario['zonas'][opcion_zona]['ex_cpu']) == capacidad:
                print(f'Lo sentimos, la Capacidad de la zona {opcion_zona} para CPU se encuentra llena')
                validar_capacidad()
            else:
                if activo[:3] == 'mou' and (inventario['zonas'][opcion_zona]['ex_mou']) == capacidad:
                    print(f'Lo sentimos, la Capacidad de la zona{opcion_zona} para Mouse se encuentra llena')
                    validar_capacidad()
                else:
                    if activo[:3] == 'mon' and (inventario['zonas'][opcion_zona]['ex_mon']) == capacidad:
                        print(f'Lo sentimos, la Capacidad de la zona{opcion_zona} para Monitores se encuentra llena')
                        validar_capacidad()
                    else:
                        if activo[:2] == 'te' and (inventario['zonas'][opcion_zona]['ex_tec']) == capacidad:
                            print(f'Lo sentimos, la Capacidad de la zona{opcion_zona} para teclados se encuentra llena')
                            validar_capacidad()
        validar_capacidad()
        global activo   
        
        op = True
        while op:
            list_opciones = ['s','n']                
            opcion = input('Desea ingresar otro activo? s(Si) n(No)').lower()
            if opcion in list_opciones:
                if opcion == 's':
                        asignados.append(activo)
                        validar_capacidad()
                else: 
                    if opcion == 'n':
                        asignados.append(activo)
                        op = False
            else: 
                print('Opcion Incorrecta')
                pause_screen()
                clear_screen()
        return opcion_zona, asignados
    else:
        print('Opción Incorrecta, Rectifique el número de zona')
        pause_screen()
        clear_screen()
        return validar_zona_asignada()

def validar_activo(asignados:list):
    inventario = read_file('inventario.json')
    CodCampus = input('Ingrese el "Código Campus" del activo: ')
    if CodCampus not in asignados:
        if CodCampus not in inventario['activos']:
            print('El código ingresado no corresponde a ningún activo')
            pause_screen()
            clear_screen()
            return validar_activo(asignados)
        else:
            estado = inventario['activos'][CodCampus]['estado']
            if estado == '0':
                    return CodCampus
            else:
                if estado == '1':
                    print('El activo ya se encuentra "Asignado"')
                    pause_screen()
                    clear_screen()
                    return validar_activo(asignados)
                elif estado == '2':
                    print('El activo se encuentra "Dado de Baja"')
                    pause_screen()
                    clear_screen()
                    return validar_activo(asignados)
                elif estado == '3':
                    print('El activo se encuentra "En Reparacion y/o Garantía"')
                    pause_screen()
                    clear_screen()
                    return validar_activo(asignados)
    else:
        print('El activo ya se encuentra asignado')
        return validar_activo(asignados)

def add_asignacion():
    inventario = read_file('inventario.json')
    fecha_asignacion = str(input('Ingrese la Fecha de la asignación: '))
    tipo_asignacion = val_tipo_asignacion()
    if tipo_asignacion == 'Personal':
        id_personas,asignados = validar_id()
        id = id_personas
        nombre = inventario['personal'][id]['name']
        for i in asignados:
                inventario['activos'][i]['estado'] = '1'
    else:
        opcion_zona,asignados = validar_zona_asignada()
        id = opcion_zona
        for i in asignados:
            inventario['activos'][i]['estado'] = '1'
        nombre = inventario['zonas'][id]['nombre_zona']
        for i in range(len(asignados)):
            if asignados[i][:2] == 'cp':
                inventario['zonas'][id]['ex_cpu'] += 1
            else:
                if asignados[i][:3] == 'mon':
                    inventario['zonas'][id]['ex_mon'] += 1
                else:
                    if asignados[i][:3] == 'mou':
                        inventario['zonas'][id]['ex_mou'] += 1
                    else: 
                        if asignados[i][:2] == 'te':
                            inventario['zonas'][id]['ex_tec'] += 1
    if id in inventario['asignaciones']:
        inventario['asignaciones'][id]['activos_asignados'].extend(asignados)
    else:
        asignacion = {
            'fecha_asignacion': fecha_asignacion,
            'tipo_asignacion ': tipo_asignacion,
            'asignado_a': [id, nombre.capitalize()],
            'activos_asignados':asignados
        }
        inventario.get('asignaciones').update({id: asignacion})
    update_file('inventario.json', inventario)
