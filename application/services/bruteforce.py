import sqlite3

# Conecte-se ao banco de dados (ou crie se não existir)
conn = sqlite3.connect('todosPossiveis.db')
cursor = conn.cursor()

# Crie uma tabela para armazenar as combinações
cursor.execute('''
    CREATE TABLE IF NOT EXISTS lotofacil (
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

# Insira todas as combinações possíveis
for n1 in range(1, 12):
    for n2 in range(n1 + 1, 13):
        for n3 in range(n2 + 1, 14):
            for n4 in range(n3 + 1, 15):
                for n5 in range(n4 + 1, 16):
                    for n6 in range(n5 + 1, 17):
                        for n7 in range(n6 + 1, 18):
                            for n8 in range(n7 + 1, 19):
                                for n9 in range(n8 + 1, 20):
                                    for n10 in range(n9 + 1, 21):
                                        for n11 in range(n10 + 1, 22):
                                            for n12 in range(n11 + 1, 23):
                                                for n13 in range(n12 + 1, 24):
                                                    for n14 in range(n13 + 1, 25):
                                                        for n15 in range(n14 + 1, 26):
                                                            cursor.execute('''
                                                                INSERT INTO lotofacil (
                                                                    numero1, numero2, numero3, numero4, numero5,
                                                                    numero6, numero7, numero8, numero9, numero10,
                                                                    numero11, numero12, numero13, numero14, numero15
                                                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                                            ''', (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15))

# Commit (salve) as alterações e feche a conexão com o banco de dados
conn.commit()
conn.close()

print("Banco de dados criado e populado com todas as combinações possíveis.")
