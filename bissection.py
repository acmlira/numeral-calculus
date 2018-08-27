from generic import (signal_check, F, E_check, header, debug, mean) 

def bissection(a, b, E, maxIter = 50):

    if signal_check(a, b):
        return Exception
    if E_check(a, b, E):
        return Exception

    x = mean(a, b)

    print(header(a, b, x))

    k = 1
    while k < maxIter:
        if E_check(a, b, E): 
            break
        if signal_check(a, x):
            a = x
        else:
            b = x

        x = mean(a, b)

        print(debug(k, a, b, x))

        k += 1
    return x