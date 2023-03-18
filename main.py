def jacobi(A, b, max_iter=100, tol=1e-6):
    n = len(b)
    x = [0] * n  # Inicializa o vetor x com zeros
    x_new = [0] * n
    
    for iter in range(max_iter):
        for i in range(n):
            row_sum = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - row_sum) / A[i][i]
            
        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:  # Verifica se a tolerância foi alcançada
            break
        
        x = x_new.copy()  # Atualiza o vetor x

    return x_new

# Exemplo de uso:
A = [[10, -1, 2, 0],
     [-1, 11, -1, 3],
     [2, -1, 10, -1],
     [0, 3, -1, 8]]

b = [6, 25, -11, 15]

x = jacobi(A, b)
print("Solução:", x)
