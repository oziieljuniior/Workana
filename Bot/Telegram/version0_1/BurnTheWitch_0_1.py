"""
    Organização do bot para envio de propostas no grupo do Telegram.
    O bot é responsável por enviar as propostas para o grupo do Telegram, utilizando a API do Telegram
"""

import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import sqlite3
from pathlib import Path
import pandas as pd
import time
import subprocess
import sys
import asyncio

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
from databaseFiltrado import atualizar_projetos_filtrados



# 1. Configuração de Logs (Importante para monitorar tentativas de acesso)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
# Adicione isso logo após carregar o logging.basicConfig
logging.getLogger("httpx").setLevel(logging.WARNING)

# 2. Carrega as variáveis de ambiente
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN_0_1")
# Converta para int, pois IDs do Telegram são numéricos
ALLOWED_GROUP_ID = int(os.getenv("GROUP_ID", 0)) 
DATABASE_PATH = Path(os.getenv("DATABASE_PATH_0_1"))

# --- FUNÇÕES DE LÓGICA ---
## Consulta e processamento de dados
def process_data():
    """
    Função para processar os dados do banco de dados SQLite e retornar um DataFrame.

    Returns:
        df: retorna um DataFrame com os dados processados do banco de dados SQLite.
    """

    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    # Ver tabelas do banco
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())

    df = pd.read_sql("SELECT * FROM projetos", conn)
    conn.close()
    return df

def listar_titulos(df):
    """
    Função para listar os títulos dos projetos a partir do DataFrame.

    Args:
        df: DataFrame contendo os dados dos projetos.

    Returns:
        list: Lista de títulos dos projetos.
    """
    return df['titulo'].tolist()

## TELEGRAM BOT
async def pipeline(context: ContextTypes.DEFAULT_TYPE):

    print("Executando pipeline:", time.strftime("%Y-%m-%d %H:%M:%S"))

    atualizar_projetos_filtrados()

    conn = sqlite3.connect(DATABASE_PATH)

    df = pd.read_sql("""
        SELECT *
        FROM projetos_filtrados
        WHERE enviado_telegram = 0
    """, conn)

    for _, row in df.iterrows():

        titulo = row['titulo']
        link = row['link']
        hash_id = row['hash_id']
        date = row['data_coleta']

        message = f"""
🚀 Novo Projeto: 📅 {date}

📂 {row['categoria']}

📌 {titulo}

🔗 {link}

"""
    
        await context.bot.send_message(
            chat_id=ALLOWED_GROUP_ID,
            text=message
        )

        # Delay anti flood
        await asyncio.sleep(30)

        conn.execute("""
            UPDATE projetos_filtrados
            SET enviado_telegram = 1
            WHERE hash_id = ?
        """, (hash_id,))

    conn.commit()
    conn.close()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde ao comando /start apenas se estiver no grupo correto."""
    if update.effective_chat.id != ALLOWED_GROUP_ID:
        print(f"Comando /start negado para: {update.effective_chat.id}")
        return
    
    await update.message.reply_text("Olá! Eu sou seu bot de estudos.")

async def filter_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processa mensagens de texto apenas se o chat for autorizado."""
    if update.effective_chat.id != ALLOWED_GROUP_ID:
        print(f"Mensagem negada para o Chat: {update.effective_chat.id}")
        return

    # Sua lógica de processamento aqui
    await update.message.reply_text("Processando informação no grupo autorizado...")

# --- EXECUÇÃO DO BOT ---

if __name__ == '__main__':

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    msg_handler = MessageHandler(
        filters.TEXT & (~filters.COMMAND),
        filter_messages
    )

    application.add_handler(msg_handler)

    # Pipeline automática
    job_queue = application.job_queue

    job_queue.run_repeating(
        pipeline,
        interval=1800,
        first=10
    )

    print("Bot iniciado e protegido por Chat ID...")
    application.run_polling()