import sqlite3

# Conecte-se ao banco de dados
conn = sqlite3.connect('resultados.db')
cursor = conn.cursor()

# Execute uma consulta para obter os resultados
cursor.execute('SELECT * FROM resultados')

# Crie o arquivo "resultadosAnteriores.txt" e escreva os números
with open('resultadosAnteriores.txt', 'w') as arquivo:
    for linha in cursor.fetchall():
        numeros = linha[1:]  # Pule o primeiro valor (assumindo que seja um ID)
        linha_formatada = ",".join(map(str, numeros))  # Formate a linha com números separados por vírgula
        arquivo.write(f"{linha_formatada}\n")

# Feche a conexão com o banco de dados
conn.close()

print("Arquivo resultadosAnteriores.txt criado com os números separados por vírgula.")
