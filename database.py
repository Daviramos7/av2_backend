# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a URL do banco de dados SQLite
DATABASE_URL = "sqlite:///./biblioteca.db"

# Cria o motor (engine) de conexão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Cria uma classe SessionLocal para gerenciar as sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe Base para os modelos declarativos
Base = declarative_base()

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()