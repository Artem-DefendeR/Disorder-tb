import telebot
from telebot import types

bot = telebot.TeleBot('1167320556:AAGfNWvYtKMz4Hyjn2O7Qv8eWQkQ0FwMpxs')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items1 = types.KeyboardButton("Информация")
    items2 = types.KeyboardButton("Сервера")
    markup.add(items1, items2)
    bot.send_message(message.chat.id, "Привет это официальный бот серверов Disorder, выбери что тебя интересует",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def button(message):
    if message.text == "Информация":
        bot.send_message(message.chat.id, "Основная наша цель - привлечь больший интерес к Киберспорту. Играйте на "
                                          "наших "
                                          "серверах, повышайте скилл и участвуйте в турнирах во всех игровых "
                                          "дисциплинах. "
                                          "Побеждайте и вы не останетесь равнодушными! ")
        bot.send_message(message.chat.id, "У нас есть всё для комфортной игры:\n1)Грамотные и справедливые "
                                          "администраторы. "
                                          "\n2)Профессиональное оборудование для приятной игры: \nCore i9 9900K "
                                          "OC\n"
                                          "Overclocked 5 Ghz Liquid Cooling 2 GB 30 GB NVME \n3)Присоединиться и "
                                          "проявить "
                                          "себя может любой человек достигший 14 лет.")
    elif message.text == "Пидор":
        bot.send_message(message.chat.id, "Сам пидор")
    elif message.text == "Сервера":
        bot.send_message(message.chat.id, "Паблик: 62.122.213.59:1337")
        bot.send_message(message.chat.id, "HSDM: 212.22.93.196:27030")
    else:
        bot.send_message(message.chat.id, "я не понима что вы пишите", message.text)


bot.polling()
