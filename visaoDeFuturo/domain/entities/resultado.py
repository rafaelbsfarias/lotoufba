# domain/entities/resultado.py

class Resultado:
    def __init__(self, concurso, dezenas, data_sorteio):
        self.concurso = concurso
        self.dezenas = dezenas
        self.data_sorteio = data_sorteio
