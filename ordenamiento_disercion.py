import random

def ordenamiento_disercion(lista):
    
    n = len(lista)
    for indice in range(1, n):
        valor_actual = lista[indice]
        posicion = indice
        while valor_actual < lista[posicion-1] and posicion > 0:
                lista[posicion] = lista[posicion-1]
                ##lista[posicion-1] = valor_actual
                posicion -= 1
        lista[posicion] = valor_actual
    return lista


if __name__ == '__main__':
    tamaño_lista = int(input('¿de que tamaño es la lista?'))
    lista = [random.randint(0, 100) for i in range(tamaño_lista)]
    print(lista)
    lista_ordenada = ordenamiento_disercion(lista)
    print(lista_ordenada)