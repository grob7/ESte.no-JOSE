from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#print(lifestore_searches[0])

''' Login
credencialies

usuario: RobertoGarcia
contraseña: Emtechzy1-RG

'''
#intentos 
intentos = 0
#Lista de Usuarios y Contraseña
l_usuarios = ['JimmyNeutron', 'RobertoGarcia', 'Emtech','Santander']
l_contraseñas = ['BoyGenius','Emtechzy1-RG', 'Institute', 'BancoSerio']
acceso = False
#Mensaje de Bienvenida
mensaje_bienvenida = 'Bienvenido al sistema \nIngresa Usuario y Contraseña'
print(mensaje_bienvenida)
#Bucle while mas intentos
while not acceso:
    #Funcion Input
    #Ingresa credenciales
    usuario = input('Usuario: ')
    contraseña = input('Contraseña: ')
    intentos += 1
    #Se revisa si hay usuario y contraseña registrado
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


