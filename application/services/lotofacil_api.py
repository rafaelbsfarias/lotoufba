# application/services/lotofacil_api.py

import requests

class LotofacilAPI:
    def obter_resultado(self, concurso_num):
        base_url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil/"
        url = base_url + str(concurso_num)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
