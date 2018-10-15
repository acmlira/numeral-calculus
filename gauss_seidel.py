from functions import line_criterion, standard

def gauss_seidel(A, b, x, epsilon = 0.001, k_max = 50):

    n = len(A)
    v = [0 for y in range(n)]

    k = 0
    while k < k_max:
        for i in range(0, n):
            s = 0
            for j in range(0, n):
                if i != j:
                    s += A[i][j] * x[j]
            v[i] = x[i]
            x[i] = (b[i] - s)/A[i][i]

        # Faltando o critério de parada
        # d = line_criterion(v, x)
        # print(d)
        # if d <= epsilon:
        #      return v
       
        x = v
        k += 1
        print(k, " - ", v)
    return v

A = [[  5,  1,  1],
     [  3,  4,  1],
     [  3,  3,  6]]

b =  [  5,  6,  0]

x =  [  0,  0,  0]

epsilon = 0.05

k_max = 4

gauss_seidel(A, b, x, epsilon, k_max)