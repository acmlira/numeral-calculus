import numpy as np
import matplotlib.pyplot as plt
import Method

class Plotter:
    def __init__(self, Method):
        self.Method = Method
        self.a_max = Method.a
        self.b_max = Method.b

    def function(self):
        x = np.arange(self.a_max, self.b_max, 0.00001)
        
        plt.plot(x, self.Method.f(x), '-')

        plt.plot(self.Method.a, 0, 'bo', color="black")
        plt.annotate('a', xy=(self.Method.a, 0), xytext=(self.Method.a + 0.02, 0))
        plt.plot(self.Method.b, 0, 'bo', color="black")
        plt.annotate('b', xy=(self.Method.b, 0), xytext=(self.Method.b + 0.02, 0))
        plt.plot(self.Method.business_rule(), 0, 'bo', color="red")
        plt.annotate('x', xy=(self.Method.business_rule(), 0), xytext=(self.Method.business_rule() - 0.04, 0))

        plt.grid(True)
        plt.show()

    def function_with_secant_line(self):
        x = np.arange(self.a_max, self.b_max, 0.00001)
        
        x_0 = self.Method.business_rule()
        a = self.Method.a
        b = self.Method.b
        Fa = self.Method.f(a)
        Fb = self.Method.f(b)

        plt.plot(x, self.Method.f(x), '-')

        #plt.plot([self.Method.a, 0], [self.Method.a, self.Method.f(self.Method.a)], '-', color="black")

        plt.plot([a, a], [Fa, 0], '--', color="black")
        plt.plot([b, b], [Fb, 0], '--', color="black")
        plt.plot([a, b], [Fa, Fb], '-', color="red", linewidth=1)

        plt.plot(a, 0, 'bo', color="black")
        plt.annotate('a', xy=(a, 0), xytext=(a + 0.02, 0))
        plt.plot(b, 0, 'bo', color="black")
        plt.annotate('b', xy=(b, 0), xytext=(b + 0.02, 0))
        plt.plot(x_0, 0, 'bo', color="red")
        plt.annotate('x', xy=(x_0, 0), xytext=(x_0 - 0.04, 0))

        plt.grid(True)
        plt.show()