from Bissection import bissection
from FalsePosition import false_position
import matplotlib.pyplot as plt
import numpy as np

# false_position(("(x**2) - 1"), 0.5, 1.5, 0.005, 20)

def f(function): 
    return eval(function)

x = np.arange(-10, 10, 0.00001)

plt.plot(x ,f("- x - 1"), '-')
plt.grid(True)
plt.show()