import datetime as dt
import locale
import random
import time

import emoji
import holidays
import requests
import telebot
from pytz import timezone

import config

bot = telebot.TeleBot(config.TOKEN)
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')  # Устанавливаем поддержку русского языка
next_day = dt.datetime.now(timezone(config.TIME_ZONE)) + dt.timedelta(1)
weekday_number = dt.datetime.now(timezone(config.TIME_ZONE)).weekday()  # Номер дня недели
next_weekday_name = next_day.strftime("%A").lower()  # Название завтрашнего дня недели
next_date = next_day.date()  # Завтрашняя дата
ru_holidays = holidays.RU()
base_url = config.SEND_POLL  # URL для отправки опроса


def get_cat_url():
    data = requests.get(config.CAT_URL)
    j_data = data.json()[0]
    return j_data.get('url')


def get_phrase():
    question = [
        'Как спалось?',
        'Как ты спала?',
        'Как настроение?',
        'Что ты сегодня ела?',
        'Что ты с утра ела?',
        'Что ты сегодня кушала?',
        'Что ты с утра кушала?',
        'Как ты завтракала?',
        'Как на работе?',
        'Как тебе погода?',
        'Что тебе снилось?',
        'О чём думешь?',
        'А ты о чём думешь?',
        'Как сегодня твои коллеги?',
        'Как сегодня доехала?',
        'Что сегодня будешь делать?',
    ]

    phrase = [
        'Hi',
        'Good morning',
        'Привет',
        'С добрым утром',
        'Здравствуй',
        'Скучаю по тебе',
        'Думаю о тебе',
        'Скучаю',
    ]

    irchick = [
        'Ирчик',
        'Ирчик',
        'Ирчик',
        'Ирчик',
        'Ира',
        'Ира',
        'Ира',
        'Ира',
        'Ира',
        'моя девочка',
        'моя хорошая',
        'хорошая',
        'моя умная',
        'моя ласковая',
        'ласковая',
        'моя нежная',
        'нежная',
        'моя милая',
        'милая',
        'моя киска',
        'моя кошечка',
        'моя конфетка',
        'конфетка',
        'кифирчик',
    ]
    emoji_list = [
        ':smile:',
        ':blush:',
        ':relaxed:',
        ':heart_eyes:',
        ':kissing_closed_eyes:',
        ':relieved:',
        ':grinning:',
        ':kissing_smiling_eyes:',
        ':sleeping:',
        ':heart:',
        ':heartpulse:',
        ':revolving_hearts:',
        ':revolving_hearts:',
        ':sparkling_heart:',
        ':relieved:',
        ':star:',
        ':dizzy:',
        ':cupid:',
        ':sparkles:',
        ':star2:',
        ':two_hearts:',
        ':wink:',
        ':kissing_heart:',
        ':smiley:',
        ':smiley:',
        ':smiley_cat:',
        ':smirk_cat:',
        ':heart_eyes_cat:',
        ':smile_cat:',
        ':joy_cat:',
    ]

    random_emoji = random.choice(emoji_list)

    return (f'{random.choice(phrase)}, '
            f'{random.choice(irchick)} '
            f'{emoji.emojize(random_emoji, variant="emoji_type", language="alias")} '
            f'{random.choice(question)}')


while True:
    try:
        current_time = dt.datetime.now(timezone(config.TIME_ZONE)).time().strftime('%H:%M:%S')  # Время опроса
        if current_time == config.CAT_BOT_TIME:
            # Условие опроса в указанные часы будних рабочих дней
            bot.send_photo(chat_id=config.TEST_CHAT_ID, photo=get_cat_url(), caption=get_phrase())
            time.sleep(10)  # Ожидание 1 день до следующего опроса

    except Exception as e:
        print(e)
        time.sleep(15)
