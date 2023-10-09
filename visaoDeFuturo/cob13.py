import itertools

# Função para gerar combinações de 16 números a partir de uma combinação de 13
def gerar_combinacoes_de_16(comb_13):
    numeros_faltantes = list(set(range(1, 26)) - set(comb_13))
    combinacoes_de_16 = itertools.combinations(comb_13 + tuple(sorted(numeros_faltantes)), 16)
    return combinacoes_de_16

print("Carregando arquivos...")
# Ler as combinações de 13 números do arquivo 13ausentes.txt
with open('13ausentes.txt', 'r') as arquivo_13ausentes:
    linhas = arquivo_13ausentes.readlines()

# Ler todas as combinações de 16 números do arquivo todasCombinações16.txt
with open('todasCombinações16.txt', 'r') as arquivo_todas_combinacoes:
    todas_combinacoes_16 = [tuple(map(int, linha.strip().split(','))) for linha in arquivo_todas_combinacoes.readlines()]

print("Arquivos carregados com sucesso.")
print("Iniciando cobertura das combinações de 13 números...")

# Inicializar um conjunto para rastrear as combinações de 16 números selecionadas
combinacoes_16_selecionadas = set()
cobertura_comb_13 = set()

# Ordenar as combinações de 13 números para otimizar a busca
linhas = [tuple(sorted(map(int, linha.strip().split(',')))) for linha in linhas]
linhas.sort()

# Algoritmo de seleção
for linha in linhas:
    numeros_13 = linha
    combinacoes_de_16 = gerar_combinacoes_de_16(numeros_13)
    
    # Verificar quais combinações de 16 números podem ser adicionadas
    combinacoes_a_adicionar = []
    for combinacao in combinacoes_de_16:
        if combinacao not in combinacoes_16_selecionadas:
            combinacoes_a_adicionar.append(combinacao)
    print("Selecionando combinações de 16 números que cobre mais combinações de 13 números...")
    # Selecionar a combinação de 16 números que cobre mais combinações de 13 números
    combinacao_selecionada = max(combinacoes_a_adicionar, key=lambda c: sum(1 for l in linhas if set(c).issuperset(set(linha))))
    print("Adicionar a combinação de 16 números selecionada")
    # Adicionar a combinação de 16 números selecionada
    combinacoes_16_selecionadas.add(combinacao_selecionada)
    cobertura_comb_13.update([linha for linha in linhas if set(combinacao_selecionada).issuperset(set(linha))])
    print("Criando arquivo")
# Escrever as combinações de 16 números selecionadas em um arquivo
with open('comb_16_numeros_13selecionados.txt', 'w') as arquivo_comb_16_selecionados:
    for combinacao in combinacoes_16_selecionadas:
        arquivo_comb_16_selecionados.write(','.join(map(str, combinacao)) + '\n')

print("Arquivo comb_16_numeros_selecionados.txt criado com as combinações de 16 números selecionadas.")
print(f"Cobertura das combinações de 13 números: {len(cobertura_comb_13)} de {len(linhas)}")
print("Cobertura das combinações de 13 números finalizada.")
