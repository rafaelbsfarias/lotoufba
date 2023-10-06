from itertools import combinations
from collections import Counter

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 11 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 11 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_11 = list(combinations(numeros, 11))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_11)

# Encontra os 10 grupos de 11 números mais frequentes
grupos_mais_frequentes = contador_grupos.most_common(10)

# Exiba os 10 grupos mais frequentes
for i, (grupo, frequencia) in enumerate(grupos_mais_frequentes, 1):
    print(f"Grupo {i}: {grupo} - Frequência: {frequencia} vezes")
