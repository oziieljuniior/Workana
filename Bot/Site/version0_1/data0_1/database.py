import sqlite3
import os
from pathlib import Path
import dotenv

# Carrega as variáveis de ambiente
dotenv.load_dotenv()
DB_PATH = Path(os.getenv("DATABASE_PATH_0_1"))

def criar_banco():
    """Cria a tabela se ela não existir. 
    Se você mudou a estrutura (adicionou colunas), apague o arquivo .db manualmete uma vez."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hash TEXT UNIQUE,
        categoria TEXT,
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
    categoria,
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
    """Insere os dados no banco. 
    Note que a quantidade de '?' deve ser EXATAMENTE igual à quantidade de colunas e valores."""
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # 10 colunas listadas = 10 interrogações (?)
        cursor.execute("""
        INSERT OR IGNORE INTO projetos 
        (
            hash,
            categoria,
            titulo,
            link,
            descricao,
            cliente_verificado,
            cliente_pagamento_verificado,
            cliente_historico,
            enviar_proposta,
            enviado_telegram
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            hash_id,
            categoria,
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
        print(f"Erro ao salvar projeto: {e}")

    finally:
        conn.close()


def projeto_existe(hash_id):
    """Verifica se o hash já está no banco para evitar duplicatas."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM projetos WHERE hash = ?",
        (hash_id,)
    )

    resultado = cursor.fetchone()
    conn.close()

    return resultado is not None
