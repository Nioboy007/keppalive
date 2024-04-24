from flask import Flask
from telegram.ext import Updater, CommandHandler

app = Flask(__name__)

# Replace "YOUR_BOT_TOKEN" with your actual Telegram bot token
updater = Updater(token="7168860212:AAFQ9gMveau8z9hoWdwA4HoqjC8dp7hFcHE", use_context=True)

# Define your Telegram bot handlers here
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your Telegram bot.")

updater.dispatcher.add_handler(CommandHandler('start', start))

# Define your keep-alive endpoint
@app.route('/keep-alive')
def keep_alive():
    return 'Bot is alive!'

if __name__ == '__main__':
    # Start the Telegram bot polling
    updater.start_polling()

    # Start the Flask app for the keep-alive endpoint
    app.run(debug=True)
