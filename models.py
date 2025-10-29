# models.py
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from database import Base, engine

class Livro(Base):
    __tablename__ = "livros" # Nome da tabela 

    # Definição das colunas conforme os requisitos
    id = Column(Integer, primary_key=True, index=True, autoincrement=True) # [cite: 23]
    titulo = Column(String, index=True) # [cite: 24]
    autor = Column(String, index=True) # [cite: 25]
    ano_publicacao = Column(Integer) # [cite: 26]
    disponivel = Column(Boolean, default=True) # [cite: 27]

# Função para criar o banco e a tabela
def create_database():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_database()
    print("Banco de dados e tabela 'livros' criados com sucesso.")