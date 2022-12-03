import datetime as dt
import time
import locale
import holidays

import telebot
from pytz import timezone
from telegram import ParseMode

import config

bot = telebot.TeleBot(config.TOKEN)
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')  # Устанавливаем поддержку русского языка
next_day = dt.datetime.now(timezone(config.TIME_ZONE)) + dt.timedelta(1)
weekday_number = dt.datetime.now(timezone(config.TIME_ZONE)).weekday()  # Номер дня недели
next_weekday_name = next_day.strftime("%A").lower()  # Название завтрашнего дня недели
next_date = next_day.date()  # Завтрашняя дата
ru_holidays = holidays.RU()
base_url = config.SEND_POLL  # URL для отправки опроса

while True:
    try:
        current_time = dt.datetime.now(timezone(config.TIME_ZONE)).time().strftime('%H:%M:%S')  # Время опроса
        if (weekday_number in (0, 1, 2, 3, 4, 5, 6) or current_time == config.REPORT_TIME) and next_date not in ru_holidays:
            # Условие опроса в указанные часы будних рабочих дней
            bot.send_message(chat_id=config.TEST_CHAT_ID,
                             text=current_time,
                             parse_mode=ParseMode.HTML)
            time.sleep(config.TEST_DELAY)  # Ожидание 1 день до следующего опроса

    except Exception as e:
        print(e)
        time.sleep(15)