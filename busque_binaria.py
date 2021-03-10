import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final -1]}')
    if objetivo > final:
        return False

    medio = (comienzo + final)//2
    
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1 , objetivo)

if __name__ == '__main__':
    tamaño_lista = int(input('¿de que tamaño es la lista?'))
    objetivo = int(input('¿que numero busca?'))
    lista = sorted([random.randint(0, 100) for i in range(tamaño_lista)])
    encontrado = busqueda_binaria(lista, 0, len(lista),objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')