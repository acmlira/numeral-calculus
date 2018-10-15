from functions import identity, successive, retroactive

def lu(A):
    L = identity(len(A))
    n = len(A)
    for i in range(0,n):
        for j in range(i+1,n):
            m = A[j][i]/A[i][i]
            L[j][i] = m
            for k in range(n):
                A[j][k] = A[j][k] - m * A[i][k]
    U = A
    return (L, U)

A = [[  3,  2,  4],
     [  1,  1,  2],
     [  4,  3, -2]]

(L, U) = lu(A)

b =  [  1,  2,  3]

y = successive(L, b)
x = retroactive(U, y)

print(x, y)