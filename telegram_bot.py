import telegram

def send_alert(msg):
    bot_token = 'your_bot_token'
    chat_id = 'your_chat_id'
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=msg)
