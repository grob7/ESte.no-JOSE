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

def puntouno():
    #Trae procesadores producto
    procesaducto = [[prose[0], prose[3]] for prose in lifestore_products] #if prose[3]=='procesadores']
    #print(f'\n{procesaducto}\n') #ID DE PRODUCTO Y CATEGORIA

    catego = {}
    for dyze in procesaducto:
        wisin = dyze[0]
        yandel = dyze[1]
        if yandel not in catego.keys():
            catego[yandel] = []        
        catego[yandel].append(wisin)
    #print(catego)

    menoventas = [[meno[0], meno[1]] for meno in lifestore_sales if meno[4]==0]
    #print(menoventas) #ID de VENTA y ID PRODUCTO

    prrrr = {}
    for n in menoventas:
        id = n[0]
        cat = n[1]
        if cat not in prrrr.keys():
            prrrr[cat] = []        
        prrrr[cat].append(id)
    #print(prrrr)

    porca = []

    for c, z in prrrr.items():
        w = (len(z))
        prrlista = [c, w]
        porca.append(prrlista)
        #if cosa != conteo:
            #print(cosa, len(conteo))

        #print(len(producto_ventas))
    #print(f'{porca}\n\n\n\n')
    elementos_porcategoria = (len(porca))
    #print (elementos_porcategoria)
    #print( sorted(porca, key=lambda x:x[1], reverse=True))

    #Categorias (imprimiendo las mayores ventas)
    process = porca[0:8]  ###############################REIVASR DETALLLES (DE ESTOS INDICES)
    tarjetavideo = porca[8:17]  #########################REVISAR DETELLAS (DE ESTOS INDICES)
    t_madre = porca[17:23]
    driv_hd = porca[23:31]
    mem_ussb = porca[31:32]
    pantallas = porca[32:35]
    bocinas = porca[35:36]
    audifonos = porca[36:40]


    # print(process)
    # # ############################################################################

    process_ord = sorted(process, key= lambda x:x[1], reverse=True)
    tarjetavideo_ord = sorted(tarjetavideo, key=lambda a:a[1], reverse=True)
    t_madre_ord = sorted(t_madre, key=lambda b:b[1], reverse=True)
    drive_hd_ord = sorted(driv_hd, key=lambda c:c[1], reverse=True)
    mem_ussb_ord = sorted(mem_ussb, key=lambda d:d[1], reverse=True)
    pantallas_ord = sorted(pantallas, key=lambda e:e[1], reverse=True)
    audifonos_ord = sorted(audifonos, key=lambda f:f[1], reverse=True)
    print(process_ord)

    print('PROCESADORES')
    # print(f'\t{process}')
    print(f'\n5 Procesadores con mayores ventas: \n\n\t{process_ord[0:5]}\n')
    print('TARJETA DE VIDEO')
    # print(f'\t{tarjetavideo}')
    print(f'\n5 Tarjetas de Video con mayores ventas: \n\n\t{tarjetavideo_ord[0:5]}\n')
    print('TARJETA MADRE')
    # print(f'\t{t_madre}')
    print(f'\n5 Tarjetas Madre con mayores ventas: \n\n\t{t_madre_ord[0:5]}\n')
    print('DISCOS DUROS')
    # print(f'\t{driv_hd}')
    print(f'\n5 Discos Duros con mayores ventas: \n\n\t{drive_hd_ord[0:5]}\n')
    print('MEMORIAS USB')
    # print(f'\t{mem_ussb}')
    print(f'\n5 Memorias USB con mayores ventas: \n\n\t{mem_ussb_ord[0:5]}\n')
    print('PANTALLAS')
    # print(f'\t{pantallas}')
    print(f'\n5 Pantallas con mayores ventas: \n\n\t{pantallas_ord[0:5]}\n')
    print('AUDIFONOS')
    # print(f'\t{audifonos}')
    print(f'\n5 Audifonos con mayores ventas: \n\n\t{audifonos_ord[0:5]}\n')

    # ###############################################################################################

    process_ord = sorted(process, key= lambda x:x[1], reverse=False)
    tarjetavideo_ord = sorted(tarjetavideo, key=lambda a:a[1], reverse=False)
    t_madre_ord = sorted(t_madre, key=lambda b:b[1], reverse=False)
    drive_hd_ord = sorted(driv_hd, key=lambda c:c[1], reverse=False)
    mem_ussb_ord = sorted(mem_ussb, key=lambda d:d[1], reverse=False)
    pantallas_ord = sorted(pantallas, key=lambda e:e[1], reverse=False)
    audifonos_ord = sorted(audifonos, key=lambda f:f[1], reverse=False)
    #print(process_ord)

    print('PROCESADORES')
    # print(f'\t{process}')
    print(f'\n5 Procesadores con menores ventas: \n\n\t{process_ord[0:5]}\n')
    print('TARJETA DE VIDEO')
    # print(f'\t{tarjetavideo}')
    print(f'\n5 Tarjetas de Video con menores ventas: \n\n\t{tarjetavideo_ord[0:5]}\n')
    print('TARJETA MADRE')
    # print(f'\t{t_madre}')
    print(f'\n5 Tarjetas Madre con menores ventas: \n\n\t{t_madre_ord[0:5]}\n')
    print('DISCOS DUROS')
    # print(f'\t{driv_hd}')
    print(f'\n5 Discos Duros con menores ventas: \n\n\t{drive_hd_ord[0:5]}\n')
    print('MEMORIAS USB')
    # print(f'\t{mem_ussb}')
    print(f'\n5 Memorias USB con menores ventas: \n\n\t{mem_ussb_ord[0:5]}\n')
    print('PANTALLAS')
    # print(f'\t{pantallas}')
    print(f'\n5 Pantallas con menores ventas: \n\n\t{pantallas_ord[0:5]}\n')
    print('AUDIFONOS')
    # print(f'\t{audifonos}')
    print(f'\n5 Audifonos con menores ventas: \n\n\t{audifonos_ord[0:5]}\n')














    regreso = [[reg[1], reg[4]] for reg in lifestore_sales if reg[4]==1]
    print(regreso)

    stock = [[stk[0], stk[4]] for stk in lifestore_products]
    #print(stock)

    stock_max_min = sorted(stock, key=lambda x:x[1], reverse=True)
    #print(stock_max_min)

    #Trae procesadores producto
    procesa_searchs = [[searches[0], searches[3]] for searches in lifestore_products] #'''#if prose[3]=='procesadores']'''
    #print(f'\n{procesa_srchs}\n') #ID DE PRODUCTO Y CATEGORIA

    categorias_searchs = {}
    for tony in procesa_searchs:
        farruko = tony[0]
        delaghetto = tony[1]
        if delaghetto not in categorias_searchs.keys():
            categorias_searchs[delaghetto] = []        
        categorias_searchs[delaghetto].append(farruko)
    #print(categorias_searchs)

    #Traer searches 
    meno_srch = [[srchs[0], srchs[1]] for srchs in lifestore_searches]
    #print(meno_srch)

    #Hacemos diccionario para clasificas las busquedas que  tiene cada producto
    busq_x_prod = {}
    for busq in meno_srch:
        id_srch = busq[0] 
        prod_srch = busq[1]
        if prod_srch not in busq_x_prod.keys():
            busq_x_prod[prod_srch] = []
        busq_x_prod[prod_srch].append(id_srch)
    #print(busq_x_prod)

    #Hacermos lista para conocer el numero de busquedasd por producto
    lista_srchs = []

    for k, v in busq_x_prod.items():
        ñ = (len(v))
        srchsilista = [k, ñ]
        lista_srchs.append(srchsilista)
        #if cosa != conteo:
            #print(cosa, len(conteo))

        #print(len(producto_ventas))
    #print(f'{lista_srchs}\n\n\n\n')#Conocer el total numero de busquedas por ID PRODUCTO
    elementos_porcategoria = (len(lista_srchs))
    #print (elementos_porcategoria)

    '''
    LISTA DE CATEGORIAS
    procesadores: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tarjetas de video: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    tarjetas madre: [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
    discos duros: [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
    memorias usb: [60, 61]
    pantallas: [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]
    bocinas: [74, 75, 76, 77, 78, 79, 80, 81, 82, 83]
    audifonos: [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]
    '''

    #Categorias (imprimiendo las menores busquedas por cateogia)
    srchs_process = lista_srchs[0:9]
    srchs_tarjetavideo = lista_srchs[9:22]
    srchs_t_madre = lista_srchs[22:31]
    srchs_driv_hd = lista_srchs[31:43]
    #srchs_mem_ussb = lista_srchs[43:42]
    srchs_pantallas = lista_srchs[43:48]
    srchs_bocinas = lista_srchs[48:51]
    srchs_audifonos = lista_srchs[51:57]
    print(srchs_process)

    srchs_process_1 = sorted(srchs_process, key= lambda x:x[1], reverse=False)
    srchs_tarjetavideo_1 = sorted(srchs_tarjetavideo, key=lambda a:a[1], reverse=False)
    srchs_t_madre_1 = sorted(srchs_t_madre, key=lambda b:b[1], reverse=False)
    srchs_driv_hd_1 = sorted(srchs_driv_hd, key=lambda c:c[1], reverse=False)
    #srch_mem_usb_ = sorted(mem_ussb, key=lambda d:d[1], reverse=True)
    srchs_pantallas_1 = sorted(srchs_pantallas, key=lambda e:e[1], reverse=False)
    srchs_bocinas_1 = sorted(srchs_bocinas, key=lambda e:e[1], reverse=False)
    srchs_audifonos_1 = sorted(srchs_audifonos, key=lambda f:f[1], reverse=False)
    #print(process_ord)

    print('BUSQUEDAS PARA PROCESADORES')
    print(f'\t{srchs_process}')
    print(f'\n5 Procesadores con menores busquedas: \n\n\t{srchs_process_1[0:5]}\n')
    print('TARJETA DE VIDEO')
    print(f'\t{srchs_tarjetavideo}')
    print(f'\n5 Tarjetas de Video con menores busquedas: \n\n\t{srchs_tarjetavideo_1[0:5]}\n')
    print('TARJETA MADRE')
    print(f'\t{srchs_t_madre}')
    print(f'\n5 Tarjetas Madre con menores busquedas: \n\n\t{srchs_t_madre_1[0:5]}\n')
    print('DISCOS DUROS')
    print(f'\t{srchs_driv_hd}')
    print(f'\n5 Discos Duros con menores busquedas: \n\n\t{srchs_driv_hd_1[0:5]}\n')
    # print('MEMORIAS USB')
    # print(f'\t{sr}')
    # print(f'\n5 Memorias USB con menores busquedas: \n\n\t{mem_ussb_ord[0:5]}\n')
    print('PANTALLAS')
    print(f'\t{srchs_pantallas}')
    print(f'\n5 Pantallas con menores busquedas: \n\n\t{srchs_pantallas_1[0:5]}\n')
    print('AUDIFONOS')
    print(f'\t{srchs_audifonos}')
    print(f'\n5 Audifonos con menores busquedas: \n\n\t{srchs_audifonos_1[0:5]}\n')

    print(f'{srchs_process}\n')
    print(f'{srchs_tarjetavideo}\n')
    print(f'{srchs_t_madre}\n')
    print(f'{srchs_driv_hd}\n')
    ##print(f'{srchs_mem_ussb}\n')
    print(f'{srchs_pantallas}\n')
    print(f'{srchs_bocinas}\n')
    print(f'{srchs_audifonos}\n')
    ####################################################################################################################################
    # ##MAYORES BUSQUEDAS
    #Categorias (imprimiendo las menores busquedas por cateogia)
    srchs_process = lista_srchs[0:9]
    srchs_tarjetavideo = lista_srchs[9:22]
    srchs_t_madre = lista_srchs[22:31]
    srchs_driv_hd = lista_srchs[31:43]
    # srchs_mem_ussb = lista_srchs[43:42]
    srchs_pantallas = lista_srchs[43:48]
    srchs_bocinas = lista_srchs[48:51]
    srchs_audifonos = lista_srchs[51:57]
    # #print(srchs_process)

    srchs_process_1 = sorted(srchs_process, key= lambda x:x[1], reverse=True)
    srchs_tarjetavideo_1 = sorted(srchs_tarjetavideo, key=lambda a:a[1], reverse=True)
    srchs_t_madre_1 = sorted(srchs_t_madre, key=lambda b:b[1], reverse=True)
    srchs_driv_hd_1 = sorted(srchs_driv_hd, key=lambda c:c[1], reverse=True)
    #srch_mem_usb_ = sorted(mem_ussb, key=lambda d:d[1], reverse=True)
    srchs_pantallas_1 = sorted(srchs_pantallas, key=lambda e:e[1], reverse=True)
    srchs_bocinas_1 = sorted(srchs_bocinas, key=lambda e:e[1], reverse=True)
    srchs_audifonos_1 = sorted(srchs_audifonos, key=lambda f:f[1], reverse=True)

    print('BUSQUEDAS PARA PROCESADORES')
    # print(f'\t{srchs_process}')
    print(f'\n5 Procesadores con mayores busquedas: \n\n\t{srchs_process_1[0:5]}\n')
    print('TARJETA DE VIDEO')
    # print(f'\t{srchs_tarjetavideo}')
    print(f'\n5 Tarjetas de Video con mayores busquedas: \n\n\t{srchs_tarjetavideo_1[0:5]}\n')
    print('TARJETA MADRE')
    # print(f'\t{srchs_t_madre}')
    print(f'\n5 Tarjetas Madre con mayores busquedas: \n\n\t{srchs_t_madre_1[0:5]}\n')
    print('DISCOS DUROS')
    # print(f'\t{srchs_driv_hd}')
    print(f'\n5 Discos Duros con mayores busquedas: \n\n\t{srchs_driv_hd_1[0:5]}\n')
    # print('MEMORIAS USB')
    # # print(f'\t{sr}')
    # print(f'\n5 Memorias USB con menores busquedas: \n\n\t{mem_ussb_ord[0:5]}\n')
    print('PANTALLAS')
    # print(f'\t{srchs_pantallas}')
    print(f'\n5 Pantallas con mayores busquedas: \n\n\t{srchs_pantallas_1[0:5]}\n')
    print('AUDIFONOS')
    # print(f'\t{srchs_audifonos}')
    print(f'\n5 Audifonos con mayores busquedas: \n\n\t{srchs_audifonos_1[0:5]}\n')

