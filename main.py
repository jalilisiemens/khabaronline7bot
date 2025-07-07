import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = "7543398711:AAGAxCgQVKr1GWWR5d7pxrdw1TiG31lHbsA"
TARGET_CHANNEL = "@khabaronline77"

SOURCE_CHANNELS = [
    "@ProxyDotNet",
    "@gizmiztel",
    "@serfan_jahate_ettela",
    "@uniquegoldd",
    "@sirnews2"
]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.username
    if chat_id and ("@" + chat_id) in SOURCE_CHANNELS:
        message = update.message
        await context.bot.copy_message(
            chat_id=TARGET_CHANNEL,
            from_chat_id=update.effective_chat.id,
            message_id=message.message_id
        )
        logger.info(f"پیام از {chat_id} به {TARGET_CHANNEL} کپی شد.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    source_filters = filters.Chat(username=SOURCE_CHANNELS)
    app.add_handler(MessageHandler(source_filters, forward_message))
    print("ربات اجرا شد...")
    app.run_polling()

if __name__ == '__main__':
    main()
