from functions import pivot, retroativas
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
A = [[  3,  2,  4],
     [  1,  1,  2],
     [  4,  3, -2]]

b =  [  1,  2,  3]

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
                A[j][k] = round(A[j][k] - m * A[i][k], 3)
            b[j] = round(b[j] - m * b[i], 2)

    x = retroativas(A, b)
    return (A, x, b, det, p)

print(gauss_elimination(A, b, True))