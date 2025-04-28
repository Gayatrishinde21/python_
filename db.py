from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker, declarative_base
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:postgres@192.168.6.80:5432/BIS_API"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
