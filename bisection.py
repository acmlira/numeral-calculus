#
#   Disciplina de Métodos Numéricos (2018.2 UFC)
#
#   Autor: Allan César
#   Data: 24/08/2018
#
#   Algoritmo do Método Numérico: Bisseção 
#
#   Base environment: Anaconda 3 (Python 3.6)
#
#   TAG: Refactor
#
def bisection(str_of_f, a, b, epsilon, k_max = 20):
    f = lambda x: eval(str_of_f)

    # Testa se há mudança de sinal no intervalo 
    if (f(a) * f(b)) > 0:
        return (False, None)

    # Regra de negócio do método e prepara a primeira iteração
    x = (a + b) / 2
    
    # Printa cabeçalho
    print("--------------------------------------------------------------------------------------------------------------------")
    print("k\ta\t\tf(a)\t\tb\t\tf(b)\t\tx\t\tf(x)\t\tintervX")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("-\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (a, f(a), b, f(b), x, f(x), b - a))

    # Testa se o intervalo já está suficientemente próximo ao valor da aproximação
    if abs(b - a) <= epsilon:
        return (True, x)

    # Inicia as iterações
    k = 0
    while k < k_max:
        # Testa se não há mudança de sinal, para a_k+1 = x_k
        if (f(x) * f(a)) > 0:
            a = x
        # Faz o inverso, então, b_k+1 = x_k
        else:
            b = x
        
        # Prepara a próxima iteração
        x = (a + b)/2

        # Linha de debug
        k += 1
        print("%i\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (k, a, f(a), b, f(b), x, f(x), b - a))

        # Testa se o intervalo já está suficientemente próximo ao valor da aproximação
        if abs(b - a) <= epsilon:
            break

    # Finaliza o método
    return(True, x)

# Chama o método    
bisection("(x**3) - 9*x + 3", 0, 1, 0.001)