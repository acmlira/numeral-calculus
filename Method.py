from Plotter import Plotter

class Method:
    def __init__(self, function, a, b, E, maxIter = 20):
        self.function = function
        self.a = a
        self.b = b
        self.E = E
        self.maxIter = maxIter
        self.x = 0
        self.plot = Plotter(self)

    def f(self, x): 
        return eval(self.function)

    def signal_is_valid(self, a, b):
        if((self.f(a) * self.f(b)) < 0):
            return True
        return False
    
    def E_is_valid(self):
        if((self.b - self.a) < self.E):
            return False
        return True

    def x_is_equal_to_root(self):
        if (self.f(self.a) <= 0 + self.E and self.f(self.a) >= 0 - self.E):
            return True
        if (self.f(self.b) <= 0 + self.E and self.f(self.b) >= 0 - self.E):
            return True
        return False
    
    def print_debug(self, k):
        print("%i\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (k, self.a, self.f(self.a), self.b, self.f(self.b), self.x, self.f(self.x), (self.b - self.a)))

    def print_header(self):
        print("k\ta\t\tFa\t\tb\t\tFb\t\tx\t\tFx\t\t\tAproximação\n-\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (self.a, self.f(self.a), self.b, self.f(self.b), self.x, self.f(self.x), (self.b - self.a)))

    def apply_method(self):
        return True

    def business_rule(self):
        return True

    def plot_debug(self):
        self.plot.function()