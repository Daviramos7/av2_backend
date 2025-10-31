# Projeto AV2: API de Biblioteca (Flask + FastAPI)

Este projeto é a atividade de avaliação (AV2) da disciplina de Backend Frameworks. O objetivo é desenvolver um sistema simples de cadastro de livros para uma biblioteca universitária, utilizando Flask para a interface web e FastAPI para uma API RESTful.
Ambas as aplicações se conectam a um banco de dados SQLite compartilhado.

## 📚 Bibliotecas Utilizadas

* `Flask`
* `FastAPI`
* `Uvicorn`
* `SQLAlchemy`
* `Pydantic`

## 🚀 Guia de Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Pré-requisitos

* Python 3.10 ou superior
* `pip` (gerenciador de pacotes do Python)

### 2. Configuração do Ambiente

1. Clone este repositório:
```bash
git clone [URL_DO_SEU_REPOSITORIO]
cd [NOME_DA_PASTA_DO_PROJETO]
```

2. Crie e ative um ambiente virtual (venv):
   * No Linux/macOS:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

   * No Windows (PowerShell):
```powershell
   python -m venv venv
   .\venv\Scripts\activate
```

3. Instale as dependências: Com o ambiente virtual ativado, execute:
```bash
pip install flask sqlalchemy fastapi "uvicorn[standard]" pydantic
```

### 3. Criação do Banco de Dados

Antes de rodar as aplicações, é necessário criar o arquivo de banco de dados (`biblioteca.db`) e a tabela `livros`. Execute o script:
```bash
python models.py
```

### 4. Executando as Aplicações

É necessário executar as duas aplicações simultaneamente, em dois terminais separados. Certifique-se de que o `venv` esteja ativado em ambos.

**Terminal 1 (Aplicação Flask):**
```bash
python app_flask.py
```

O servidor Flask estará rodando na `http://127.0.0.1:5000/`.

**Terminal 2 (API FastAPI):**
```bash
uvicorn api_fast:app --reload --port 8000
```

O servidor FastAPI estará rodando na `http://127.0.0.1:8000/`.

## 🧪 Acessando o Sistema

Após iniciar os dois servidores, você pode testar:

1. **Interface Web (Flask):** Acesse no seu navegador para cadastrar e listar os livros.
   * URL: `http://127.0.0.1:5000/`

2. **Documentação da API (FastAPI):** Acesse a documentação interativa (Swagger UI) para testar todos os endpoints CRUD (GET, POST, PUT, DELETE).
   * URL: `http://127.0.0.1:8000/docs`
