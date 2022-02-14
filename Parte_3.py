from lifestore_file import lifestore_products, lifestore_sales


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
