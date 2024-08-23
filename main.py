from telebot import TeleBot, types

import config
import messages

bot = TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def handle_command_start(message: types.Message):
    bot.send_message(
        message.chat.id,
        messages.HELLO,
    )

@bot.message_handler(commands=['help'])
def handle_command_help(message: types.Message):
    bot.send_message(
        message.chat.id,
        messages.HELP_MESSAGES,
    )

@bot.message_handler(commands=['goncharov'])
def handle_command_goncharov(message: types.Message):
    bot.send_photo(
        chat_id=message.chat.id,
        photo=config.GONCHAROV_URL,
    )

@bot.message_handler()
def only_cultural_message(message: types.Message):
    text = message.text
    if 'дур' in text.lower():
        text = "Коллеги, ну мы же работники культуры! Не сквернословьте."
    else:
        text = ''
    bot.send_message(
        message.chat.id, 
        text,
    )

def is_Goncharov_on_photo(message: types.Message):
    return message.caption and 'гончаров' in message.caption.lower()

@bot.message_handler(content_types=['photo'], func=is_Goncharov_on_photo)
def handle_photo_with_Goncharov_caption(message: types.Message):
    bot.send_message(
        chat_id = message.chat.id,
        text = messages.GONCHAROV_DISCRIPTION
    )

@bot.message_handler(content_types=['photo'])
def handle_photo(message: types.Message):
    photo_file_id = message.photo[-1].file_id
    bot.send_photo(
        message.chat.id,
        photo = photo_file_id,
        reply_to_message_id=message.id,
    )

if __name__ == '__main__':
    bot.infinity_polling(skip_pending=True)

