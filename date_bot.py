import datetime as dt
import time

import telebot
from telegram import ParseMode

import config

bot = telebot.TeleBot(config.TOKEN)

while True:
    current_time = dt.datetime.now().time().strftime('%H:%M:%S')  # Время опроса
    # Условие опроса в указанные часы будних рабочих дней
    bot.send_message(chat_id=config.TEST_CHAT_ID,
                     text=current_time,
                     parse_mode=ParseMode.HTML)
    time.sleep(config.TEST_DELAY)  # Ожидание 1 день до следующего опроса
