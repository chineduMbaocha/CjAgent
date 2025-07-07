import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import openai

# Load tokens from environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I'm your bot. How can I help you?")

def main():
    if TELEGRAM_TOKEN is None or OPENAI_API_KEY is None:
        print("Error: Missing TELEGRAM_BOT_TOKEN or OPENAI_API_KEY environment variables.")
        return

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is starting...")
    app.run_polling()

if __name__ == '__main__':
    main()
