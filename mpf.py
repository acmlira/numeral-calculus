#
#   Disciplina de Métodos Numéricos (2018.2 UFC)
#
#   Autor: Allan César
#   Data: 12/09/2018
#
#   Algoritmo do Método Numérico: Método da Posição Fixa
#
#   Base environment: Anaconda 3 (Python 3.6)
#
def mpf(str_of_f, str_of_fi, x0, epsilon, iterMax=20):
    f = lambda x: eval(str_of_f)
    fi = lambda x: eval(str_of_fi)
    
    # Testa x0 para saber se já é a raiz desejada
    if abs(f(x0)) <= epsilon:           
        return (False, x0)              

    # Mostra cabeçalho de iterações
    print("--------------------------------------------------------------------------------------------------------------------")
    print("k\tx1\t\tf(x1)\t\tfi(x1)")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("-\t%e\t%e\t%e" % (x0, f(x0), fi(x0)))

    # Começa as iterações
    k = 0
    while k < iterMax:
        k += 1
        x1 = fi(x0)

        # Printa linha de debug
        print("%i\t%e\t%e\t%e" % (k, x1, f(x1), fi(x1)))

        # Testa se meu novo x já será a raiz desejada
        if abs(f(x1)) <= epsilon:
            return (True, x1)

        # Prepara a próxima iteração
        x0 = x1

    # Se chegou no número máximo de iterações encerra o método e retorna um erro (False)
    return (False, x0)

mpf("(x**2) + x - 6","(6 - x)**(1/2)",1.5,0.00000001)