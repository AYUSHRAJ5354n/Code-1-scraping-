from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot is running!')

def main():
    updater = Updater("7103487326:AAFBaGo96RkepaOyx5KPPjv27Irjr30q9ik")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    # Add more command handlers for other features
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
