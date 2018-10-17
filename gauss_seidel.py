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

        print(k, " - ", x)
        # Faltando o critério de parada
        d = line_criterion(x, v)
        # print(d)
        if d <= epsilon:
             return x


        # x = v
        k += 1
    return v


A = [[  4, -1,  0,  0],
     [ -1,  4, -1,  0],
     [  0, -1,  4, -1],
     [  0,  0, -1,  4]]

b =  [  1,  1,  1,  1]

x =  [  0,  0,  0,  0]

epsilon = 0.001

k_max = 20
gauss_seidel(A, b, x, epsilon, k_max)