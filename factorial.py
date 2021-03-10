
def factorial(n):
    """ Calcula el factorial de n.

    n int>0
    returnn!
    """
    if n==1:
        return 1
    return n * factorial(n-1)

n = int(input('Escriba un entero:  '))
print (factorial(n))
