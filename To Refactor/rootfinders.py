import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import findroots as fr

mpl.rcParams['lines.linewidth'] = 2

f = lambda x: eval(sys.argv[1]) 

a = float(sys.argv[2])
b = float(sys.argv[3])
dx = float(sys.argv[4])

fig, ax = plt.subplots()
plt.xlabel("x")
plt.ylabel("fx")
plt.title("EsboÃ§o da funÃ§Ã£o f(x)")
xRange = np.arange(a, b, 0.01)
fxRange = f(xRange)
ax.set(xlim=(a, b), ylim=(min(fxRange), max(fxRange)))
ax.plot(xRange, fxRange, 'b-', xRange, 0*xRange, 'k-')[0]

intervals = []
while True:
    x1,x2 = fr.findroots(f,a,b,dx)
    if x1 != None:
        a = x2
        intervals.append([x1, x2])
    else:
        break

intervals = np.array(intervals)
vertSize = int(0.15*max(abs(fxRange)))
print(vertSize)
for i in range(intervals.shape[0]):
    ax.plot(vertSize*[intervals[i,0]], np.arange(vertSize)-vertSize/2, 'r-')
    ax.plot(vertSize*[intervals[i,1]], np.arange(vertSize)-vertSize/2, 'r-')
    ax.plot(np.linspace(intervals[i,0], intervals[i,1], num=10), 10*[0], 'r-')

print("Intervalos encontrados:")
print(intervals)
plt.show()