#
#   Disciplina de Métodos Numéricos (2018.2 UFC)
#
#   Autor: Allan César
#   Data: 12/09/2018
#
#   Algoritmo do Método Numérico: Método da Posição Fixa
#
#   Base environment: Anaconda 3 (Python 3.6)
def mpf(fi, x0, E, iterMax=100):
    if(abs(fi(x0)) < E):
        return Exception
    k = 1
    print("x aprox\t\t\tf\t\t\tf'\t\t\tk")
    while k < iterMax:

        x1 = fi(x0)
        k += 1
        
        print("%e\t\t%e\t\t%e\t\t" % (x1,  fi(x1), k))
        
        if (abs(fi(x1)) < E):
            break 
            
        x0 = x1
        
        
        if (k == iterMax):
            return Exception
    return x0