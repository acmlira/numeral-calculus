from Bissection import Bissection
from FalsePosition import FalsePosition

interval = FalsePosition(("(x**3) - (9*x) + 3"), 0, 1, 0.005, 20)
print(interval.false_position())