objetivo = int(input('Ingrese su numero: ')
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = 0.0
funcion = int(input ('Ingrese la función que desee: ')

if funcion == 1:
    enumeracion(objetivo)
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
elif funcion == 2:
    aproximacion(objetivo)
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
elif funcion == 2:
    busqueda_binaria(objetivo)
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def enumeracion ( objetivo):
    while respuesta **2 < objetivo: 
        respuesta += 1

    return respuesta

def aproximacion (objetivo):
    paso = epsilon**2
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        return respuesta

    else:
        return respuesta

def busqueda_binaria (objetivo):
    respuesta = (alto + bajo) /2
    while abs(respuesta**2 - objetivo) >= epsilon:
        
            if respuesta**2 < objetivo:
                bajo = respuesta
            else:
                alto = respuesta
        respuesta = (bajo + alto)/2
    return respuesta
