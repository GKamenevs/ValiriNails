import telebot
from telebot import types

bot = telebot.TeleBot('6357571261:AAHvKGgD1XV6Mwf7oq2jC5WeiTmc8AUHiLo')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Записаться На Маникюр', callback_data='button1')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Отменить запись', callback_data='button2')
    markup.row(btn2)
    bot.send_message(message.chat.id, 'Приветсвую!\n'
                                      'Выберите пожалуйста услугу\n'
                                      'На которую Хотели бы записаться', reply_markup=markup)

@bot.callback_query_handler(func=lambda query: query.data == 'button1')
def button1_pressed(query):
    markup = types.InlineKeyboardMarkup()
    zps1 = types.InlineKeyboardButton('12.10 19.01', callback_data='button3')
    markup.row(zps1)
    zps2 = types.InlineKeyboardButton('12.10 19.00', callback_data='button4')
    markup.row(zps2)
    zps3 = types.InlineKeyboardButton('12.10 19.03', callback_data='button5')
    markup.row(zps3)
    zps4 = types.InlineKeyboardButton('12.10 19.04', callback_data='button6')
    markup.row(zps4)
    zps5 = types.InlineKeyboardButton('12.10 19.05', callback_data='button7')
    markup.row(zps5)
    bot.send_message(query.message.chat.id, 'Пожалуйста\nВыберите дату и время', reply_markup=markup)



@bot.callback_query_handler(func=lambda query: query.data == 'button2')
def button2_pressed(query):
    bot.send_message(query.message.chat.id, 'Выберите запись для отмены')
    markup = types.InlineKeyboardMarkup()
    otm1 = types.InlineKeyboardButton('12.10 19.01', callback_data='button8')
    markup.row(otm1)
    otm2 = types.InlineKeyboardButton('12.10 19.00', callback_data='button9')
    markup.row(otm2)
    otm3 = types.InlineKeyboardButton('12.10 19.03', callback_data='button0')
    markup.row(otm3)
    otm4 = types.InlineKeyboardButton('12.10 19.04', callback_data='button10')
    markup.row(otm4)
    otm5 = types.InlineKeyboardButton('12.10 19.05', callback_data='button11')
    markup.row(otm5)
    bot.send_message(query.message.chat.id, 'Пожалуйста\nВыберите дату и время', reply_markup=markup)






bot.polling(none_stop=True)
