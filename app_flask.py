# app_flask.py [cite: 31]
from flask import Flask, render_template, request, redirect, url_for
from database import SessionLocal
from models import Livro
import logging

# Configura o logging para depuração
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # 
def index():
    db = SessionLocal()
    try:
        # Lógica para o método POST (Adicionar livro) 
        if request.method == 'POST':
            app.logger.debug(f"Recebido POST: {request.form}")
            novo_livro = Livro(
                titulo=request.form['titulo'],
                autor=request.form['autor'],
                ano_publicacao=int(request.form['ano_publicacao']),
                disponivel=True
            )
            db.add(novo_livro) # 
            db.commit()
            app.logger.debug("Livro adicionado com sucesso.")
            return redirect(url_for('index'))

        # Lógica para o método GET (Listar livros) 
        livros = db.query(Livro).all() # 
        app.logger.debug(f"Encontrados {len(livros)} livros.")
        # 
        return render_template('index.html', livros=livros) 

    except Exception as e:
        app.logger.error(f"Erro: {e}")
        db.rollback()
        return "Ocorreu um erro.", 500
    finally:
        db.close()

if __name__ == '__main__':
    # Executa o Flask na porta 5000 [cite: 52]
    app.run(debug=True, port=5000)