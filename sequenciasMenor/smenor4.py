from itertools import combinations
from collections import Counter

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 4 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 4 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_4 = list(combinations(numeros, 4))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_4)

# Encontra todos os grupos de 4 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 4 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")
