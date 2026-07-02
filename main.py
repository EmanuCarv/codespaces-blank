from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
from database import Base, engine, get_session


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Página inicial
@app.get("/")
def home():
    return RedirectResponse(url="/livros")


# LISTAR LIVROS
@app.get("/livros")
def listar(request: Request, session: Session = Depends(get_session)):
    livros = session.scalars(select(models.Livro)).all()

    return templates.TemplateResponse(
        request,
        "lista.html",
        {"livros": livros},
    )


# FORMULÁRIO NOVO LIVRO
@app.get("/livros/novo")
def form_novo(request: Request, session: Session = Depends(get_session)):
    categorias = session.scalars(select(models.Categoria)).all()

    return templates.TemplateResponse(
        request,
        "form.html",
        {
            "livro": None,
            "categorias": categorias,
        },
    )


# CRIAR LIVRO
@app.post("/livros")
def criar(
    titulo: str = Form(...),
    autor: str = Form(...),
    editora: str = Form(...),
    ano: int = Form(...),
    imagem: str = Form(...),
    categoria_id: int = Form(...),
    nota: float = Form(0),
    lido: bool = Form(False),
    session: Session = Depends(get_session),
):
    livro = models.Livro(
        titulo=titulo,
        autor=autor,
        editora=editora,
        ano=ano,
        imagem=imagem,
        categoria_id=categoria_id,
        nota=nota,
        lido=lido,
    )

    session.add(livro)
    session.commit()

    return RedirectResponse(
        url="/livros",
        status_code=303,
    )


# FORMULÁRIO EDITAR
@app.get("/livros/{livro_id}/editar")
def form_editar(
    livro_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    livro = session.get(models.Livro, livro_id)

    categorias = session.scalars(
        select(models.Categoria)
    ).all()

    return templates.TemplateResponse(
        request,
        "form.html",
        {
            "livro": livro,
            "categorias": categorias,
        },
    )


# ATUALIZAR
@app.post("/livros/{livro_id}/editar")
def atualizar(
    livro_id: int,
    titulo: str = Form(...),
    autor: str = Form(...),
    editora: str = Form(...),
    ano: int = Form(...),
    categoria_id: int = Form(...),
    nota: float = Form(0),
    lido: bool = Form(False),
    session: Session = Depends(get_session),
):
    livro = session.get(models.Livro, livro_id)

    livro.titulo = titulo
    livro.autor = autor
    livro.editora = editora
    livro.ano = ano
    livro.categoria_id = categoria_id
    livro.nota = nota
    livro.lido = lido

    session.commit()

    return RedirectResponse(
        url="/livros",
        status_code=303,
    )


# EXCLUIR
@app.post("/livros/{livro_id}/excluir")
def excluir(
    livro_id: int,
    session: Session = Depends(get_session),
):
    livro = session.get(models.Livro, livro_id)

    session.delete(livro)
    session.commit()

    return RedirectResponse(
        url="/livros",
        status_code=303,
    )