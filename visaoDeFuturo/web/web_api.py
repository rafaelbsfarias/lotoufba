from flask import Flask, jsonify
from application.use_cases.lotofacil import LotofacilUseCase
from infrastructure.database.sqlite_repository import SQLiteResultadoRepository
from application.services.lotofacil_api import LotofacilAPI

import sqlite3
import sys
import os

# Obtém o diretório atual do script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Adiciona o diretório raiz do projeto ao caminho de busca do Python
project_root = os.path.join(current_dir, "../../")
sys.path.insert(0, project_root)

app = Flask(__name__)

db_file = "lotocerta.db"
resultado_repository = SQLiteResultadoRepository(db_file)
lotofacil_api = LotofacilAPI()
lotofacil_use_case = LotofacilUseCase(resultado_repository, lotofacil_api)

@app.route('/resultado/<int:concurso_num>')
def obter_e_salvar_resultado(concurso_num):
    lotofacil_use_case.buscar_resultado_e_salvar(concurso_num)
    return jsonify({"message": "Resultado salvo com sucesso"})

@app.route('/resultados')
def listar_resultados():
    resultados = resultado_repository.buscar_todos()
    resultados_json = [{"concurso": r.concurso, "dezenas": r.dezenas, "data_sorteio": r.data_sorteio} for r in resultados]
    return jsonify(resultados_json)

@app.route('/datas', methods=['GET'])
def get_datas():
    try:
        # Conecte-se ao banco de dados SQLite
        conn = sqlite3.connect('datas.db')
        cursor = conn.cursor()

        # Execute uma consulta SQL para obter os dados
        cursor.execute("SELECT data_loteria FROM datas")

        # Recupere os dados do banco de dados
        datas = cursor.fetchall()

        # Feche a conexão com o banco de dados
        conn.close()

        # Converta os dados em uma lista de dicionários
        data_list = [{'data_loteria': data[0]} for data in datas]

        return jsonify(data_list)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
