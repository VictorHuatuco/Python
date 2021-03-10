def operacion(x, y):
    """Suma los valores de dos valores.

    Recordemos que x & y son parametros
    y que 5 y 17 son argumentos. 
    No, no son lo mismo. 
    Los parametros son los que se ponen
    al definir (def) la funcion.
    En cambio los argumentos son el
    numero, nombre, o dato que va a
    suplir al parametro en la operacion a 
    la hora de imprimir.

    Parametros:
    x recibe un numero entero
    y recibe un numero entero
    
    Que regresa? #Resultado pues
    returns el valor de x mas y
    """
    return x + y

print("\n") #La \n da un salto de linea al imprimir
print(operacion(5, 17))
print("\n") #La \n sirve para separar 'prints'
print(operacion.__doc__) 
help(operacion) 