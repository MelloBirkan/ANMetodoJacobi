# Função que implementa o método de Jacobi para resolver sistemas lineares
def jacobi(A, b, max_iter=100, tol=1e-6):
    n = len(b)  # Número de equações (e variáveis) no sistema
    x = [0] * n  # Inicializa o vetor x com zeros
    x_new = [0] * n  # Inicializa o vetor x_new com zeros

    # Itera até atingir o número máximo de iterações
    for iter in range(max_iter):
        # Atualiza o vetor x_new com base no vetor x atual
        for i in range(n):
            # Calcula a soma dos produtos A[i][j] * x[j] para j diferente de i
            row_sum = sum(A[i][j] * x[j] for j in range(n) if j != i)
            # Atualiza o valor de x_new[i] usando a fórmula do método de Jacobi
            x_new[i] = (b[i] - row_sum) / A[i][i]

        # Verifica se a diferença máxima entre os elementos de x e x_new é menor que a tolerância
        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            break  # Se a tolerância foi alcançada, interrompe o loop

        x = x_new.copy()  # Atualiza o vetor x com os novos valores de x_new

    return x_new  # Retorna o vetor x_new como a solução aproximada do sistema

# Exemplo de uso visto em aula:
A = [[10, -1, 2, 0],
     [-1, 11, -1, 3],
     [2, -1, 10, -1],
     [0, 3, -1, 8]]
# Termos independentes
b = [6, 25, -11, 15]

x = jacobi(A, b)
print("Solução:", x)
