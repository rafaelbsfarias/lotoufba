import time

# Registra o tempo de início
inicio = time.time()

from itertools import combinations
from collections import Counter

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Itera de 1 a 15 dezenas
for n in range(1, 16):
    # Inicializa um contador para os grupos de n números
    contador_grupos = Counter()

    # Para cada linha, gera todas as combinações de n números
    for linha in linhas:
        numeros = [int(numero) for numero in linha.strip().split(',')]
        grupos_de_n = list(combinations(numeros, n))

        # Atualiza o contador com os grupos gerados
        contador_grupos.update(grupos_de_n)

    # Ordena as combinações em ordem decrescente de ocorrência
    comb_ordenadas = contador_grupos.most_common()

    # Calcula o número total de resultados anteriores
    total_resultados = len(linhas)

    # Salva o resultado em um arquivo com nome incremental
    nome_arquivo = f'ocorrenciasDe{n}.txt'
    with open(nome_arquivo, 'w') as resultado:
        resultado.write(f"Combinações de {n} dezenas com ocorrência e percentual:\n")
        for comb, ocorrencia in comb_ordenadas:
            percentual = (ocorrencia / total_resultados) * 100
            resultado.write(f"Combinação {', '.join(map(str, comb))}: {ocorrencia} vezes ({percentual:.2f}%)\n")

    print(f"O resultado foi salvo em {nome_arquivo}.")

# Registra o tempo de término
fim = time.time()

# Calcula o tempo decorrido
tempo_decorrido = fim - inicio

print(f"Tempo de execução: {tempo_decorrido:.2f} segundos")