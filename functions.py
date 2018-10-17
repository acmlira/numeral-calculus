def identity(n):
    I = [[0 for y in range(n)]for x in range (n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                I[i][j] = 1
    return I

def pivoting(i, A, b):
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
    return (p, A, b)

def retroactive(A, b):
    n = len(A)
    x = n*[0]
    for i in range(n-1, -1, -1):
        s = sum([A[i][j]*x[j] for j in range(i+1,n)])
        x[i] = (b[i] - s)/A[i][i]
    return x

def successive(A, b):
    n = len(A)
    x = n * [0]
    x[0] = b[0]/A[0][0]
    for i in range (0,n):
        s = 0
        for j in range (0,i):
            s = s + A[i][j] * x[j]
            x[i] = (b[i] - s)/A[i][i]
            
    return x

def standard(v):
    n = len(v)
    s = 0

    for i in range(0, n):
        s += v[i] * v[i]

    return s ** (1/2)

def line_criterion(v, x):
    n = len(x)
    M = 0
    m = 0

    for i in range(0, n):
        if(abs(v[i] - x[i]) > M):
            M = abs(v[i] - x[i])
        if(abs(v[i]) > m):
            m = abs(v[i])

    return M/m

def sassenfeld(B):
    n = len(B)
    M = 0

    for i in range(0, n):
        if(abs(B[i]) > M):
            M = abs(B[i])
    
    return B[i]
    