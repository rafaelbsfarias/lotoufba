#############################################
## Gropos de 2 menor frequencia
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

# Encontra todos os grupos de 2 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 2 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")

#############################################
## Gropos de 3 menor frequencia

from itertools import combinations
from collections import Counter

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

# Encontra todos os grupos de 3 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 3 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")


#############################################
## Gropos de 4 menor frequencia

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


#############################################
## Gropos de 5 menor frequencia

from itertools import combinations
from collections import Counter

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

# Encontra todos os grupos de 5 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 5 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")


#############################################
## Gropos de 6 menor frequencia

from itertools import combinations
from collections import Counter

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

# Encontra todos os grupos de 6 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 6 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")


#############################################
## Gropos de 7 menor frequencia

from itertools import combinations
from collections import Counter

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

# Encontra todos os grupos de 7 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 7 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")


#############################################
## Gropos de 8 menor frequencia

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

# Encontra todos os grupos de 8 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 8 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")


#############################################
## Gropos de 9 menor frequencia

from itertools import combinations
from collections import Counter

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

# Encontra todos os grupos de 9 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 9 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")

#############################################
## Gropos de 10 menor frequencia
from itertools import combinations
from collections import Counter

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

# Encontra todos os grupos de 10 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 10 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")


#############################################
## Gropos de 11 menor frequencia

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

# Encontra todos os grupos de 11 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 11 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")

#############################################
## Gropos de 12 menor frequencia

from itertools import combinations
from collections import Counter

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

# Encontra todos os grupos de 12 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 12 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")

#############################################
## Gropos de 13 menor frequencia

from itertools import combinations
from collections import Counter

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

# Encontra todos os grupos de 13 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 13 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")


#############################################
## Gropos de 14 menor frequencia

from itertools import combinations
from collections import Counter

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

# Encontra todos os grupos de 14 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 14 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")

#############################################
## Gropos de 15 menor frequencia

from itertools import combinations
from collections import Counter

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

# Encontra todos os grupos de 15 números, ordenados por frequência
grupos_menos_frequentes = contador_grupos.most_common()[:-1]

print("O grupo de 15 números menos frequente é:", grupos_menos_frequentes[-1][0])
print("Ele apareceu", grupos_menos_frequentes[-1][1], "vezes.")

