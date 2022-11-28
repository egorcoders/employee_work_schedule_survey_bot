import config
import datetime as dt
import json
import locale
import requests
import time

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

weekday_number = dt.datetime.now().weekday()
weekday_name = dt.datetime.now().strftime("%A")
current_date = dt.datetime.now().date()

base_url = config.SEND_POLL
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
    poll_time = dt.datetime.now().time().strftime('%H:%M:%S')
    if weekday_number in range(6) and poll_time == '09:00:00':
        resp = requests.get(base_url, data=parameters)
        print(resp.text, weekday_number)
        time.sleep(60 * 60 * 24)
