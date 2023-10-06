import itertools

# Função para ler as combinações dos resultados anteriores
def ler_combinacoes_resultados_antigos(arquivo):
    combinacoes_antigas = set()
    with open(arquivo, 'r') as arquivo_resultados:
        linhas = arquivo_resultados.readlines()
        for linha in linhas:
            numeros = list(map(int, linha.strip().split(',')))
            for combinacao in itertools.combinations(numeros, 11):
                combinacoes_antigas.add(tuple(sorted(combinacao)))  # Garante que as combinações estejam ordenadas
    return combinacoes_antigas

# Gere todas as combinações possíveis de 11 números
todas_combinacoes = set(itertools.combinations(range(1, 26), 11))

# Leitura das combinações dos resultados anteriores
combinacoes_antigas = ler_combinacoes_resultados_antigos('resultadosAnteriores.txt')

# Encontre as combinações ausentes
comb_ausentes = todas_combinacoes - combinacoes_antigas

# Se houver combinações ausentes, salve-as em um arquivo
if comb_ausentes:
    with open('comb_ausentes.txt', 'w') as arquivo_comb_ausentes:
        for combinacao in comb_ausentes:
            arquivo_comb_ausentes.write(','.join(map(str, combinacao)) + '\n')
    print("Arquivo comb_ausentes.txt criado com as combinações de 11 números ausentes nos resultados anteriores.")
else:
    print("Não há combinações de 11 números ausentes nos resultados anteriores.")
