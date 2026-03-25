import sqlite3
import os
from pathlib import Path

# Caminho do banco
DB_PATH = Path("/home/darkcover/Documentos/Workana/data/workana.db")


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


# Buscar projetos não enviados ao Telegram
def buscar_projetos_nao_enviados():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 
        id,
        titulo,
        link,
        descricao,
        cliente_verificado,
        cliente_pagamento_verificado,
        cliente_historico,
        enviar_proposta
    FROM projetos
    WHERE enviado_telegram = 0
    ORDER BY data_coleta DESC
    """)

    projetos = cursor.fetchall()

    conn.close()

    return projetos


# Buscar projetos para enviar proposta
def buscar_projetos_para_proposta():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM projetos
    WHERE enviar_proposta = 1
    """)

    projetos = cursor.fetchall()

    conn.close()

    return projetos


# Marcar como enviado no Telegram
def marcar_como_enviado(projeto_id):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE projetos
    SET enviado_telegram = 1
    WHERE id = ?
    """, (projeto_id,))

    conn.commit()
    conn.close()


# Marcar para enviar proposta
def marcar_para_proposta(projeto_id):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE projetos
    SET enviar_proposta = 1
    WHERE id = ?
    """, (projeto_id,))

    conn.commit()
    conn.close()


# Listar todos projetos
def listar_projetos():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projetos")

    projetos = cursor.fetchall()

    conn.close()

    return projetos

import os

def projeto_existe(hash_id):

    base_dir = os.path.dirname(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, "data", "workana.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM projetos WHERE hash = ?",
        (hash_id,)
    )

    resultado = cursor.fetchone()

    conn.close()

    return resultado is not None

