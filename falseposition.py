from generic import (secant_line, signal_check, F, E_check, root_check, header, debug) 

def falseposition(a, b, E, maxIter = 50):

    if signal_check(a, b):
        return Exception
    if E_check(a, b, E):
        return Exception
    if root_check(a, b):
        return Exception

    x = secant_line(a, b)

    print(header(a, b, x))

    k = 1
    while k < maxIter:
        if E_check(a, b, E): 
            break
        if root_check(a, x):
            break
        else:
            if signal_check(a, x):
                a = x
            else:
                b = x

        x = secant_line(a, b)
    
        print(debug(k, a, b, x))

        k += 1
    return x