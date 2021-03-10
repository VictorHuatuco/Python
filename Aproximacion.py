objetivo = int(input('Escoja un numero'))
epsilon = 0.001
paso = epsilon**2
respuesta = 0.0
cuenta = 0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raiz cuadrada')
else:
    print(f'La raiz cuadra de {objetivo} es {respuesta}')
  