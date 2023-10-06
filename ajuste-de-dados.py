import sqlite3
import os

# Nome do arquivo do banco de dados de destino
db_destino = 'resultados.db'

# Verificar se o arquivo do banco de dados já existe
if not os.path.exists(db_destino):
    # Se não existir, crie o banco de dados
    conn_destino = sqlite3.connect(db_destino)
    conn_destino.close()

# Conectar ao banco de dados lotofacil.db (seu banco de origem)
conn_origem = sqlite3.connect('lotofacil.db')
cursor_origem = conn_origem.cursor()

# Conectar ao novo banco de dados resultados.db
conn_destino = sqlite3.connect(db_destino)
cursor_destino = conn_destino.cursor()

# Criar a tabela resultados no novo banco de dados com o esquema desejado
cursor_destino.execute('''
    CREATE TABLE IF NOT EXISTS resultados (
        id INTEGER PRIMARY KEY,
        numero1 INTEGER,
        numero2 INTEGER,
        numero3 INTEGER,
        numero4 INTEGER,
        numero5 INTEGER,
        numero6 INTEGER,
        numero7 INTEGER,
        numero8 INTEGER,
        numero9 INTEGER,
        numero10 INTEGER,
        numero11 INTEGER,
        numero12 INTEGER,
        numero13 INTEGER,
        numero14 INTEGER,
        numero15 INTEGER
    )
''')

# Consulta para recuperar todos os dados da tabela resultados do banco de origem
cursor_origem.execute("SELECT * FROM resultados")
resultados_origem = cursor_origem.fetchall()

# Iterar por todos os resultados e migrá-los para o novo banco de dados
for resultado in resultados_origem:
    concurso = resultado[0]
    dezenas = resultado[1].split(', ')
    
    if len(dezenas) == 15:
        dezenas_int = [int(dezena) for dezena in dezenas]
        cursor_destino.execute('''
            INSERT INTO resultados (
                numero1, numero2, numero3, numero4, numero5, numero6, numero7,
                numero8, numero9, numero10, numero11, numero12, numero13, numero14, numero15
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', tuple(dezenas_int))
    else:
        print(f"Número de dezenas inválido no resultado do concurso {concurso}.")

# Fazer commit de todas as inserções no novo banco de dados
conn_destino.commit()
print("Dados inseridos com sucesso no novo banco de dados.")

# Fechar as conexões com os bancos de dados
conn_origem.close()
conn_destino.close()

## Conectar ao banco de dados resultados.db
#conn = sqlite3.connect('resultados.db')
#cursor = conn.cursor()
#
## Executar a consulta SQL para recuperar o campo numero11 de todas as entidades
#cursor.execute("SELECT numero11 FROM resultados")
#
## Recuperar todos os valores do campo numero11
#resultados_numero11 = cursor.fetchall()
#
## Fechar a conexão com o banco de dados
#conn.close()
#
## Imprimir os valores de numero11
#for resultado in resultados_numero11:
#    print(resultado[0])
