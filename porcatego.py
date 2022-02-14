from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
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
print(f'\t{process}')
print(f'\n5 Procesadores con mayores ventas: \n\n\t{process_ord[0:5]}\n')
print('TARJETA DE VIDEO')
print(f'\t{tarjetavideo}')
print(f'\n5 Tarjetas de Video con mayores ventas: \n\n\t{tarjetavideo_ord[0:5]}\n')
print('TARJETA MADRE')
print(f'\t{t_madre}')
print(f'\n5 Tarjetas Madre con mayores ventas: \n\n\t{t_madre_ord[0:5]}\n')
print('DISCOS DUROS')
print(f'\t{driv_hd}')
print(f'\n5 Discos Duros con mayores ventas: \n\n\t{drive_hd_ord[0:5]}\n')
print('MEMORIAS USB')
print(f'\t{mem_ussb}')
print(f'\n5 Memorias USB con mayores ventas: \n\n\t{mem_ussb_ord[0:5]}\n')
print('PANTALLAS')
print(f'\t{pantallas}')
print(f'\n5 Pantallas con mayores ventas: \n\n\t{pantallas_ord[0:5]}\n')
print('AUDIFONOS')
print(f'\t{audifonos}')
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

# print('PROCESADORES')
# print(f'\t{process}')
# print(f'\n5 Procesadores con menores ventas: \n\n\t{process_ord[0:5]}\n')
# print('TARJETA DE VIDEO')
# print(f'\t{tarjetavideo}')
# print(f'\n5 Tarjetas de Video con menores ventas: \n\n\t{tarjetavideo_ord[0:5]}\n')
# print('TARJETA MADRE')
# print(f'\t{t_madre}')
# print(f'\n5 Tarjetas Madre con menores ventas: \n\n\t{t_madre_ord[0:5]}\n')
# print('DISCOS DUROS')
# print(f'\t{driv_hd}')
# print(f'\n5 Discos Duros con menores ventas: \n\n\t{drive_hd_ord[0:5]}\n')
# print('MEMORIAS USB')
# print(f'\t{mem_ussb}')
# print(f'\n5 Memorias USB con menores ventas: \n\n\t{mem_ussb_ord[0:5]}\n')
# print('PANTALLAS')
# print(f'\t{pantallas}')
# print(f'\n5 Pantallas con menores ventas: \n\n\t{pantallas_ord[0:5]}\n')
# print('AUDIFONOS')
# print(f'\t{audifonos}')
# print(f'\n5 Audifonos con menores ventas: \n\n\t{audifonos_ord[0:5]}\n')














regreso = [[reg[1], reg[4]] for reg in lifestore_sales if reg[4]==1]
print(regreso)

stock = [[stk[0], stk[4]] for stk in lifestore_products]
print(stock)

stock_max_min = sorted(stock, key=lambda x:x[1], reverse=True)
print(stock_max_min)


# # #Hacemos diccionario para clasificas las busquedas que  tiene cada producto
# stck_x_prod = {}
# for stckq in stock:
#     id_stck = stckq[0] 
#     prod_stck = stckq[1]
#     if id_stck not in stck_x_prod.keys():
#         stck_x_prod[id_stck] = []
#     stck_x_prod[id_stck].append(prod_stck)
# #print(stck_x_prod)
# for n in stck_x_prod:
#     stok = (stck_x_prod[1])
#     print(stok)

# mes_stck = {}
# for mess, ids_vstckenta in stck_x_prod.items():
#     lista_stck = ids_vstckenta
#     suma_stck = 0
#     for id_vstckenta in lista_stck:
#         indicee = id_vstckenta - 1
#         info_stck = lifestore_sales[indicee]
#         id_productstck = info_stck[1]
#         info_stck1 = lifestore_products[id_productstck-1]
#         preciostck = info_stck1[2]
#         suma_stck += preciostck
#     print(mess, suma_stck, f'ventas totales: {len(lista_stck)}')
#     #print(suma_venta)
#     #print(mes)
#     mes_stck[mess] = [suma_stck, len(lista_stck)]
# #print(mes_info)
# #PARA ORDERNAR Y SUMAR YA QUE NO PUEDES ORDENAR UN DICCIONARIO POR DEFINICION
# #CREAMOS UNA LISTA 
#print(id_ventas)


#Hacermos lista para conocer el numero de stock por producto

# lista_stck = []

# for t, y in stck_x_prod.items():
#     w = (len(y))
#     stckilista = [t, w]
#     lista_stck.append(stckilista)
    #if cosa != conteo:
        #print(cosa, len(conteo))

    #print(len(producto_ventas))
#print(f'{lista_stck}\n\n\n\n')#Conocer el total numero de stock por ID PRODUCTO
#elemstck_porcategoria = (len(lista_stck))
#print (elementos_porcategoria)
