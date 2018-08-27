from __future__ import division

def debug(k, a, b, x):
    return ("%i\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (k, a, F(a), b, F(b), x, F(x), (b - a)))

def header(a, b, x):
    return ("k\ta\t\tFa\t\tb\t\tFb\t\tx\t\tFx\t\t\tAproximação\n-\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (a, F(a), b, F(b), x, F(x), (b - a)))

def signal_check(a, b):
    if(F(a) * F(b) < 0):
        return False
    return True

def E_check(a, b, E):
    if((b - a) < E):
        return True
    return False

def root_check(a, b):
    if F(a) == 0:
        return True
    if F(b) == 0:
        return True
    return False

def mean(a, b):
    return (a + b)/2

def secant_line(a, b):
    return ((a*F(b)) - (b*F(a)))/(F(b) - F(a))

def F(x):
    return eval("(x**3) - (9*x) + 3") 