#
#   Disciplina de Métodos Numéricos (2018.2 UFC)
#
#   Autor: Allan César
#   Data: 12/09/2018
#
#   Algoritmo do Método Numérico: Posição Falsa
#
#   Base environment: Anaconda 3 (Python 3.6)
def false_position(str_of_f, a, b, epsilon, k_max = 20):
    f = lambda x: eval(str_of_f)

    if (f(a) * f(b)) > 0:
        return (False, None)

    x = (a*f(b) - b*f(a)) / (f(b) - f(a))
    
    print("--------------------------------------------------------------------------------------------------------------------")
    print("k\ta\t\tf(a)\t\tb\t\tf(b)\t\tx\t\tf(x)\t\tintervX")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("-\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (a, f(a), b, f(b), x, f(x), b - a))

    if (b - a) < epsilon:
        return (True, x)
    if f(x) <= epsilon and f(x) >= - epsilon:
        return (True, x)

    k = 0
    while k < k_max:
        if f(x) <= epsilon and f(x) >= - epsilon:
            break
        else:
            if (f(x) * f(a)) > 0:
                a = x
            else:
                b = x
        
        x = (a*f(b) - b*f(a)) / (f(b) - f(a))

        k += 1
        print("%i\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (k, a, f(a), b, f(b), x, f(x), b - a))

        if (b - a) < epsilon:
            break

    print("--------------------------------------------------------------------------------------------------------------------")
    return(True, x)
    
false_position("(x**3) - 9*x + 3", 0, 1, 0.001)