from collections import Counter

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os números
contador_numeros = Counter()

# Para cada linha, conte a frequência de cada número
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    contador_numeros.update(numeros)

# Calcule o total de números no arquivo
total_numeros = sum(contador_numeros.values())

# Ordene os números pela frequência relativa (em ordem decrescente)
numeros_ordenados = sorted(contador_numeros.items(), key=lambda x: x[1], reverse=True)

# Exiba a frequência absoluta e relativa de cada número (ordenado)
for numero, frequencia_absoluta in numeros_ordenados:
    frequencia_relativa = (frequencia_absoluta / total_numeros) * 100
    print(f'Número {numero}: Frequência Absoluta = {frequencia_absoluta}, Frequência Relativa = {frequencia_relativa:.2f}%')
