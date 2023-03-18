import time
from tabulate import tabulate

def jacobi(A, b, max_iter=1000, tol=1e-6, print_time=False):
    ini = time.time()
    n = len(b)  # Número de equações (e variáveis) no sistema
    x = [0] * n  # Inicializa o vetor x com zeros
    x_new = [0] * n  # Inicializa o vetor x_new com zeros

    # Verifica se há elementos da diagonal principal igual a zero
    if any(A[i][i] == 0 for i in range(n)):
        return"Elemento da diagonal principal é igual a zero"

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
    
    fim=time.time()
    if(print_time):
      return f"{round(fim-ini, 6)} segundos"
    return x_new  # Retorna o vetor x_new como a solução aproximada do sistema


def resolver3(eq, ti, tole = 0.1, print_time=False):
    resultados = []

    for i in range(0, 3):
        ini = time.time()
        r3 = jacobi(eq, ti, 100, tole)
        tole /= 10
        fim = time.time()

        if print_time:
            tole_print = tole * 10
            resultados.append([tole_print, round(fim - ini, 6), r3])
        else:
            print(r3)

    if print_time:
        headers = ["Tolerância", "Tempo (segundos)", "Resultado"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
  
# Exercicio 1 (
  
# Exemplo de uso visto em aula:
A = [[10, -1, 2, 0],
     [-1, 11, -1, 3],
     [2, -1, 10, -1],
     [0, 3, -1, 8]]

# Termos independentes
TIA = [6, 25, -11, 15]
rA = jacobi(A, TIA)
print("Exercicio 1:\n")
print(f"Solução: {rA}\n\n")
#)

# Exercicio 2 (
print("Exercicio 2:")
print('''
3x1 - 0.1x2 - 0.2x3 = 7.85
0.1x1 + 7x2 - 0.3x3 = -19.3
0.3x1 - 0.2x2 + 10x3 = 71.4
''')
# Exemplo com 3 equações
A2 = [[3, -0.1, -0.2],
  [0.1, 7, -0.3],
  [0.3, -0.2, 10]]
# Termos independentes
b2 = [7.85, -19.3, 71.4]
rB = jacobi(A2, b2, max_iter=10, tol=0.1)
print("Solução aproximada:", rB)
#)

 # Exercicio 3 (
print("\n\nExercicio 3")
a = [[1, -1, 3], [3, -3, 1], [1, 1, 0]]
at = [2, -1, 3]
print("\nA)", end=" ")
rB = jacobi(a, at, max_iter=10, tol=0.1)
print("Solução aproximada:", rB)
resolver3(a, at) 

b = [[2, -1.5, 3], [-1, 0, 2], [4, -4.5, 5]]
bt = [1, 3, 1]
print("\nB)", end=" ")
resolver3(b, bt) 

c = [[2, 0, 0, 0], [1, 1.5, 0, 0], [0, -3, 0.5, 0], [2, -2, 1, 1]]
ct = [3, 4.5, -6.6, 0.8]
print("\nC)", end=" ")
resolver3(c, ct) 

d = [[1, 1, 0, 1], [2, 1, -1, 1], [4, -1, -2, 2], [3, -1, -1, 2]]
dt = [2, 1, 0, -3]
print("\nD)", end=" ")
resolver3(d, dt) 

# Exercicio 4 (
print("\n\nExercicio 4\n")
rA = jacobi(A, TIA, print_time = True)
print(f"Tempo exercicio 1: {rA}")
rB = jacobi(A2, b2, print_time=True)
print(f"Tempo exercicio 2: {rB}")
#)

# Exercicio 5 (
print("\n\nExercicio 5\n")
print("\nA)", end=" ")
resolver3(a, at, print_time = True) 
print("\nB)", end=" ")
resolver3(b, bt, print_time = True) 
print("\nC)", end=" ")
resolver3(c, ct, print_time = True) 
print("\nD)", end=" ")
resolver3(d, dt, print_time = True) 
#)