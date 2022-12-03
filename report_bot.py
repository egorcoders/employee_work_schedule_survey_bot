import datetime as dt
import locale
import time

import holidays
import telebot
from pytz import timezone
from telegram import ParseMode

import config

bot = telebot.TeleBot(config.TOKEN, threaded=False)

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')  # Устанавливаем поддержку русского языка
next_day = dt.datetime.now(timezone(config.TIME_ZONE)) + dt.timedelta(1)
weekday_number = dt.datetime.now(timezone(config.TIME_ZONE)).weekday()  # Номер дня недели
next_weekday_name = next_day.strftime("%A")  # Название завтрашнего дня недели
next_date = next_day.date()  # Завтрашняя дата
ru_holidays = holidays.RU()

while True:
    try:
        current_time = dt.datetime.now(timezone(config.TIME_ZONE)).time().strftime('%H:%M:%S')  # Время опроса
        # Условие опроса в указанные часы будних рабочих дней
        if (weekday_number in (0, 1, 2, 3, 4) and current_time == config.REPORT_TIME) and next_date not in ru_holidays:
            bot.send_message(chat_id=config.TEST_CHAT_ID,
                             text=config.DREAM_TEAM_MESSAGE,
                             parse_mode=ParseMode.HTML)
            time.sleep(config.POLL_DELAY)  # Ожидание 1 день до следующего опроса^

    except Exception as e:
        print(e)  # или просто print(e) если у вас логгера нет,
        time.sleep(15)
