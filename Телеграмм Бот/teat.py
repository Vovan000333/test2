import telebot
from telebot import types  # для указание типов

bot = telebot.TeleBot("6254716733:AAFzMlNY1MrCclRCXTpIWkI2E1BYnEo7zNE")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
    elif (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)

import telebot

# Создаем бота с указанным токеном
bot = telebot.TeleBot('6254716733:AAFzMlNY1MrCclRCXTpIWkI2E1BYnEo7zNE')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Welcome to the Calculator bot! Enter your arithmetic expression to evaluate:")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def calculate_handler(message):
    try:
        # Пытаемся вычислить арифметическое выражение
        result = eval(message.text)

        # Отправляем ответ пользователю
        bot.send_message(message.chat.id, "Result: {}".format(result))
    except:
        # Если вычислить арифметическое выражение не удалось
        bot.send_message(message.chat.id, "Error: Invalid input")

# Запускаем бота
bot.polling()

print("приветмир"
      "")
if x = 5:


