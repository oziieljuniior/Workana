import sqlite3
from pathlib import Path

#/home/darkcover/Documentos/Workana/data/workana.db
DB_PATH = Path("/home/darkcover/Documentos/Workana/data/workana.db")

def criar_banco():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        link TEXT UNIQUE,
        descricao TEXT,
        data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def salvar_projeto(titulo, link, descricao):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO projetos (titulo, link, descricao)
        VALUES (?, ?, ?)
        """, (titulo, link, descricao))

        conn.commit()

    except Exception as e:
        print("Projeto já existe ou erro:", e)

    conn.close()


