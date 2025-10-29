# api_fast.py [cite: 40]
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import engine, get_db

# Garante que as tabelas sejam criadas (embora já tenhamos feito isso)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Endpoint POST /livros (Adicionar) [cite: 44]
@app.post("/livros", response_model=schemas.Livro, status_code=201) # 
def create_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    db_livro = models.Livro(**livro.dict())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro

# Endpoint GET /livros (Listar todos) [cite: 42]
@app.get("/livros", response_model=List[schemas.Livro], status_code=200)
def read_livros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    livros = db.query(models.Livro).offset(skip).limit(limit).all()
    return livros

# Endpoint GET /livros/{id} (Obter um) [cite: 43]
@app.get("/livros/{id}", response_model=schemas.Livro, status_code=200)
def read_livro(id: int, db: Session = Depends(get_db)):
    db_livro = db.query(models.Livro).filter(models.Livro.id == id).first()
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado") # 
    return db_livro

# Endpoint PUT /livros/{id} (Atualizar) [cite: 45]
@app.put("/livros/{id}", response_model=schemas.Livro, status_code=200)
def update_livro(id: int, livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    db_livro = db.query(models.Livro).filter(models.Livro.id == id).first()
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    # Atualiza os campos
    db_livro.titulo = livro.titulo
    db_livro.autor = livro.autor
    db_livro.ano_publicacao = livro.ano_publicacao
    db_livro.disponivel = livro.disponivel

    db.commit()
    db.refresh(db_livro)
    return db_livro

# Endpoint DELETE /livros/{id} (Excluir) [cite: 46]
@app.delete("/livros/{id}", response_model=schemas.Livro, status_code=200)
def delete_livro(id: int, db: Session = Depends(get_db)):
    db_livro = db.query(models.Livro).filter(models.Livro.id == id).first()
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    db.delete(db_livro)
    db.commit()
    return db_livro