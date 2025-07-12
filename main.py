from API import API
import telebot
from telebot import types

import API.model

bot = telebot.TeleBot("8028982090:AAFZcLixJ8lkAgohXugaou4kUal1skT1QZs")

#userId = 0

@bot.message_handler(commands=['start'])
def start(message):

    #Init userID
    #userId = message.from_user.id

    markupMain = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Создать видео", callback_data="CreateVideoCallBack")
    btn2 = types.InlineKeyboardButton("Аккаунты", callback_data="AccountsCallBack")
    btn3 = types.InlineKeyboardButton("Просмотр видео", callback_data="WatchingCallBack")
    markupMain.row(btn1, btn3)
    markupMain.row(btn2)
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


createVideoCBStates = {}
def createVideoCallBackHandler(callback):

    #bot.send_message(callback.from_user.id, "Here will be creating of video by prompt")
    userId = callback.from_user.id
    createVideoCBStates[userId] = "WaitingTheOption"

    markupCreateVideo = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("/Stable_AI")
    btn2 = types.KeyboardButton("Заглушка 1")
    btn3 = types.KeyboardButton("Заглушка 2")
    markupCreateVideo.row(btn1)
    markupCreateVideo.row(btn2, btn3)

    bot.send_message(userId, "Выберите нейронку для генерации видео:", reply_markup=markupCreateVideo)

@bot.message_handler(commands=['Stable_AI'])
def stableAIHandler(message):

    userId = message.from_user.id

    if createVideoCBStates[userId] == "WaitingTheOption":

        createVideoCBStates[userId] = "WaitingPrompt"
        bot.reply_to(message, "Введите промпт:")

    elif createVideoCBStates[userId] == "WaitingPrompt":

        createVideoCBStates[userId] = "WaitingResponse"
        prompt = message.text

        stableAI = API.StableAI(prompt)
        stableAI.reqToGen()
        stableAI.respToGen()

    else:
        print("Something went wrong on handling stableAI generator")




accountsStates = {}
def accountCallBackHanlder(callback):

    userId = callback.from_user.id
    accountStates[userId] = "WaitingTheOption"

    markupAccounts = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("/AddAccount")
    btn2 = types.KeyboardButton("/ViewAccountsList")
    btn3 = types.KeyboardButton("?Создать аккаунт?")
    btn4 = types.KeyboardButton("?Выбрать аккаунт?")
    markupAccounts.row(btn1, btn2)
    markupAccounts.row(btn3, btn4)

    bot.send_message(userId, "Настройка аккаунтов:", reply_markup=markupAccounts)

@bot.message_handler(commands=['AddAccount'])
def addingAccountHandler(message):

    if accountsStates[message.from_user.id] == "WaitingTheOption":
        markupAccount = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("<<", callback_data="CreateVideoCallBack")
        btn2 = types.InlineKeyboardButton("Аккаунты", callback_data="AccountsCallBack")
        btn3 = types.InlineKeyboardButton(">>", callback_data="WatchingCallBack")
        markupMain.row(btn1, btn3)
        markupMain.row(btn2)
        bot.reply_to(message, "Добро пожаловать!", reply_markup=markupMain)


def watchingCallBackHandler(callback):
    bot.send_message(callback.from_user.id, "Here will be the panel with generated videoes")

bot.polling(none_stop=True, interval=0)

