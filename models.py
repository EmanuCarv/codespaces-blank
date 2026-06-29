# models.py
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Genero(Base):
    __tablename__ = 'generos'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    filmes: Mapped[list['Filme']] = relationship(back_populates='genero')

class Filme(Base):
    __tablename__ = 'filmes'
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    diretor: Mapped[str]
    ano: Mapped[int]
    nota: Mapped[float] = mapped_column(default=0)
    assistido: Mapped[bool] = mapped_column(default=False)
    genero_id: Mapped[int] = mapped_column(ForeignKey('generos.id'))   # FK
    genero: Mapped['Genero'] = relationship(back_populates='filmes')