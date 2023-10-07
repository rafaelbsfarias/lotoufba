# domain/repositories/resultado_repository.py

from abc import ABC, abstractmethod
from domain.entities.resultado import Resultado

class ResultadoRepository(ABC):
    @abstractmethod
    def salvar(self, resultado: Resultado):
        pass

    @abstractmethod
    def buscar_todos(self):
        pass