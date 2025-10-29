# Projeto AV2 - Backend Frameworks

Sistema de cadastro de livros usando Flask e FastAPI.

## Requisitos

* Python 3.10+
* flask
* fastapi
* uvicorn
* sqlalchemy
* pydantic

## Configuração (Linux)

1.  Clone o repositório.
2.  Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt 
    ```
    *(Nota: Você pode criar um `requirements.txt` com `pip freeze > requirements.txt`)*

4.  Crie o banco de dados (SQLite):
    ```bash
    python models.py
    ```

## Execução

É necessário executar as duas aplicações em terminais separados.

**Terminal 1 (Flask - Porta 5000):**
```bash
python app_flask.py