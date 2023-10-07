from itertools import combinations
from collections import Counter

# Números disponíveis
numeros_disponiveis = [2, 3, 5, 7, 8, 10, 13, 14, 15, 16, 17, 18, 19, 22, 25]

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 7 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 7 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_7 = list(combinations(numeros, 7))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_7)

# Encontra o grupo de 7 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 7 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")
