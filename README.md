# 📚 Biblioteca

Sistema web de gerenciamento de livros desenvolvido com **FastAPI**, **SQLAlchemy** e **Jinja2**. Permite cadastrar, listar, editar e excluir livros, organizados por categorias, com controle de leitura e avaliação.

---

## 👥 Integrantes

- Hananda Islla
- Maresa Nascimento
- Maria Emanuele

---

## 🎯 Tema

**Biblioteca** — gerenciamento pessoal de acervo de livros.

---

## ✨ Funcionalidades

- **Listagem de livros** — exibe todos os livros cadastrados em cards com título, autor, ano, categoria, nota e status de leitura
- **Cadastro de livro** — formulário para adicionar novos livros com título, autor, ano, categoria, nota (0–10) e marcação de lido/não lido
- **Edição de livro** — atualização de qualquer campo de um livro existente
- **Exclusão de livro** — remoção de um livro do acervo
- **Categorias** — cada livro pertence a uma categoria (ex.: ficção, romance, técnico)
- **Status de leitura** — indica se o livro foi lido ou ainda está na fila

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | [FastAPI](https://fastapi.tiangolo.com/) |
| ORM | [SQLAlchemy](https://www.sqlalchemy.org/) |
| Banco de dados | PostgreSQL via [Supabase](https://supabase.com/) |
| Templates | [Jinja2](https://jinja.palletsprojects.com/) |
| Configuração | [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) |
| Gerenciador de pacotes | [uv](https://docs.astral.sh/uv/) |

---

## 📁 Estrutura do Projeto

```
├── main.py          # Rotas da aplicação (CRUD de livros)
├── models.py        # Modelos ORM: Livro e Categoria
├── database.py      # Configuração do banco e sessão SQLAlchemy
├── pyproject.toml   # Dependências e tasks do projeto
├── static/
│   └── style.css    # Estilização da interface
└── templates/
    ├── base.html    # Layout base com header e navegação
    ├── lista.html   # Listagem de livros em cards
    └── form.html    # Formulário de cadastro e edição
```

---

## ⚙️ Como Executar

### Pré-requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado
- Banco de dados PostgreSQL (ou projeto no Supabase)

### Configuração

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd codespaces-blank
   ```

2. Instale as dependências:
   ```bash
   uv sync
   ```

3. Crie o arquivo `.env` na raiz do projeto com a URL do banco:
   ```env
   DATABASE_URL=postgresql+psycopg://usuario:senha@host:porta/banco
   ```

4. Inicie o servidor de desenvolvimento:
   ```bash
   uv run task run
   ```

5. Acesse a aplicação em [http://localhost:8000](http://localhost:8000)

---

## 🗄️ Modelos de Dados

### Livro
| Campo | Tipo | Descrição |
|---|---|---|
| id | int | Identificador único |
| titulo | str | Título do livro |
| autor | str | Nome do autor |
| ano | int | Ano de publicação |
| nota | float | Avaliação de 0 a 10 |
| lido | bool | Status de leitura |
| categoria_id | int | Referência à categoria |

### Categoria
| Campo | Tipo | Descrição |
|---|---|---|
| id | int | Identificador único |
| nome | str | Nome da categoria |

---

## 🔗 Rotas

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Redireciona para `/livros` |
| GET | `/livros` | Lista todos os livros |
| GET | `/livros/novo` | Exibe o formulário de cadastro |
| POST | `/livros` | Cria um novo livro |
| GET | `/livros/{id}/editar` | Exibe o formulário de edição |
| POST | `/livros/{id}/editar` | Atualiza um livro |
| POST | `/livros/{id}/excluir` | Exclui um livro |


<img width="1353" height="633" alt="image" src="https://github.com/user-attachments/assets/7f2d5a84-b0ff-481e-a105-f723a52e83df" />
<img width="1349" height="629" alt="image" src="https://github.com/user-attachments/assets/3afa4bcb-b1f6-40f9-b308-3678fc47d6f9" />


