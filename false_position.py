#
#   Disciplina de Métodos Numéricos (2018.2 UFC)
#
#   Autor: Allan César
#   Data: 12/09/2018
#
#   Algoritmo do Método Numérico: Posição Falsa
#
#   Base environment: Anaconda 3 (Python 3.6)
#
#   TAG: Refactor
#
def false_position(str_of_f, a, b, epsilon, k_max = 20):
    f = lambda x: eval(str_of_f)

    # Testa se há mudança de sinal no intervalo
    if (f(a) * f(b)) > 0:
        return (False, None)

    # Prepara a primeira iteração por meio de uma reta secante
    x = (a*f(b) - b*f(a)) / (f(b) - f(a))
    
    print("--------------------------------------------------------------------------------------------------------------------")
    print("k\ta\t\tf(a)\t\tb\t\tf(b)\t\tx\t\tf(x)\t\tintervX")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("-\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (a, f(a), b, f(b), x, f(x), b - a))

    # Testa se o intervalo é suficientemente pequeno a ponto de ser menor do que epsilon
    if abs(b - a) <= epsilon:
        return (True, x)
    # Testa se x já é a raiz 
    if abs(f(x)) <= epsilon:
        return (True, x)

    # Começa as iterações
    k = 0
    while k < k_max:
        # Testa se a x é a raiz desejada
        if abs(f(x)) <= epsilon:
            break
        else:
            # Testa se não há mudança de sinal, para a_k+1 = x_k
            if (f(x) * f(a)) > 0:
                a = x
            # Faz o inverso, então, b_k+1 = x_k
            else:
                b = x
        
        # Prepara a próxima iteração
        x = (a*f(b) - b*f(a)) / (f(b) - f(a))

        # Printa uma linha de debug
        k += 1
        print("%i\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (k, a, f(a), b, f(b), x, f(x), b - a))

        # Testa se o intervalo já está suficientemente próximo ao valor da aproximação
        if abs(b - a) <= epsilon:
            break
    
    # Finaliza o método  
    print("--------------------------------------------------------------------------------------------------------------------")
    return(True, x)

# Chama o método      
false_position("(x**3) - 9*x + 3", 0, 1, 0.001)