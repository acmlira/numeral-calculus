#
#   Disciplina de Métodos Numéricos (2018.2 UFC)
#
#   Autor: Allan César
#   Data: 24/08/2018
#
#   Algoritmo do Método Numérico: Newton-Raphson
#
#   Base environment: Anaconda 3 (Python 3.6)
def newton(f, flin, x0, E, iterMax=100):
    if(abs(f(x0)) < E):
        return Exception
    k = 1
    print("x aprox\t\t\tf\t\t\tf'\t\t\tk")
    while k < iterMax:

        x1 = x0 - (f(x0)/flin(x0))
        k += 1
        
        print("%e\t\t%e\t\t%e\t\t%e" % (x1,  f(x1), flin(x1), k))
        
        if (abs(f(x1)) < E):
            break 
            
        x0 = x1
        
        
        if (k == iterMax):
            return Exception
    return x0