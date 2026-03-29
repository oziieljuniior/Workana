import sqlite3
import os
from pathlib import Path
import dotenv

# Caminho do banco
dotenv.load_dotenv()
DB_PATH = Path(os.getenv("DATABASE_PATH"))


def criar_banco():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hash TEXT UNIQUE,
        titulo TEXT,
        link TEXT UNIQUE,
        descricao TEXT,
        cliente_verificado BOOLEAN,
        cliente_pagamento_verificado BOOLEAN,
        cliente_historico TEXT,
        enviar_proposta BOOLEAN DEFAULT 0,
        enviado_telegram BOOLEAN DEFAULT 0,
        data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def salvar_projeto(
    titulo,
    link,
    descricao,
    hash_id,
    cliente_verificado=False,
    cliente_pagamento_verificado=False,
    cliente_historico="",
    enviar_proposta=False,
    telegram_enviado=False
):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT OR IGNORE INTO projetos 
        (
            hash,
            titulo,
            link,
            descricao,
            cliente_verificado,
            cliente_pagamento_verificado,
            cliente_historico,
            enviar_proposta,
            enviado_telegram
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            hash_id,
            titulo,
            link,
            descricao,
            cliente_verificado,
            cliente_pagamento_verificado,
            cliente_historico,
            enviar_proposta,
            telegram_enviado
        ))

        conn.commit()

    except Exception as e:
        print("Erro ao salvar projeto:", e)

    conn.close()


def projeto_existe(hash_id):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM projetos WHERE hash = ?",
        (hash_id,)
    )

    resultado = cursor.fetchone()

    conn.close()

    return resultado is not None
