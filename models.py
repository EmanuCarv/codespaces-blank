from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]

    livros: Mapped[list["Livro"]] = relationship(back_populates="categoria")


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    autor: Mapped[str]
    ano: Mapped[int]
    nota: Mapped[float] = mapped_column(default=0)
    lido: Mapped[bool] = mapped_column(default=False)

    categoria_id: Mapped[int] = mapped_column(
        ForeignKey("categorias.id")
    )

    categoria: Mapped["Categoria"] = relationship(back_populates="livros")