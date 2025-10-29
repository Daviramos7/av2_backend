# schemas.py
from pydantic import BaseModel
from typing import Optional

# Modelo Pydantic para a criação de um livro (POST/PUT)
class LivroBase(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: int
    disponivel: Optional[bool] = True

class LivroCreate(LivroBase):
    pass

# Modelo Pydantic para a leitura de um livro (GET)
class Livro(LivroBase):
    id: int

    class Config:
        orm_mode = True # Permite que o Pydantic leia dados de ORM (SQLAlchemy)