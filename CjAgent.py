import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import openai

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to your AI Content Agent. Type /idea or /caption to start.")

async def idea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args) or "reels for finance"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a social media strategist"},
            {"role": "user", "content": f"Give me 3 short video content ideas for {prompt}"}
        ]
    )
    ideas = response.choices[0].message.content
    await update.message.reply_text(f"🎥 Content ideas:\n\n{ideas}")

async def caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(context.args) or "money tips"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a creative Instagram content writer."},
            {"role": "user", "content": f"Write a fun Instagram caption with hashtags about {topic}"}
        ]
    )
    caption = response.choices[0].message.content
    await update.message.reply_text(f"📝 Caption:\n\n{caption}")

app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("idea", idea))
app.add_handler(CommandHandler("caption", caption))

app.run_polling()
