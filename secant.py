#
#   Disciplina de Métodos Numéricos (2018.2 UFC)
#
#   Autor: Allan César
#   Data: 12/09/2018
#
#   Algoritmo do Método Numérico: Secante
#
#   Base environment: Anaconda 3 (Python 3.6)
#
def secant(str_of_f, x0, x1, epsilon, iterMax=100):
    f = lambda x: eval(str_of_f)

    if abs(f(x0)) <= epsilon:                   # Teste para saber se x0 já é a raiz (usa abs para conter os valores negativos)
        return (False, x0)                      # Retorna uma tupla com False (por que o método falhou) e com a raiz
    if abs(f(x1)) <= epsilon:                   # Teste para saber se x0 já é a raiz (usa abs para conter os valores negativos)
        return (False, x1)

    x2 = x1 - (f(x1)/((f(x1) - f(x0)) / (x1 - x0)))
    print("--------------------------------------------------------------------------------------------------------------------")
    print("k\tx2\t\tf(x2)")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("-\t%e\t%e-" % (x2, f(x2)))
    
    k = 0                                       # Inicia as iterações                                       

    while k < iterMax:                          # Loop condicionado

        k += 1
        x2 = x1 - (f(x1)/((f(x1) - f(x0)) / (x1 - x0)))
        print("%i\t%e\t%e" % (k, x2, f(x2)))
        if abs(f(x2)) <= epsilon:
            return (True, x2)
        x0 = x1
        x1 = x2
    return (False, x0) 

print(secant("(x**2) + x - 6",1.5,1.7,0.001))