from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()


# Modelo da tarefa
class Tarefa(BaseModel):
    nome: str
    descricao: str
    status: str


# Conexão com o banco de dados
def conectar_banco():
    conexao = sqlite3.connect("livros.db")
    conexao.row_factory = sqlite3.Row
    return conexao


# Criação da tabela
def criar_tabela():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


criar_tabela()


# GET - Listar todas as tarefas
@app.get("/tarefas")
def listar_tarefas():
    conexao = conectar_banco()

    tarefas = conexao.execute(
        "SELECT * FROM tarefas"
    ).fetchall()

    conexao.close()

    return [dict(tarefa) for tarefa in tarefas]


# POST - Criar uma nova tarefa
@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    conexao = conectar_banco()

    cursor = conexao.execute(
        """
        INSERT INTO tarefas (nome, descricao, status)
        VALUES (?, ?, ?)
        """,
        (tarefa.nome, tarefa.descricao, tarefa.status)
    )

    conexao.commit()

    tarefa_id = cursor.lastrowid

    nova_tarefa = conexao.execute(
        "SELECT * FROM tarefas WHERE id = ?",
        (tarefa_id,)
    ).fetchone()

    conexao.close()

    return dict(nova_tarefa)


# PUT - Atualizar uma tarefa
@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa: Tarefa):
    conexao = conectar_banco()

    tarefa_existente = conexao.execute(
        "SELECT * FROM tarefas WHERE id = ?",
        (tarefa_id,)
    ).fetchone()

    if tarefa_existente is None:
        conexao.close()
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada."
        )

    conexao.execute(
        """
        UPDATE tarefas
        SET nome = ?, descricao = ?, status = ?
        WHERE id = ?
        """,
        (
            tarefa.nome,
            tarefa.descricao,
            tarefa.status,
            tarefa_id
        )
    )

    conexao.commit()

    tarefa_atualizada = conexao.execute(
        "SELECT * FROM tarefas WHERE id = ?",
        (tarefa_id,)
    ).fetchone()

    conexao.close()

    return dict(tarefa_atualizada)


# DELETE - Remover uma tarefa
@app.delete("/tarefas/{tarefa_id}")
def remover_tarefa(tarefa_id: int):
    conexao = conectar_banco()

    tarefa_existente = conexao.execute(
        "SELECT * FROM tarefas WHERE id = ?",
        (tarefa_id,)
    ).fetchone()

    if tarefa_existente is None:
        conexao.close()
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada."
        )

    conexao.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (tarefa_id,)
    )

    conexao.commit()
    conexao.close()

    return {"mensagem": "Tarefa removida com sucesso!"}