import modules.core_files as cf
from modules.activos_module import clear_screen,pause_screen
# valida el numero de asignacion
def validar_Nasignacion():
    
    inventario = cf.read_file('inventario.json')
    try:
        numero_asignacion = int(input('Ingrese el numero de la asignacion: '))
        if numero_asignacion in inventario['asignacion'] :
            print('El numero de asignacion ya se encuentra reguistrado')
            pause_screen()
            clear_screen()
            return validar_Nasignacion()
        if numero_asignacion < 0: 
            print('Numero de asignacion Invalido')
            pause_screen()
            clear_screen()
            return validar_Nasignacion()

    except ValueError:
        print('Numero invalido')
        pause_screen()
        clear_screen()
        return validar_Nasignacion()
    return numero_asignacion


# valida el tipo de asignacion
def val_tipo_asignacion():
     
    try:
        print('Ingrese el tipo de asignacion que desea registrar: ')
        print('1.Personal \n 2.Zona')
        opc=input('-')
        if opc =='1':
            tipo_asignacion='Personal'
            return tipo_asignacion
        elif opc =='2':
            tipo_asignacion='zona'
            return tipo_asignacion
        else:
            print('Opcion Incorrecta')
            pause_screen()
            clear_screen()
            val_tipo_asignacion()
    except ValueError:
        print('Opcion Incorrecta')
        pause_screen()
        clear_screen()
        val_tipo_asignacion()
#valida el id de la persona que adquiere el activo
def validar_id():
    inventario = cf.read_file('inventario.json') 
    id_persona=input('Ingrese el Id de la persona')
    if id_persona in inventario['personal']:
        nombre=inventario.get('personal').get(id_persona).get('name')
        print(nombre)
        return id_persona
    else:
        print('El Id no se encuentra Registrado')
        pause_screen()
        clear_screen()
        validar_id()
def validar_zona_asignada():
    inventario = cf.read_file('inventario.json')
    opcion_zona=input('Ingrese el numero de la zona: ')
    if opcion_zona in inventario['zonas']:
        return opcion_zona
    else:  
        print('Opcion Incorrecta, Recctifique numero de zona')
        pause_screen()
        clear_screen()
        validar_zona_asignada()

def validar_activo():
    inventario = cf.read_file('inventario.json') 
    CodCampus=input('Ingrese el CodCampus del activo')
def agregar_asignacion():

    inventario = cf.read_file('inventario.json') 
    numero_asignacion=validar_Nasignacion()
    fecha_asignacion=str(input('Ingrese la Fecha de la asignacion'))
    tipo_asignacion=val_tipo_asignacion()
    if tipo_asignacion=='Personal':
        id=validar_id()
        nombre=inventario['personal'][id]['name']
    else:
        id= validar_zona_asignada()
        nombre= inventario['zonas'][id]['Nombre Zona']

    # NO SE DEBE PERMITIR ASIGNAR ACTIVOS QUE SE ENCUENTREN DADOS DE BAJA
    # PARA ASIGNAR UN EQUIPO ESTE DEBE ESTAR EN ESTADO NO ASIGNADO.

    asignacion={
        'nAsignacion':str(numero_asignacion).zfill(3),
        'FechaAsignación':fecha_asignacion,
        'TipoAsignacion ':tipo_asignacion,
        'AsignadoA':[id,nombre],
        'Activos':''
    }
    print(asignacion)



    