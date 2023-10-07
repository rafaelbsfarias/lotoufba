# infrastructure/database/sqlite_repository.py

import sqlite3
from domain.repositories.resultado_repository import ResultadoRepository
from domain.entities.resultado import Resultado

class SQLiteResultadoRepository(ResultadoRepository):
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS resultados (
                concurso INTEGER PRIMARY KEY,
                dezenas TEXT,
                data_sorteio TEXT
            )
        """)

    def salvar(self, resultado: Resultado):
        self.cursor.execute("""
            INSERT INTO resultados (concurso, dezenas, data_sorteio)
            VALUES (?, ?, ?)
        """, (resultado.concurso, resultado.dezenas, resultado.data_sorteio))

        self.conn.commit()

    def buscar_todos(self):
        self.cursor.execute("SELECT * FROM resultados")
        rows = self.cursor.fetchall()

        resultados = []
        for row in rows:
            concurso, dezenas, data_sorteio = row
            resultado = Resultado(concurso, dezenas, data_sorteio)
            resultados.append(resultado)

        return resultados