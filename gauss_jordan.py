from functions import pivot, identity

def gauss_jordan(A, b, pivoted):
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

    for i in range(n-1, -1, -1):
        for j in range (i-1, -1, -1):
            m = A[j][i]/A[i][i]
            for k in range(0, n):
                A[j][k] = A[j][k] - m * A[i][k]
            b[j] = b[j] - m * b[i]

    for i in  range(0, n):
        for j in range(i, n):
            if i == j:
                b[i] = round(b[i]/A[i][j], 2)
                for k in range(0, n):
                    A[i][k] = round(A[i][k]/A[i][j], 2)

    return (A, b, det, p)

A = [[  3,  2,  4],
     [  1,  1,  2],
     [  4,  3, -2]]

b =  [  1,  2,  3]

print(gauss_jordan(A, b, True))