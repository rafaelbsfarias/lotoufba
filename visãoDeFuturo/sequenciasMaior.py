
####Sequencia2
from itertools import combinations
from collections import Counter

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 2 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 2 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_2 = list(combinations(numeros, 2))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_2)

# Encontra o grupo de 2 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 2 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")


####Sequencia3

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 3 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 3 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_3 = list(combinations(numeros, 3))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_3)

# Encontra o grupo de 3 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 3 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")


################################################################
## Sequencia4

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

# Encontra o grupo de 4 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 4 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")



################################################################
## Sequencia5

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 5 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 5 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_5 = list(combinations(numeros, 5))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_5)

# Encontra o grupo de 5 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 5 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")


################################################################
## Sequencia6

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 6 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 6 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_6 = list(combinations(numeros, 6))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_6)

# Encontra o grupo de 6 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 6 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")


################################################################
## Sequencia7

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


################################################################
## Sequencia8

from itertools import combinations
from collections import Counter

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 8 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 8 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_8 = list(combinations(numeros, 8))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_8)

# Encontra o grupo de 8 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 8 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")


################################################################
## Sequencia9

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 9 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 9 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_9 = list(combinations(numeros, 9))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_9)

# Encontra o grupo de 9 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 9 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")

################################################################
## Sequencia10

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 10 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 10 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_10 = list(combinations(numeros, 10))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_10)

# Encontra o grupo de 10 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 10 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")

################################################################
## Sequencia11

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

# Encontra o grupo de 11 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 11 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")

################################################################
## Sequencia12

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 12 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 12 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_12 = list(combinations(numeros, 12))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_12)

# Encontra o grupo de 12 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 12 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")


################################################################
## Sequencia13


# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 13 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 13 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_13 = list(combinations(numeros, 13))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_13)

# Encontra o grupo de 13 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 13 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")


################################################################
## Sequencia14

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 14 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 14 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_14 = list(combinations(numeros, 14))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_14)

# Encontra o grupo de 14 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 14 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")



################################################################
## Sequencia15

# Lê os dados do arquivo resultadosAnteriores.txt
with open('resultadosAnteriores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializa um contador para os grupos de 15 números
contador_grupos = Counter()

# Para cada linha, gera todas as combinações de 15 números
for linha in linhas:
    numeros = [int(numero) for numero in linha.strip().split(',')]
    grupos_de_15 = list(combinations(numeros, 15))
    
    # Atualiza o contador com os grupos gerados
    contador_grupos.update(grupos_de_15)

# Encontra o grupo de 15 números mais frequente
grupo_mais_frequente = contador_grupos.most_common(1)[0]

print("O grupo de 15 números mais frequente é:", grupo_mais_frequente[0])
print("Ele apareceu", grupo_mais_frequente[1], "vezes.")