def puntodos():
        #ORDENAR POR RESEÑA (MEJORES RESEÑAS)

    resultado = {}
    for item in lifestore_sales:
        idproducto = str(item[1])
        if item[4] == 1:
            continue
        if idproducto in  resultado.keys():
            resultado[idproducto][0] = resultado[idproducto][0] + item[2]
            resultado[idproducto][1] = resultado[idproducto][1] + 1
        else:
            resultado[idproducto] = [item[2],1,0]

    for key,value in resultado.items():
        resultado[key][2] = resultado[key][0]/resultado[key][1]

    a = [{"nombre":"a","valor":3},{"nombre":"b","valor":5}]

    listaResultado = list(resultado.items())

    resutltado_ordenado = sorted(listaResultado,key= lambda x : x[1][2],reverse=True)

    #print(resutltado_ordenado[0:5])


    ##################################################################################################

    # ORDENAR RESEÑA (PERORES RESEÑAS)

    resultado = {}
    for item in lifestore_sales:
        idproducto = str(item[1])
        #if item[4] == 0:
            #continue
        if idproducto in  resultado.keys():
            resultado[idproducto][0] = resultado[idproducto][0] + item[2]
            resultado[idproducto][1] = resultado[idproducto][1] + 1
        else:
            resultado[idproducto] = [item[2],1,0]

    for key,value in resultado.items():
        resultado[key][2] = resultado[key][0]/resultado[key][1]

    a = [{"nombre":"a","valor":3},{"nombre":"b","valor":5}]

    listaResultado = list(resultado.items())

    resutltado_ordenado = sorted(listaResultado,key= lambda x : x[1][2],reverse=False)

    print(resutltado_ordenado[0:5])

