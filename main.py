import telebot
from datetime import datetime, date, time
from telebot import types

bot = telebot.TeleBot('5210659967:AAG4-LwoXi81I9gfpx3emjJYwYt-cfWGWD0')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Hello <b>{message.from_user.first_name}</b>,\ntype /cat to see the status of your cat"
    bot.send_message(message.chat.id, mess, parse_mode='html')
    #markup = types.InlineKeyboardMarkup()
    #markup.add(types.InlineKeyboardButton('See your cat'))
    #bot.send_message(message.chat.id, reply_markup=markup)
    #photo = open('image.jpg', 'rb')
    #bot.send_photo(message.chat.id, photo, reply_markup=markup)

@bot.message_handler(commands=['cat'])
def cat(message):
    #markup = types.InlineKeyboardMarkup()
    #markup.add(types.InlineKeyboardButton("See your cat", url="https://ya.ru"))
    bot.send_message(message.chat.id, f'<u>Last update</u>', parse_mode='html')
    file_time = open('time.txt', 'r')
    text_time = file_time.readline()
    bot.send_message(message.chat.id, text_time)
    bot.send_message(message.chat.id, '<u>Your cat status</u>', parse_mode='html')
    file = open('status.txt', 'r')
    text_status = file.readline()
    bot.send_message(message.chat.id, text_status)
    photo = open('image.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)



#@bot.message_handler(content_types=['text'])
#def get_user_text(message):
#    # print info about user and message
#    #bot.send_message(message.chat.id, message, parse_mode='html')
#    if message.text == 'Hello':
#        bot.send_message(message.chat.id, 'Hey!', parse_mode='html')
#    elif message.text == 'Id':
#        bot.send_message(message.chat.id, f'Your id is {message.from_user.id}', parse_mode='html')
#    elif message.text == 'photo':
#        photo = open('image.jpg', 'rb')
#        bot.send_photo(message.chat.id, photo)
#    else:
#        bot.send_message(message.chat.id, 'Do not understand you', parse_mode='html')

@bot.message_handler(commands=['set_status'])
def set_status(message):
    print('message.text =', message.text)
    sent = bot.send_message(message.chat.id, 'Input status')
    bot.register_next_step_handler(sent, input_status)
    #with open("status.txt", 'w') as status_file:
    #    status_file.write(message.text)
    #bot.send_message(message.chat.id, 'Status received')

def input_status(message):
    file = open('status.txt', 'w')
    file.write(message.text)
    file.close()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    time_file = open('time.txt', 'w')
    time_file.write(dt_string)
    bot.send_message(message.chat.id, 'Status received')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    print('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, 'Photo received')



bot.polling(none_stop=True)