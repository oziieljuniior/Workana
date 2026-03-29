import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 1. Configuração de Logs (Importante para monitorar tentativas de acesso)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
# Adicione isso logo após carregar o logging.basicConfig
logging.getLogger("httpx").setLevel(logging.WARNING)

# 2. Carrega as variáveis de ambiente
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
# Converta para int, pois IDs do Telegram são numéricos
ALLOWED_GROUP_ID = int(os.getenv("GROUP_ID", 0)) 

# --- FUNÇÕES DE LÓGICA ---

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
    # Criamos apenas UMA instância da aplicação
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Handler para o comando /start
    application.add_handler(CommandHandler("start", start))
    
    # Handler para mensagens de texto (ignora comandos para não duplicar resposta)
    msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), filter_messages)
    application.add_handler(msg_handler)

    print("Bot iniciado e protegido por Chat ID...")
    application.run_polling()