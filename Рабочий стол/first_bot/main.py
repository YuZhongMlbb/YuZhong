from telebot import *
from config import TOKEN
bot = TeleBot(TOKEN)
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("супы", "горячие блюда")
menu.row("десерты", "напитки")

dish = types.ReplyKeyboardMarkup(resize_keyboard=True)
dish.row('Блюдо 1', 'Блюдо 2', 'Блюдо 3')
dish.row("Вернуться в меню")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в кафе 'У Аннура' наше электронное меню", reply_markup=menu)

@bot.message_handler(func=lambda message:True)
def second(message):
    if message.text == 'супы':
        bot.send_message(message.chat.id, "Выюерите суп: ", reply_markup=dish)
    elif message.text == 'горячие блюда':
        bot.send_message(message.chat.id, "Выберите горячее блюдо: ", reply_markup=dish)
    elif message.text == 'десерты':
        bot.send_message(message.chat.id, "Выюерите десерт", reply_markup=dish)
    elif message.text == 'напитки':
        bot.send_message(message.chat.id, "Выберите напиток: ", reply_markup=dish)
    elif message.text == "Вернуться в меню":
        bot.send_message(message.chat.id, f"Наше меню", reply_markup=menu)
    elif message.text in ['Блюдо 1', 'Блюдо 2', 'Блюдо 3']:
        bot.send_message(message.chat.id, f"Вы выбрали {message.text}")
bot.polling(non_stop=True)
