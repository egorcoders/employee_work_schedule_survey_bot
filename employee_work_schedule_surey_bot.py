import config
import datetime as dt
import json
import locale
import requests
import time

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')  # Устанавливаем поддержку русского языка

weekday_number = dt.datetime.now().weekday()  # Номер дня недели
weekday_name = dt.datetime.now().strftime("%A")  # Название дня недели
current_date = dt.datetime.now().date()  # Текущая дата

base_url = config.SEND_POLL  # URL для отправки опроса

parameters = {
    'chat_id': config.CHAT_ID,
    'question': f'{current_date} ({weekday_name}) я работаю:',
    'options': json.dumps([
        'Из офиса. Полный рабочий день.',
        'Из офиса. Первая половина дня.',
        'Из офиса. Вторая половина дня.',
        'Удалённо.',
        'Сегодня не работаю.',
    ]),
    'is_anonymous': False,
    'disable_notification': True,
}

while True:
    poll_time = dt.datetime.now().time().strftime('%H:%M:%S')  # Время опроса
    if weekday_number in range(6) and poll_time == config.POLL_TIME:  # Условие опроса в будние часы
        requests.get(base_url, data=parameters)
        time.sleep(config.POLL_DELAY)   # Ожидание 1 день до следующего опроса
