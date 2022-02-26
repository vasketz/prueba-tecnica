#!/usr/bin/env python3

"""
programa para imprimir si es numero perfecto o no 
"""

"""se importa argv para capturar los argumentos pasados por consola"""
from sys import argv

"""guardian para ejecutar el script sin problemas de enviroment variables"""
if __name__ == "__main__":
    """se inicializan las variables"""
    n = int(argv[1])
    i = int(2)
    p = int(0)

    """ciclo para dar con el numero dado emepzando desde 2"""
    while (i <= n):
        """se saca el resido o modulo del numero dado dividiendo el numero dado por el incremente que sea igual a 0"""
        if (n % i == 0):
            """evaluamos si la suma del numero perfecto es igual al numero dado"""
            p = p + (n/i)
        """incrementamos"""
        i = i + 1

    """si el numero dado es igual al numero perfecto imprime es perfecto de lo contrario no es perfecto"""
    if(n == p):
        print("{} Es perfecto".format(n))
    else:
        print("{} No es perfecto".format(n))
