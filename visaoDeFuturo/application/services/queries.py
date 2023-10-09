import sqlite3

def criar_tabela_resultados():
    conn = sqlite3.connect("lotofacil.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resultados (
            concurso INTEGER PRIMARY KEY,
            dezenas TEXT            
        )
    """)
    
    conn.commit()
    conn.close()

def inserir_resultado(concurso, dezenas):
    conn = sqlite3.connect("lotofacil.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO resultados (concurso, dezenas)
        VALUES (?, ?)
    """, (concurso, dezenas))
    
    conn.commit()
    conn.close()

def buscar_resultados():
    conn = sqlite3.connect("lotofacil.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM resultados")
    resultados = cursor.fetchall()
    
    conn.close()
    
    return resultados
