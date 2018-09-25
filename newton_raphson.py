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
def newton_raphson(str_of_f, str_of_flin, x0, epsilon, iterMax=20):  
    f = lambda x: eval(str_of_f)
    flin = lambda x: eval(str_of_flin)
    
    
    if abs(f(x0)) <= epsilon:                   # Teste para saber se x0 já é a raiz (usa abs para conter os valores negativos)
        return (False, x0)                      # Retorna uma tupla com False (por que o método falhou) e com a raiz
    
    print("--------------------------------------------------------------------------------------------------------------------")
    print("k\tx1\t\tf(x1)\t\tflin(x1)")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("-\t%e\t%e\t%e\t-" % (x0, f(x0), flin(x0)))
    
    k = 0                                       # Inicia as iterações                                       

    while k < iterMax:                          # Loop condicionado
        k += 1
        x1 = x0 - (f(x0)/flin(x0))
        print("%i\t%e\t%e\t%e" % (k, x1, f(x1), flin(x1)))
        if abs(f(x1)) <= epsilon:
            return (True, x1)
        x0 = x1
        
    return (False, x0) 

print(newton_raphson("(x**2) + x - 6","2*x + 1",1.5,0.001))