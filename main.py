import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import openai

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Get tokens from environment
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

async def start(update, context):
    await update.message.reply_text("Hello! I'm your AI Social Media Agent bot.")

async def help_command(update, context):
    await update.message.reply_text("Send me a message and I'll generate captions for your Instagram and YouTube posts.")

async def handle_message(update, context):
    user_text = update.message.text

    # Use OpenAI to generate a caption
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a catchy Instagram and YouTube caption for: {user_text}",
        max_tokens=50
    )
    caption = response.choices[0].text.strip()
    await update.message.reply_text(caption)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot started...")
    app.run_polling()

if __name__ == '__main__':
    main()
