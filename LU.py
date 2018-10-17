from functions import identity, successive, retroactive, pivoting

def lu(A, b, pivoted):
    L = identity(len(A))
    n = len(A)
    det = 1
    

    for i in range(0,n):
        if(pivoted):
            (p, A, b) = pivoting(i, A, b) 
            det *= ((-1) ** p)

        det *= A[i][i]
        for j in range(i+1,n):
            m = A[j][i]/A[i][i]
            L[j][i] = m
            for k in range(n):
                A[j][k] = A[j][k] - m * A[i][k]
    U = A
    return (L, U)

A = [[  3, -4,  1],
     [  1,  2,  2],
     [  4,  0, -3]]

b =  [  9,  3, -2]

(L, U) = lu(A, b, True)

y = successive(L, b)
x = retroactive(U, y)

print(x, "\n\n", L, "\n\n", U)