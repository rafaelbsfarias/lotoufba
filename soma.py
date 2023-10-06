# Lê os dados do arquivo resultadosAnteriores.txt
#todasCombinações.txt
#
#with open('todasCombinações.txt', 'r') as arquivo:
#    linhas = arquivo.readlines()
#
## Inicializa contadores para os grupos de somas
#grupos_de_somas = {
#    '120-135': 0,
#    '136-151': 0,
#    '152-167': 0,
#    '168-183': 0,
#    '184-199': 0,
#    '200-215': 0,
#    '216-231': 0,
#    '232-247': 0,
#    '248-263': 0,
#    'maiores_que_264': 0,
#}
#
## Para cada linha, calcule a soma e agrupe nos intervalos apropriados
#for linha in linhas:
#    numeros = [int(numero) for numero in linha.strip().split(',')]
#    soma = sum(numeros)
#    
#    if 120 <= soma <= 135:
#        grupos_de_somas['120-135'] += 1
#    elif 136 <= soma <= 151:
#        grupos_de_somas['136-151'] += 1
#    elif 152 <= soma <= 167:
#        grupos_de_somas['152-167'] += 1
#    elif 168 <= soma <= 183:
#        grupos_de_somas['168-183'] += 1
#    elif 184 <= soma <= 199:
#        grupos_de_somas['184-199'] += 1
#    elif 200 <= soma <= 215:
#        grupos_de_somas['200-215'] += 1
#    elif 216 <= soma <= 231:
#        grupos_de_somas['216-231'] += 1
#    elif 232 <= soma <= 247:
#        grupos_de_somas['232-247'] += 1
#    elif 248 <= soma <= 263:
#        grupos_de_somas['248-263'] += 1
#    else:
#        grupos_de_somas['maiores_que_264'] += 1
#
#
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa contadores para os grupos de somas
grupos_de_somas = {
    '120-129': 0,
    '130-139': 0,
    '140-149': 0,
    '150-159': 0,
    '160-169': 0,
    '170-179': 0,
    '180-189': 0,
    '190-199': 0,
    '200-209': 0,
    '210-219': 0,
    '220-229': 0,
    '230-239': 0,
    '240-249': 0,
    '250-259': 0,
    '260-270': 0,
    
}

# Para cada linha, calcule a soma e agrupe nos intervalos apropriados
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    soma = sum(numeros)
    
    if 120 <= soma <= 129:
        grupos_de_somas['120-129'] += 1
    elif 130 <= soma <= 139:
        grupos_de_somas['130-139'] += 1
    elif 140 <= soma <= 149:
        grupos_de_somas['140-149'] += 1
    elif 150 <= soma <= 159:
        grupos_de_somas['150-159'] += 1
    elif 160 <= soma <= 169:
        grupos_de_somas['160-169'] += 1
    elif 170 <= soma <= 179:
        grupos_de_somas['170-179'] += 1
    elif 180 <= soma <= 189:
        grupos_de_somas['180-189'] += 1
    elif 190 <= soma <= 199:
        grupos_de_somas['190-199'] += 1
    elif 200 <= soma <= 209:
        grupos_de_somas['200-209'] += 1
    elif 210 <= soma <= 219:
        grupos_de_somas['210-219'] += 1
    elif 220 <= soma <= 229:
        grupos_de_somas['220-229'] += 1
    elif 230 <= soma <= 239:
        grupos_de_somas['230-239'] += 1
    elif 240 <= soma <= 249:
        grupos_de_somas['240-249'] += 1
    elif 250 <= soma <= 259:
        grupos_de_somas['250-259'] += 1
    else:
        grupos_de_somas['260-270'] += 1
    

# Exiba os resultados
#for intervalo, contagem in grupos_de_somas.items():
#    print(f'Intervalo {intervalo}: {contagem} ocorrências')


total_ocorrencias = sum(grupos_de_somas.values())

# Exiba os resultados com os percentuais
for intervalo, contagem in grupos_de_somas.items():
    percentual = (contagem / total_ocorrencias) * 100
    print(f'Intervalo {intervalo}: {contagem} ocorrências ({percentual:.2f}%)')