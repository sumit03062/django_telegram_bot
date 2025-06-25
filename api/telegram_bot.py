from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from django.conf import settings
from .models import TelegramUser

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username
    TelegramUser.objects.get_or_create(telegram_username=username)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {username}, you are registered!")

def run_bot():
    app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
