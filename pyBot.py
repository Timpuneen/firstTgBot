import telebot as tbot
import config

bot = tbot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
