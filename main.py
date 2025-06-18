import telebot
from telebot import types

bot = telebot.TeleBot("8028982090:AAFZcLixJ8lkAgohXugaou4kUal1skT1QZs")

@bot.message_handler(commands=['start'])
def start(message):
    markupMain = types.InlineKeyboardMarkup()
    markupMain.add(types.InlineKeyboardButton("Создать видео", callback_data="CreateVideoCallBack"))
    markupMain.add(types.InlineKeyboardButton("Аккаунты", callback_data="AccountsCallBack"))
    markupMain.add(types.InlineKeyboardButton("Просмотр видео", callback_data="WatchingCallBack"))
    bot.reply_to(message, "Добро пожаловать!", reply_markup=markupMain)

@bot.callback_query_handler(func=lambda callback: True)
def callBackHandler(callback):
    if callback.data == "CreateVideoCallBack":
        createVideoCallBackHandler(callback)

    elif callback.data == "AccountsCallBack":
        accountCallBackHanlder(callback)

    elif callback.data == "WatchingCallBack":
        watchingCallBackHandler(callback)

    else:
        print("CALLBACK ERROR")

def createVideoCallBackHandler(callback):
    #bot.send_message(callback.from_user.id, "Here will be creating of video by prompt")
    markupCreateVideo = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Stable AI")
    btn2 = types.KeyboardButton("Заглушка 1")
    btn3 = types.KeyboardButton("Заглушка 2")
    markupCreateVideo.row(btn1)
    markupCreateVideo.row(btn2, btn3)
    bot.send_message(callback.from_user.id, "Чё хочешь?", reply_markup=markupCreateVideo)

def accountCallBackHanlder(callback):
    bot.send_message(callback.from_user.id, "Here will be a list of accounts")

def watchingCallBackHandler(callback):
    bot.send_message(callback.from_user.id, "Here will be the panel with generated videoes")

bot.polling(none_stop=True, interval=0)

