from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

# Señalar los id correspondientes a cada categoria
id_categoria = [[producto[0], producto[3]] for producto in lifestore_products]
#Creamos diccionario
clasificacion_productos = {}
for duo in id_categoria:
    id = duo[0]
    categ = duo[1]
    if categ not in clasificacion_productos:
        clasificacion_productos[categ] = []
    clasificacion_productos[categ].append(id)
#print(f'\n {clasificacion_productos}')
# for id, categ in clasificacion_productos.items():
#     print(f'\n{id}')
#     print(categ)
    
#print(f'Los id correspodientes a la categoria Procesadores son: \n{clasificacion_productos["procesadores"]}')

#print(f'\tLas ventas mensaules de esta categoria son las siguientes: ')
#Dividir por meses las ventas 
id_fecha = [[sale[0], sale[3]] for sale in lifestore_sales]
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
    fdfs=1
    #print(key)
    #print(categorizacion_meses[key])



lista_1 = []
lista_1.append(id_fecha)
print(lista_1)
