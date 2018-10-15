#
#   Disciplina de Métodos Numéricos (2018.2 UFC)
#
#   Autor: Allan César
#   Data: 14/10/2018
#
#   Algoritmo do Método Numérico: Eliminação de Gauss 
#
#   Base environment: Anaconda 3 (Python 3.6)
#
#   TAG: To comment 
#
A = [[  1,  2,  3],
     [  3,  1,  0],
     [  0,  3,  4]]

b =  [  3,  4,  3]

def pivot(i, A, b):
    n = len(A)
    p = 0

    for r in range(i, n):
        if abs(A[r][i]) > abs(A[i][i]):
            p += 1
            for t in range(n):
                g       = A[i][t]
                A[i][t] = A[r][t]
                A[r][t] = g
            f    = b[i]
            b[i] = b[r]
            b[r] = f
    return p

def gauss_elimination(A, b, pivoted):
    n = len(A)
    det = 1
    p = 0

    for i in range(0, n):
        det *= A[i][i]

        if(pivoted):
            p = pivot(i, A, b)
            det *= ((-1) ** p)

        for j in range (i+1, n):
            m = A[j][i]/A[i][i]
            for k in range(n):
                A[j][k] = A[j][k] - m * A[i][k]
            b[j] = b[j] - m * b[i]

    x = n*[0]
    for i in range(n-1, -1, -1):
        s = sum([A[i][j]*x[j] for j in range(i+1,n)])
        x[i] = (b[i] - s)/A[i][i]

    return (A, x, det, p)

print(gauss_elimination(A, b, True))