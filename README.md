# lotocerta

################################

## Estrutura de Diretórios:

```
lotocerta/
 ├── application/
 │   ├── use_cases/
 │   │   ├── lotofacil.py  # Casos de uso relacionados à Lotofácil
 │   └── services/
 │       ├── lotofacil_api.py  # Serviços para acessar a API da Lotofácil
 ├── domain/
 │   ├── entities/
 │   │   ├── resultado.py  # Entidade Resultado
 │   └── repositories/
 │       ├── resultado_repository.py  # Interface de repositório para Resultados
 ├── infrastructure/
 │   ├── database/
 │   │   ├── sqlite_repository.py  # Implementação do repositório SQLite
 │   └── web/
 │       ├── web_api.py  # Interface da Web para interagir com o aplicativo
 └── main.py  # Ponto de entrada do aplicativo
 ```


##Objetivo
Listar todas as cartelas que somem 184 a 199 pontos e que nunca foram sorteadas.

OBS: Mais recursos estatísticos serão solicitaods no futuro.


###Tecnologias:
________________________________________________________________

Python
SQLite

