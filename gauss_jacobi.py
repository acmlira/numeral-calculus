from functions import line_criterion, standard

def gauss_jacobi(A, b, x, epsilon = 0.001, k_max = 50):

    n = len(A)
    v = [0 for y in range(n)]

    k = 0
    while k < k_max:
        for i in range(0, n):
            s = 0
            for j in range(0, n):
                if i != j:
                    s += A[i][j] * x[j]
            v[i] = (b[i] - s)/A[i][i]

        # Faltando o critério de parada
        # d = line_criterion(v, x)
        # print(d)
        # if d <= epsilon:
        #      return v
       
        x = v
        k += 1
        print(k, " - ", v)
    return v

A = [[ 10,  2,  1],
     [  1,  5,  1],
     [  2,  3, 10]]

b =  [  7, -8,  6]

x =  [0.7,-1.6,0.6]

epsilon = 0.05

k_max = 4

gauss_jacobi(A, b, x, epsilon, k_max)