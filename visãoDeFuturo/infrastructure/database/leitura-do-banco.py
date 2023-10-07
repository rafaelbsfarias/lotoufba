import sqlite3

# Nome do arquivo do banco de dados
db_filename = "data.db"

try:
    # Conecte-se ao banco de dados SQLite
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    # Execute uma consulta SQL para selecionar todos os dados da tabela
    cursor.execute("SELECT * FROM datas")

    # Recupere todos os registros da tabela
    rows = cursor.fetchall()

    # Imprima os registros
    for row in rows:
        print(row)

    # Feche a conexão com o banco de dados
    conn.close()

except sqlite3.Error as e:
    print("Erro ao acessar o banco de dados:", e)