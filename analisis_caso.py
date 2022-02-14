from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


''' Analisis del Caso'''

#Imprimiendo lista de productos
''' #Ejemplo 1 imprimiendo productos
for producto in lifestore_products:
    print(producto)
'''
#Imprimiendo precios
''' #Ejemplo 2 imprimiendo precio de productos
for producto in lifestore_products:
    precio = producto[2]
    print(precio)
'''

#Imprimiendo producto y su precio
''' #Ejemplo 3 Impreime cada producto con su respectivo precio
for producto in lifestore_products:
    nombre = producto[1]
    precio = producto[2]
    #print (nombre, precio)
    print(f'El producto " {nombre[:15]}" cuesta: {precio}')
'''
#Imprimiendo obteniendo una columna de nuestra tabla
#precios = []
#for producto in lifestore_products:
    #precio = producto[2]
    #precios.append(precio)
#print(precios)

#Teniendo la columna de precios podemos analizar
#Ejemplo 5 Calculando el promedio de una columna

#suma = sum(precios)
#cantidad_datos = len(precios)
#promedio_precios = suma / cantidad_datos
#print(f'El promedio de precios es {promedio_precios}')

#Ejemplo 6 forma rapida de extraer una columna
#precios = [producto[2] for producto in lifestore_products]
#print(precios)

#Ejemplo 7 Estraer mas de una columna, de manera mas rapida
#nombre_precio = [[producto[1], producto[2]] for producto in lifestore_products ]
#for elemente in nombre_precio:
    #print(elemente)

id_categoria = [ [producto[0], producto[3]] for producto in lifestore_products ]
#print(id_categoria)

#Ejemplo 8 Usanso diccionarios para clasificar

productos_clasificados = {}
for par in id_categoria:
    id = par[0]
    cat = par[1]
    if cat not in productos_clasificados.keys():
        productos_clasificados[cat] = []        
    productos_clasificados[cat].append(id)
#print(productos_clasificados)

#Traer ventas netas (id sale, refund y date)
#id_y_refund = [[sale[0], sale[4], sale[3]] for sale in lifestore_sales if sale[4] == 0]
#for par in id_y_refund:
    #print(par)



#Traer ventas por id venta, id producto y date (ventas brutas)
#f_ventas = [ [sale[0], sale[1], sale[3]] for sale in lifestore_sales]
#for tri in f_ventas:
    #print(tri)

#Dividir por meses las ventas 
id_fecha = [[sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0]
#Para categorizar usamos un diccionario
categorizacion_meses = {}

for meses in id_fecha:
    #Tengo ID y Mes
    id = meses [0]
    _, mes, _ = meses[1].split('/')
    #Si el mes aun no existe como llave, la creamos
    if mes not in categorizacion_meses.keys():
        categorizacion_meses[mes] = []
    categorizacion_meses[mes].append(id)
for key in categorizacion_meses.keys():
    print(key)
    print(categorizacion_meses[key])

#Realizar suma de las ventas del mes

for key in categorizacion_meses.keys():
    lista_mes = categorizacion_meses[key]
    suma_venta = 0
#lista_enero = categorizacion_meses['01']
    for id_venta in lista_mes:
        indice = id_venta - 1
        info_venta = lifestore_sales[indice]
        id_product = info_venta[1]
        precio = lifestore_products[id_product - 1][2]
        suma_venta += precio
    print(key, suma_venta, f'ventas totales: {len(lista_mes)}')

#Encontrar la info para cada categoria

#Hacer el analisis de reviews por categoria tambien la de ventas
prod_reviews = {}
for sale in lifestore_sales:
    #prod y review de venta
    prod_id = sale[1]
    review = sale[2]
    #categorizar por id
    if prod_id not in prod_reviews.keys():
        prod_reviews[prod_id] = []
    prod_reviews[prod_id].append(review)

category_ids = {}
for prod in lifestore_products:
    prod_id = prod[0]
    category = prod[3]
    if category not in category_ids.keys():
        category_ids[category] = []
    category_ids[category].append(prod_id)

# Nuevo diccionario de resultados por categoria
# cat -> id -> reviews -> la cantidad de reviews es la cantidad de ventas
resultados_por_categoria = {}
for category, prod_id_list in category_ids.items():
    reviews = []
    ganancias = 0 
    ventas = 0
    for prod_id in prod_id_list:
        if prod_id not in prod_reviews.keys():
            continue
        reviews_ventas = prod_reviews[prod_id]
        precio = lifestore_products[prod_id][2]
        total_sales = len(reviews_ventas)
        g = precio * total_sales
        reviews += reviews_ventas
        ganancias += g
        ventas += total_sales

    prom_reviews = sum(reviews) / len(reviews)

    resultados_por_categoria[category] = {
    'review_promedio':prom_reviews,
    'gnanacias': ganancias,
    'ventas_totales': ventas
    }
print(resultados_por_categoria)
for cat, dic in resultados_por_categoria.items():
    print(cat)
    for key, val in dic.items():
        print(f'\t {key} : {val}')


#Podemos encontrar la review por producto especificandolo dentro del print
#print(prod_reviews)

#
#for key, values in category_ids.items():
    #print(key)
    #print(values)
