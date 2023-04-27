num = int(input("Digite um número inteiro: "))

# Inicializa as duas primeiras posições da sequência
fibonacci = [0, 1]

# Gera a sequência de Fibonacci até o número digitado
while fibonacci[-1] < num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Verifica se o número está na sequência
if num in fibonacci:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")
