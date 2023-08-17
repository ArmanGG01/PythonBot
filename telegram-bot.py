from teleram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

# Fungsi untuk menangani perintah /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Halo! Saya adalah bot gabut. Kirim pesan apa pun untuk berbincang.")

# Fungsi untuk menangani pesan masuk
def echo(update: Update, context: CallbackContext) -> None:
    responses = ["Haha iya", "Wah seru ya!", "Keren!", "Ngomong-ngomong, gimana kabarmu?"]
    response = random.choice(responses)
    update.message.reply_text(response)

def main() -> None:
    # Ganti TOKEN_BOT_ANDA dengan token bot yang Anda dapatkan dari BotFather di Telegram
    updater = Updater("6315172994:AAE-nSTwK6xgewRkiybt2YGPvZ8kBZDzbrw")

    dispatcher = updater.dispatcher

    # Menangani perintah /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Menangani pesan masuk
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Memulai polling untuk mendapatkan pesan masuk
    updater.start_polling()

    # Menjaga bot berjalan hingga Anda berhenti secara manual
    updater.idle()

if __name__ == '__main__':
    main()
