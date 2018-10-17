from functions import pivoting, retroactive
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
A = [[  2,  2,  1,  1],
     [  1, -1,  2, -1],
     [  3,  2, -3, -2],
     [  4,  3,  2,  1]]

b =  [  7,  1,  4, 12]

def gauss_elimination(A, b, pivoted):
    n = len(A)
    det = 1
    p = 0

    for i in range(0, n):
        if(pivoted):
            (p, A, b) = pivoting(i, A, b)
            det *= ((-1) ** p)

        det *= A[i][i]

        for j in range (i+1, n):
            m = A[j][i]/A[i][i]
            for k in range(n):
                A[j][k] = round(A[j][k] - m * A[i][k], 3)
            b[j] = round(b[j] - m * b[i], 2)

    x = retroactive(A, b)
    return (A, x, b, det, p)

(A, x, b, det, p) = gauss_elimination(A, b, False)

print(x)