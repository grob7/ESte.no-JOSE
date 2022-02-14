from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
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
# #Categorias (imprimiendo las menores busquedas por cateogia)
# srchs_process = lista_srchs[0:9]
# srchs_tarjetavideo = lista_srchs[9:22]
# srchs_t_madre = lista_srchs[22:31]
# srchs_driv_hd = lista_srchs[31:43]
# #srchs_mem_ussb = lista_srchs[43:42]
# srchs_pantallas = lista_srchs[43:48]
# srchs_bocinas = lista_srchs[48:51]
# srchs_audifonos = lista_srchs[51:57]
# #print(srchs_process)

# srchs_process_1 = sorted(srchs_process, key= lambda x:x[1], reverse=True)
# srchs_tarjetavideo_1 = sorted(srchs_tarjetavideo, key=lambda a:a[1], reverse=True)
# srchs_t_madre_1 = sorted(srchs_t_madre, key=lambda b:b[1], reverse=True)
# srchs_driv_hd_1 = sorted(srchs_driv_hd, key=lambda c:c[1], reverse=True)
# #srch_mem_usb_ = sorted(mem_ussb, key=lambda d:d[1], reverse=True)
# srchs_pantallas_1 = sorted(srchs_pantallas, key=lambda e:e[1], reverse=True)
# srchs_bocinas_1 = sorted(srchs_bocinas, key=lambda e:e[1], reverse=True)
# srchs_audifonos_1 = sorted(srchs_audifonos, key=lambda f:f[1], reverse=True)

# print('BUSQUEDAS PARA PROCESADORES')
# print(f'\t{srchs_process}')
# print(f'\n5 Procesadores con mayores busquedas: \n\n\t{srchs_process_1[0:5]}\n')
# print('TARJETA DE VIDEO')
# print(f'\t{srchs_tarjetavideo}')
# print(f'\n5 Tarjetas de Video con mayores busquedas: \n\n\t{srchs_tarjetavideo_1[0:5]}\n')
# print('TARJETA MADRE')
# print(f'\t{srchs_t_madre}')
# print(f'\n5 Tarjetas Madre con mayores busquedas: \n\n\t{srchs_t_madre_1[0:5]}\n')
# print('DISCOS DUROS')
# print(f'\t{srchs_driv_hd}')
# print(f'\n5 Discos Duros con mayores busquedas: \n\n\t{srchs_driv_hd_1[0:5]}\n')
# # print('MEMORIAS USB')
# # print(f'\t{sr}')
# # print(f'\n5 Memorias USB con menores busquedas: \n\n\t{mem_ussb_ord[0:5]}\n')
# print('PANTALLAS')
# print(f'\t{srchs_pantallas}')
# print(f'\n5 Pantallas con mayores busquedas: \n\n\t{srchs_pantallas_1[0:5]}\n')
# print('AUDIFONOS')
# print(f'\t{srchs_audifonos}')
# print(f'\n5 Audifonos con mayores busquedas: \n\n\t{srchs_audifonos_1[0:5]}\n')
