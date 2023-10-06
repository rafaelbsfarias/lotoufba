import requests
import time
from queries import criar_tabela_resultados, inserir_resultado

base_url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil/"
concurso_num = 2887  # Número inicial do concurso

# Criar a tabela de resultados se não existir
criar_tabela_resultados()

while True:
    try:
        url = base_url + str(concurso_num)  # Construir a URL com o número do concurso
        response = requests.get(url)
        response.raise_for_status()  # Verifica se ocorreu algum erro na resposta
        data = response.json()

        concurso = concurso_num
        dezenas = ', '.join(map(str, data["dezenas"]))

        # Inserir os dados na tabela
        inserir_resultado(concurso, dezenas)

        concurso_num += 1  # Incrementar o número do concurso

    except requests.exceptions.RequestException as e:
        print("Erro na chamada à API:", e)

    # Pausa de 1 segundo antes de fazer a próxima chamada
    time.sleep(0.25)
