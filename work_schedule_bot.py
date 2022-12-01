import datetime as dt
import json
import locale
import time

import holidays
import requests
import telebot
from telegram import ParseMode

import config

bot = telebot.TeleBot(config.TOKEN)

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')  # Устанавливаем поддержку русского языка
next_day = dt.datetime.now() + dt.timedelta(1)
weekday_number = dt.datetime.now().weekday()  # Номер дня недели
next_weekday_name = next_day.strftime("%A").lower()  # Название завтрашнего дня недели
next_date = next_day.date()  # Завтрашняя дата
ru_holidays = holidays.RU()
base_url = config.SEND_POLL  # URL для отправки опроса

NEXT_DAY_NAME = {
    'понедельник': 'в понедельник',
    'вторник': 'во вторник',
    'среда': 'в среду',
    'четверг': 'в четверг',
    'пятница': 'в пятницу',
    'суббота': 'в субботу',
    'воскресенье': 'в воскресенье',
}

parameters = {
    'chat_id': config.DEVELOPMENT_CHAT_ID,
    'question': f'Завтра {next_date} {NEXT_DAY_NAME[next_weekday_name]}, я работаю:',
    'options': json.dumps([
        'Из офиса, полный рабочий день.',
        'Из офиса, первая половина дня.',
        'Из офиса, вторая половина дня.',
        'Удалённо.',
        'Завтра не работаю.',
    ]),
    'is_anonymous': False,
    'disable_notification': True,
}

while True:
    poll_time = dt.datetime.now().time().strftime('%H:%M:%S')  # Время опроса
    # Условие опроса в указанные часы будних рабочих дней
    if (weekday_number in (0, 1, 2, 3, 6) and poll_time == config.POLL_TIME) and next_date not in ru_holidays:
        requests.get(base_url, data=parameters)
        bot.send_message(chat_id=parameters.get('chat_id'),
                         text=config.DEVELOPMENT_MESSAGE,
                         parse_mode=ParseMode.HTML)
        time.sleep(config.POLL_DELAY)  # Ожидание 1 день до следующего опроса^