import telebot
import datetime
import time
import threading
import random


bot = telebot.TeleBot('Введите токен')


@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать напоминать о воде\n"
        "/help - Какие команды есть\n"
        "/fact - Интересный факт о воде\n"
        "/double - Удвоить число. Используй: /double <число>\n"
        "/square - Возвести в квадрат. Используй: /square <число>\n"
    )
    bot.reply_to(message, help_text)


@bot.message_handler(commands=['double'])
def double_message(message):
    try:
        number = message.text.split()[1]
        number = float(number)
        double_number = number * 2

        response = f"Ответ: {double_number}"
    except ValueError as e:
        response = "Пожалуйста, введите корректное число после команды /square."
    except Exception as e:
        response = "Произошла ошибка. Пожалуйста, попробуйте снова."

    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['square'])
def square_message(message):
    try:
        number = message.text.split()[1]
        number = float(number)
        square_number = number ** 2

        response = f"Ответ: {square_number}"
    except ValueError as e:
        response = "Пожалуйста, введите корректное число после команды /square."
    except Exception as e:
        response = "Произошла ошибка. Пожалуйста, попробуйте снова."

    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет тебе напоминать пить воду')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()


@bot.message_handler(commands=['fact'])
def fact_message(message):
    listm = [
        "**Тройное состояние воды**: Вода — одно из немногих веществ на Земле, которое может существовать в трех состояниях (жидком, твердом и газообразном) при естественных температурах. При определенных условиях температуры и давления вода может существовать в этих трех состояниях одновременно, что называется тройной точкой.",
        "**Замерзание и расширение**: В отличие от большинства веществ, вода расширяется при замерзании. Это связано с уникальной структурой льда, где молекулы воды образуют кристаллическую решетку, которая занимает больше места, чем в жидком состоянии. Это свойство позволяет льду плавать на поверхности воды, что играет важную роль в поддержании жизни в водоемах в холодных климатах.",
        "**Вода как растворитель**: Вода известна как «универсальный растворитель» из-за своей способности растворять многие вещества. Это связано с полярностью молекул воды, которая позволяет им взаимодействовать с ионами и другими полярными молекулами, способствуя химическим реакциям и транспортировке веществ в биологических системах. Например, большинство процессов в организме человека, таких как обмен веществ и транспортировка питательных веществ, зависят от растворимости веществ в воде."
    ]

    random_fact = random.choice(listm)
    bot.reply_to(message, f'Лови инетересный факт о воде: {random_fact}')


def send_reminders(chat_id):
    wakeup_rem = "6:30"
    fitness_rem = "16:42"
    first_rem = "09:00"
    second_rem = "14:00"
    end_rem = "18:00"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == wakeup_rem:
            bot.send_message(chat_id, "Просыпайся")
            time.sleep(61)
        if now == fitness_rem:
            bot.send_message(chat_id, "Время зарядки")
            time.sleep(61)
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Напоминание - выпей стакан воды")
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True)
