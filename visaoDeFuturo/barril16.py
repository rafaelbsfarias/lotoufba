import itertools

# Função para gerar todas as combinações de 14 números a partir de uma lista de 15
def generate_combinations(numbers):
    combinations = list(itertools.combinations(numbers, 14))
    return combinations

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa uma lista para armazenar os números presentes nos resultados anteriores
numeros_presentes = []

# Extrai os números das linhas e os adiciona à lista de números presentes
for linha in linhas:
    numeros_linha = linha.strip().split(',')
    numeros_presentes.extend(map(int, numeros_linha))

# Todos os números possíveis
todos_numeros = list(range(1, 26))

# Remove os números já presentes nos resultados anteriores
numeros_disponiveis = [numero for numero in todos_numeros if numero not in numeros_presentes]

# Gera todas as combinações de 14 números a partir dos números disponíveis
combinacoes_14 = generate_combinations(numeros_disponiveis)

# Verifica se todas as combinações possíveis de 14 números já foram sorteadas
if not combinacoes_14:
    print("Todas as combinações possíveis de 14 números já foram sorteadas.")
else:
    # Exibe as combinações de 14 números
    for i, combinacao in enumerate(combinacoes_14, start=1):
        print(f"Combinação {i} de 14 números:")
        print(combinacao)

    # Verifica se é possível gerar alguma sequência de 15 números
    if len(combinacoes_14) == 0:
        print("Nenhuma combinação pode ser gerada para formar sequências de 15 números.")
