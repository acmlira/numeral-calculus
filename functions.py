def identity(n):
    I = [[0 for y in range(n)]for x in range (n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                I[i][j] = 1
    return I

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

def retroativas(A, b):
    n = len(A)
    x = n*[0]
    for i in range(n-1, -1, -1):
        s = sum([A[i][j]*x[j] for j in range(i+1,n)])
        x[i] = (b[i] - s)/A[i][i]
    return x