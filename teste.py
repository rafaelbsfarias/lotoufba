#import sqlite3
#
## Conectar ao banco de dados todosPossiveis.db
#conn = sqlite3.connect('todosPossiveis.db')
#cursor = conn.cursor()
#
## ID do resultado que queremos buscar
#resultado_id = 1  # Altere para o ID desejado
#
## Consulta SQL para recuperar os números pelo ID
#query = f'''
#    SELECT numero1, numero2, numero3, numero4, numero5,
#           numero6, numero7, numero8, numero9, numero10,
#           numero11, numero12, numero13, numero14, numero15
#    FROM lotofacil
#    WHERE id = {resultado_id}
#'''
#
## Execute a consulta
#cursor.execute(query)
#
## Recupere os números
#numeros = cursor.fetchone()
#
## Feche a conexão com o banco de dados
#conn.close()
#
## Verifique se encontrou o resultado
#if numeros:
#    # Calcule a soma dos números
#    soma = sum(numeros)
#    print(f'Soma dos números para o resultado ID {resultado_id}: {soma}')
#else:
#    print(f'Resultado com ID {resultado_id} não encontrado.')
#



import sqlite3

# Conectar ao banco de dados todosPossiveis.db
conn = sqlite3.connect('todosPossiveis.db')
cursor = conn.cursor()

# Abra o arquivo soma.txt para escrita
with open('soma.txt', 'w') as arquivo_soma:
    # Inicialize o ID
    resultado_id = 1

    # Continue buscando resultados até não encontrar mais nenhum
    while True:
        # Consulta SQL para recuperar os números pelo ID
        query = f'''
            SELECT numero1, numero2, numero3, numero4, numero5,
                numero6, numero7, numero8, numero9, numero10,
                numero11, numero12, numero13, numero14, numero15
            FROM lotofacil
            WHERE id = {resultado_id}
        '''

        # Execute a consulta
        cursor.execute(query)

        # Recupere os números
        numeros = cursor.fetchone()

        # Verifique se encontrou o resultado
        if numeros:
            # Calcule a soma dos números
            soma = sum(numeros)
            # Escreva a soma no arquivo soma.txt
            if 184 <= soma <= 199:
                arquivo_soma.write(f'{soma}\n')
        else:
            # Se não encontrou mais resultados, saia do loop
            break

        # Incrementa o ID para buscar o próximo resultado
        resultado_id += 1

# Feche a conexão com o banco de dados
conn.close()

print("Somas foram escritas em 'soma.txt'.")