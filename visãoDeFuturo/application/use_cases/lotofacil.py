# application/use_cases/lotofacil.py

from domain.entities.resultado import Resultado
from domain.repositories.resultado_repository import ResultadoRepository
from application.services.lotofacil_api import LotofacilAPI

class LotofacilUseCase:
    def __init__(self, resultado_repository: ResultadoRepository, lotofacil_api: LotofacilAPI):
        self.resultado_repository = resultado_repository
        self.lotofacil_api = lotofacil_api

    def buscar_resultado_e_salvar(self, concurso_num):
        data = self.lotofacil_api.obter_resultado(concurso_num)
        if "data_sorteio" in data:
            concurso = concurso_num
            dezenas = ', '.join(map(str, data["dezenas"]))
            data_sorteio = data["data_sorteio"]

            resultado = Resultado(concurso, dezenas, data_sorteio)
            self.resultado_repository.salvar(resultado)
