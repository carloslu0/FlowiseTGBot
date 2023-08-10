import os
import requests
import telebot

API_KEY = os.getenv('TELEGRAM_TOKEN')  # Fetching the Telegram Bot Token from the environment variable
bot = telebot.TeleBot(API_KEY)

API_URL = "https://flowise-08rv.onrender.com/api/v1/prediction/41558f0b-7293-4b9b-ba82-7ca6e6ede503"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

@bot.message_handler(func=lambda msg: msg.entities is not None and any(
    entity.type == 'mention' for entity in msg.entities))
def echo_all(message):
    if '@flowise_fennec_bot' in message.text:
        msg = message.text.replace('@flowise_fennec_bot', '').strip()
        api_response = query({"question": msg})
        bot.reply_to(message, '{}'.format(api_response))

bot.polling()
