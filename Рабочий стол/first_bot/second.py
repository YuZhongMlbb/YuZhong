from config import S_TOKEN
from telebot import *
bot = TeleBot(S_TOKEN)
group = types.ReplyKeyboardMarkup(resize_keyboard=True)
group.row("наша группа", "о нас")

people = types.ReplyKeyboardMarkup(resize_keyboard=True)
people.row("Аннур", "Ширин", "Ламар")
people.row("Вернуться назад")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствую!", reply_markup=group)

@bot.message_handler(func=lambda message:True)
def second(message):
    if message.text == 'наша группа':
        bot.send_message(message.chat.id, "Наши участники: ", reply_markup=people)
    elif message.text == 'о нас':
        bot.send_message(message.chat.id, "Наш адрес: БЦ 'Олимп'")
    elif message.text == 'Аннур':
        bot.send_message(message.chat.id, "Рекомендация: не переоценивать")
    elif message.text == 'Ширин':
        bot.send_message(message.chat.id, "Учится в универе")
    elif message.text == 'Ламар':
        bot.send_message(message.chat.id, "Вода камень точит")
    elif message.text == 'Вернуться назад':
        bot.send_message(message.chat.id, "Назад...", reply_markup=group)

bot.polling(non_stop=True)