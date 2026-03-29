import sqlite3
import dotenv
import os
from pathlib import Path
import pandas as pd


dotenv.load_dotenv()
DB_PATH = Path(os.getenv("DATABASE_PATH"))


def criar_tabela_projetos_filtrados():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projetos_filtrados (
            id INTEGER PRIMARY KEY,
            hash_id TEXT UNIQUE,
            titulo TEXT,
            link TEXT UNIQUE,
            descricao TEXT,
            cliente_verificado BOOLEAN,
            cliente_pagamento_verificado BOOLEAN,
            cliente_historico TEXT,
            enviar_proposta BOOLEAN DEFAULT 1,
            enviado_telegram BOOLEAN DEFAULT 0,
            data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def atualizar_projetos_filtrados():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql("SELECT * FROM projetos", conn)

    # Filtro válido
    filtro_valido = (
        (df['cliente_pagamento_verificado'] != 0) |
        (df['cliente_historico'] != '')
    ) & (df['enviar_proposta'] != 1)

    df_final = df[filtro_valido].reset_index(drop=True)

    for _, row in df_final.iterrows():

        try:

            conn.execute("""
                INSERT INTO projetos_filtrados (
                    id,
                    hash_id,
                    titulo,
                    link,
                    descricao,
                    cliente_verificado,
                    cliente_pagamento_verificado,
                    cliente_historico,
                    enviar_proposta,
                    enviado_telegram,
                    data_coleta
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row['id'],
                row["hash"],
                row["titulo"],
                row["link"],
                row["descricao"],
                row["cliente_verificado"],
                row["cliente_pagamento_verificado"],
                row["cliente_historico"],
                1,  # enviar_proposta
                row.get("enviado_telegram", 0),
                row.get("data_coleta", None)
            ))


            # Atualizar tabela original
            conn.execute("""
                UPDATE projetos
                SET enviar_proposta = 1
                WHERE hash = ?
            """, (row["hash"],))

        except sqlite3.IntegrityError:
            pass

    conn.commit()
    conn.close()
