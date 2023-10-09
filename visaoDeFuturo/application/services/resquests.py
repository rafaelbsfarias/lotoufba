import requests
import time

base_url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil/"
concurso_num = 2900  # Número inicial do concurso

while True:
    try:
        url = base_url + str(concurso_num)  # Construir a URL com o número do concurso
        response = requests.get(url)
        response.raise_for_status()  # Verifica se ocorreu algum erro na resposta

        # Verifica se a resposta não está vazia
        if response.text.strip():
            data = response.json()

            dezenas = ','.join(map(str, data["dezenas"]))

            # Lê o conteúdo atual do arquivo
            with open("resultadosAnteriores.txt", "r") as file:
                existing_content = file.read()

            # Salva as dezenas no arquivo, acrescentando uma nova linha
            with open("resultadosAnteriores.txt", "a") as file:
                # Adicione um separador se já houver conteúdo no arquivo
                if existing_content:
                    file.write("\n")
                file.write(dezenas)
                print("Dezenas incluídas no arquivo:", dezenas)

        concurso_num += 1  # Incrementar o número do concurso

    except requests.exceptions.RequestException as e:
        print("Erro na chamada à API:", e)

    # Pausa de 1 segundo antes de fazer a próxima chamada
    time.sleep(0.25)
