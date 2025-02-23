from sqlalchemy import Column, Integer, Float
from app.db.base import Base

class Franquia(Base):
    __tablename__ = "franquias"

    id = Column(Integer, primary_key=True, index=True)
    porcentagem = Column(Float)