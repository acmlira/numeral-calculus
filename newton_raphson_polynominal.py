#
#   Disciplina de Métodos Numéricos (2018.2 UFC)
#
#   Autor: Allan César
#   Data: 24/08/2018
#
#   Algoritmo do Método Numérico: Newton-Raphson
#
#   Base environment: Anaconda 3 (Python 3.6)
#
#   Obs: Calcula f(x)/f'(x) através do método de Horner
#
def newton_raphson_polynominal(n, a, x, epsilon, iterMax=20):      
    n = len(a)-1
    print("k\t x\t\t p(x)")
    k = 0
    
    while k <= iterMax:    
        b = [1.0] * len(a)
        c = [1.0] * n

        i = n - 1
        while i != 0:
            b[i] = a[i] + b[i+1]*x
            c[i-1] = b[i] + c[i]*x
            i -= 1

        b[0] = a[0] + b[1]*x
   
        print("%d\t %e\t %e\t" %(k, x, b[0]))

        if abs(b[0]) <= epsilon:
            return(False, x)
        if abs(c[0]) == 0 :
            
            return (True, None)
        
        x = x - b[0]/c[0]
        k += 1

    return(True, x)