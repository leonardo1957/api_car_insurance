from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String)
    ano = Column(Integer)
    valor = Column(Float)
    local_de_registro = Column(String, nullable=True)