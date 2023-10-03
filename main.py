import telebot
from telebot import types

bot = telebot.TeleBot('6357571261:AAHvKGgD1XV6Mwf7oq2jC5WeiTmc8AUHiLo')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Записаться', callback_data='button1')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Отменить запись', callback_data='button2')
    markup.row(btn2)
    bot.send_message(message.chat.id, 'Приветсвую!\n'
                                      'Выберите пожалуйста услугу\n'
                                      'На которую Хотели бы записаться', reply_markup=markup)

@bot.callback_query_handler(func=lambda query: query.data == 'button1')
def button1_pressed(query):






bot.polling(none_stop=True)
