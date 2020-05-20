import telebot
#from telebot import apihelper
from telebot import types
import numpy as np

#ip = '5.133.207.84'
#port = '4353'

#telebot.apihelper.proxy = {
#  'https': 'socks5://{}:{}'.format(ip,port)
#}

bot = telebot.TeleBot('1043358537:AAEieO3jHbk9hI6KS7aMKe7GtV3Y2Fu4Nrg')

markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
markup.row('Да или нет', '1 или 0')
markup.row('Красное или белое')
markup_off = types.ReplyKeyboardRemove()
markup_force = types.ForceReply()

#@bot.message_handler(regexp='жир')
#def fat(message):
#    bot.send_message(message.chat.id, 'Твою маму ебал, паскуда!', reply_markup = markup_force)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Стартуем')

@bot.message_handler(regexp='Сладких снов, котик\)')
def goodnight(message):
    bot.send_message(message.chat.id, 'Спокойной ночи, котик)')

@bot.message_handler(regexp='пиздец')
def goodnight(message):
    bot.send_message(message.chat.id, 'Ты самый лучший котик в целом мире)')
    
#@bot.message_handler(regexp='а что')
#def google(message):
#    keyboard = types.InlineKeyboardMarkup()
#    url_button = types.InlineKeyboardButton(text = 'Тебя что, в гугле забанили?', url='http://google.com')
#    url_button2 = types.InlineKeyboardButton(text = 'Не грусти, пупсик, послушай музыку', url='https://music.yandex.ru/home')
#    keyboard.add(url_button, url_button2)
#    bot.send_message(message.chat.id, 'Нажимай', reply_markup = keyboard)

@bot.message_handler(regexp = '1 или 0')
def onenil(message):
    bot.send_message(message.chat.id, np.random.randint(0,2), reply_markup=markup_off)

@bot.message_handler(regexp = 'Красное или белое')
def onenil(message):
    bot.send_message(message.chat.id, np.random.choice(['Красное','Белое'], p=[0.4,0.6]), reply_markup=markup_off)    

@bot.message_handler(regexp = 'Да или нет')
def onenil(message):
    bot.send_message(message.chat.id, np.random.choice(['Да','Нет', 'Совершенно точно нет, вот просто нет! Даже не думай пользоваться обратным выбором'], p=[0.495,0.495,0.01]), reply_markup=markup_off) 

#@bot.message_handler(content_types=['text'])
#def game(message):
#    bot.send_message(message.chat.id, 'Ты котик) Всё будет хорошо)')

@bot.message_handler(content_types=['text'])
def game(message):
    bot.send_message(message.chat.id, 'Выбирайте, мадам:', reply_markup = markup)
#    with open('log_bot.txt', 'a') as file:
#            file.write('Пользователь {} что-то отправлял\n'.format(message.from_user.username))

bot.polling(none_stop = True)
#bot.infinity_polling()