def puntotres():
        # # Ejemplo 1, imprimiendo los elementos
    # for producto in lifestore_products[:5]:
    #     nombre = producto[1]
    #     precio = producto[2]
    #     # print(nombre[:15], precio)
    #     print(f'El producto: {nombre}\n\tCuesta:{precio}\n')

    # # Encontrar promedio de precios
    # col_precio = []

    # for producto in lifestore_products:
    #     precio = producto[2]
    #     col_precio.append(precio)
    # # Toda la lista
    # print(col_precio)
    # # Suma y cuenta, para calcular promedio
    # suma = sum(col_precio)
    # cuenta = len(col_precio)
    # promedio = suma/cuenta
    # # Imprimir promedio
    # print(promedio)

    # col_precios = [ producto[2] for producto in lifestore_products ]
    # print(sum(col_precios) / len(col_precios))

    # id_y_refund = [ [sale[0], sale[4]] for sale in lifestore_sales if sale[4] == 0]
    # print(id_y_refund)

    # for par in id_y_refund:
    #     print(par)

    # Dividir por meses las ventas
    id_fecha = [ [sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0 ]
    # Para categorizar usamos un diccionario
    categorizacion_meses = {}

    for par in id_fecha:
        # Tengo ID y Mes
        id = par[0]
        _, mes, _ = par[1].split('/')
        # Si el mes aun no existe como llave, la creamos
        if mes not in categorizacion_meses.keys():
            categorizacion_meses[mes] = []
        categorizacion_meses[mes].append(id)

    # mes : [ids de venta]

    # for key in categorizacion_meses.keys():
    #     print(key)
    #     print(categorizacion_meses[key])

    # crear dic
    mes_info = {}
    for mes, ids_venta in categorizacion_meses.items():
        lista_mes = ids_venta
        suma_venta = 0
        for id_venta in lista_mes:
            indice = id_venta - 1
            info_venta = lifestore_sales[indice]
            id_product = info_venta[1]
            info_prod = lifestore_products[id_product-1]
            precio = info_prod[2]
            suma_venta += precio
        #print(mes, suma_venta, f'ventas totales: {len(lista_mes)}')
        #print(suma_venta)
        #print(mes)
        mes_info[mes] = [suma_venta, len(lista_mes)]
    #print(mes_info)
    #PARA ORDERNAR Y SUMAR YA QUE NO PUEDES ORDENAR UN DICCIONARIO POR DEFINICION
    #CREAMOS UNA LISTA 
    #print(id_ventas)
    total_ingresos = [26949 + 107270 + 91936 + 117738 + 191066 + 162931 + 36949 + 3077]
    vents_anuales = [11 + 40 + 34 + 52 + 74 + 49 + 11 + 3]

    #ventas_meses = {}
    #  [7,11],[2,40],[5,34],[1,52],[4,74],[3,49][6,11][8,3]}
    mes_ganancia_ventas = []
    for mes, datos in mes_info.items():
        ganancias, ventas = datos
        sub = [mes, ganancias, ventas]
        mes_ganancia_ventas.append(sub)

    #print(mes_ganancia_ventas)


    ord_mes = sorted(mes_ganancia_ventas)
    ord_gancia = sorted(mes_ganancia_ventas, key=lambda x:x[1], reverse=True)
    ord_ventas = sorted(mes_ganancia_ventas, key=lambda x:x[2], reverse=True)
    print (ord_gancia)
    print(ord_mes)
    print(ord_ventas)
    #print(ord_ventas)

    id_ventas = []
    for prod in lifestore_products:
        id_prod = prod[0]
        sub = [id_prod, 0]
        id_ventas.append(sub)

    for sale in lifestore_sales:
        id_prod = sale[1]
        indice = id_prod - 1
        if sale[-1] == 1:
            continue
        id_ventas[indice][1] += 1


    '''
    Total INGRESO y VENTAS
    mes/ingresos/ventas
    [['07', 26949, 11]
    ['02', 107270, 40]
    ['05', 91936, 34]
    ['01', 117738, 52]
    ['04', 191066, 74]
    ['03', 162931, 49]
    ['06', 36949, 11]
    ['08', 3077, 3]]
    '''
    #Resultados PARTE 3
    #LOS INGRESOS TOTALES ANUALES
    print(f'Los ingresos totales anuales son\n\t{total_ingresos}\n')
    #TOTAL VENTAS ANUALES
    print(f'Las ventas totales anuales son\n\t{vents_anuales}\n')
    #VENTAS PROMEDIO MENSUALES 
    print(f'Las Ventas Promedio Mensuales \n ---mes/ingresos/ventas---\n {ord_ventas}')



def menu():
    login()
    while True:
        print('Que operacion desea hacer:')
        print('\t1. Realizar el punto 1')
        print('\t2. Realizar el punto 2')
        print('\t3. Realizar el punto 3')
        print('\t0. Salir')
        seleccion = input('> ')
        if seleccion == '1':
            puntouno()
            print('\n')
        elif seleccion == '2':
            puntodos()
            print('\n')
        elif seleccion == '3':
            puntotres()
            print('\n')
        elif seleccion == '0':
            exit()
        else:
            print('Opcion invalida!')

menu()
