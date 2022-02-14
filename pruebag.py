from lifestore_file import lifestore_products,lifestore_sales,lifestore_searches


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