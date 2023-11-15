from telebot import types,telebot

bot = telebot.TeleBot("...")  # В скобках нужно ввести токен бота

db = {'ФИО': 'Кулеш Дмитрий',
      'Адрес':'Каруселева 47',
      'Работа':'Нету'
}

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ФИО")
    item2 = types.KeyboardButton("Адрес")
    item3 = types.KeyboardButton("Работа")

    markup.add(item1)   # Вывод кнопок для пользователю
    markup.add(item2)
    markup.add(item3)

    bot.send_message(m.chat.id, f'Здравствуйте, что вас интересует?', reply_markup=markup)  # m - переменная в начале(m - от слова message)

@bot.message_handler(content_types=["text"])
def handle_text(message):

    if message.text.strip() == 'ФИО':
        answer = db['ФИО']
    elif message.text.strip() == 'Адрес':
        answer = db['Адрес']
    elif message.text.strip() == 'Работа':
        answer = db['Работа']
    else:
        answer = 'Такой команды нет'

    bot.send_message(message.chat.id, answer)

    #
bot.polling(none_stop=True,interval=0) # Чтобы бот работал всегда