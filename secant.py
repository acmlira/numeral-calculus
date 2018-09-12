#
#   Disciplina de Métodos Numéricos (2018.2 UFC)
#
#   Autor: Allan César
#   Data: 12/09/2018
#
#   Algoritmo do Método Numérico: Secante
#
#   Base environment: Anaconda 3 (Python 3.6)
def secante(f, x0, x1, E, iterMax=100):
    if(abs(f(x0)) < E):
        return Exception
    k = 1
    print("x aprox\t\t\tf\t\t\tf'\t\t\tk")
    while k < iterMax:
        d = (f(x1) - f(x0)) / (x1 - x0)
        
        x2 = x1 - (f(x1)/d)
        k += 1
        
        print("%e\t\t%e\t\t%e\t\t%e" % (x1,  f(x1), d, k))
        
        if (abs(f(x2)) < E):
            break 
            
        x0 = x1
        x1 = x2
        
        if (k == iterMax):
            return Exception
    return x1