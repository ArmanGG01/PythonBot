from telegram import Update, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, CallbackContext, InlineQueryHandler
from telegram.inline.queryresult import InlineQueryResultArticle

TOKEN = "6315172994:AAE-nSTwK6xgewRkiybt2YGPvZ8kBZDzbrw"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Halo! Saya bot gabut.")

def options(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineQueryResultArticle(id="1", title="Opsi 1", input_message_content=InputTextMessageContent("Anda memilih opsi 1."))],
        [InlineQueryResultArticle(id="2", title="Opsi 2", input_message_content=InputTextMessageContent("Anda memilih opsi 2."))],
        [InlineQueryResultArticle(id="3", title="Opsi 3", input_message_content=InputTextMessageContent("Anda memilih opsi 3."))]
    ]
    update.inline_query.answer(keyboard)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("options", options))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
