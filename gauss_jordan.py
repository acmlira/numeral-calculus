from functions import pivoting, identity

def gauss_jordan(A, b, pivoted):
    n = len(A)
    det = 1
    p = 0
    I = identity(n)

    for i in range(0, n):
        if(pivoted):
            (p, A, b) = pivoting(i, A, b) 
            det *= ((-1) ** p)

        det *= A[i][i]

        for j in range (i+1, n):
            m = A[j][i]/A[i][i]
            for k in range(n):
                I[j][k] = I[j][k] - m * A[i][k]
                A[j][k] = A[j][k] - m * A[i][k]
            b[j] = b[j] - m * b[i] 

    for i in range(n-1, -1, -1):
        for j in range (i-1, -1, -1):
            m = A[j][i]/A[i][i]
            for k in range(0, n):
                I[j][k] = I[j][k] - m * A[i][k]
                A[j][k] = A[j][k] - m * A[i][k]
            b[j] = b[j] - m * b[i]

    for i in  range(0, n):
        for j in range(i, n):
            if i == j:
                b[i] = round(b[i]/A[i][j], 2)
                for k in range(0, n):
                    A[i][k] = A[i][k]/A[i][j]
                    I[i][k] = I[i][k]/A[i][j]

    return (A, b, det, p, I)

A = [[  2,  2,  1,  1],
     [  1, -1,  2, -1],
     [  3,  2, -3, -2],
     [  4,  3,  2,  1]]

b =  [  7,  1,  4, 12]

(A, b, det, p, I) = gauss_jordan(A, b, True)

print(A ,"\n\n", b, "\n\n", det)