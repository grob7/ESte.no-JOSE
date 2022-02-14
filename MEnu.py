from lifestore_file import *

# print('El valor promedio de los primeros 10 prod: ', suma/10)


def login():
    ''' Login
credencialies

usuario: RobertoGarcia
contraseña: Emtechzy1-RG

'''
    acceso = False
    intentos = 0

    #Lista de Usuarios y Contraseña
    l_usuarios = ['JimmyNeutron', 'RobertoGarcia', 'Emtech','Santander']
    l_contraseñas = ['BoyGenius','Emtechzy1-RG', 'Institute', 'BancoSerio']

    #Mensaje de Bienvenida
    mensaje_bienvenida = 'Bienvenido al sistema \nIngresa Usuario y Contraseña'
    print(mensaje_bienvenida)

    ##Bucle while mas intentos
    while not acceso:
        #Funcion input
        #Se revisa si hay usuario y contraseña registrado
        usuario = input('Usuario: ')
        contraseña = input('Contraseña: ')
        intentos += 1
        # Reviso si el par coincide
        if usuario in l_usuarios and contraseña in l_contraseñas:
            intentos -= 1
            acceso = True
            print('Hola, Bienvenido al Sistema')
        else:
            #imprime los intentos
            print(f'Tienes {4-intentos} intentos restantes')
            if usuario == l_usuarios: 
                print('Usuario o contraseña incorrecto')
            else:
                print('Usuario o contraseña incorrecto')
            #Acceso bloqueado
        if intentos == 4:
            print('Acceso bloqueado')
            exit()


def punto_2():
    # id : [reviews]
    prod_reviews = {}
    for sale in lifestore_sales:
        # prod y review de venta
        prod_id = sale[1]
        review = sale[2]
        # categorizar por id
        if prod_id not in prod_reviews.keys():
            prod_reviews[prod_id] = []
        prod_reviews[prod_id].append(review)

    # id : [rev_prom, cant]
    id_rev_prom = {}
    for id, reviews in prod_reviews.items():
        # print(id, reviews)
        rev_prom = sum(reviews) / len(reviews)
        rev_prom = int(rev_prom*100)/100
        id_rev_prom[id] = [rev_prom, len(reviews)]

    # Para ordenar siempre es mas facil usar listas.
    dicc_en_list = []
    for id, lista in id_rev_prom.items():
        # print(id, rev_prom)
        rev_prom = lista[0]
        cant = lista[1]
        sub = [id, rev_prom, cant]
        dicc_en_list.append(sub)

    dicc_en_list = sorted(dicc_en_list, key=lambda x: x[1], reverse=True)
    for sublista in dicc_en_list[:5]:
        id, rev, num = sublista
        indice_lsp = id - 1
        prod = lifestore_products[indice_lsp]
        nombre = prod[1]
        nombre = nombre.split(' ')
        nombre = ' '.join(nombre[:4])
        print(
            f'El producto "{nombre}":\n\trev_prom: {rev}, num de ventas: {num}')


def menu():
    login()
    while True:
        print('Que operacion desea hacer:')
        print('\t1. Realizar el punto 1')
        print('\t2. Realizar el punto 2')
        print('\t0. Salir')
        seleccion = input('> ')
        if seleccion == '1':
            continue
        elif seleccion == '2':
            punto_2()
            print('\n')
        elif seleccion == '0':
            exit()
        else:
            print('Opcion invalida!')

menu()
