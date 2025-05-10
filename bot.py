import os
import telebot
from telebot import types

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

def main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Узнать кто представитель клуба КГЖ")
    markup.add("Подписаться на соцсети представителя")
    markup.add("Поддержать представителя в голосовании")
    bot.send_message(chat_id, "Добрый день! Я помощник Клуба Городского Жителя — сокращенно КГЖ. Выбери один из 3-х пунктов", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Начать")
    bot.send_message(message.chat.id, "Нажми кнопку 'Начать'", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Начать")
def handle_start_button(message):
    main_menu(message.chat.id)

@bot.message_handler(func=lambda m: m.text == "Узнать кто представитель клуба КГЖ")
def handle_find_representative(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Не знаю")
    bot.send_message(message.chat.id, "Напиши номер своего избирательного округа (от 1 до 36)", reply_markup=markup)

districts = {
    "1": ("Павел Александрович Цуканов", "https://vk.com/pavel.tsukanov48"),
    "2": ("Сергей Васильевич Сазонов", "https://vk.com/svsazonov"),
    "3": ("Олег Владимирович Косолапов", "https://vk.com/id597083208"),
    "4": ("Василий Алексеевич Литовкин", "https://vk.com/id714688672"),
    "5": ("Анна Валерьевна Широких", "https://vk.com/id352507585"),
    "6": ("Вадим Николаевич Негробов", "https://vk.com/id288778777"),
    "7": ("Кирилл Викторович Иванов", "https://vk.com/ivanov_kb"),
    "8": ("Юрий Анатольевич Шкарин", "https://vk.com/id565972891"),
    "9": ("Михаил Юрьевич Русаков", "https://vk.com/mikhaelrusakov"),
    "10": ("Артем Николаевич Голощапов", "https://vk.com/a.goloshchapov"),
    "11": ("Андрей Викторович Выжанов", "https://vk.com/avyzhanov"),
    "12": ("Евгения Вальерьевна Фрай", "https://vk.com/evgenyafrai"),
    "13": ("Сергей Викторович Попов", "https://vk.com/id917351362"),
    "14": ("Станислав Алексеевич Полосин", "https://vk.com/stanislavpolosin48"),
    "15": ("Екатерина Алексеевна Пинаева", "https://vk.com/pinaeva_ea"),
    "16": ("Вера Ивановна Урываева", "https://vk.com/urivaevavi"),
    "17": ("Глеб Игоревич Гутевич", "https://vk.com/id1037188881"),
    "18": ("Игорь Николаевич Подзоров", "https://vk.com/inpodzorov"),
    "19": ("Евгений Сергеевич Колесников", ""),
    "20": ("Алексей Иванович Поляков", ""),
    "21": ("Павел Викторович Рухлин", "https://vk.com/pavelrukhlin"),
    "22": ("Елена Александровна Есина", "https://vk.com/id156008190"),
    "23": ("Игорь Александрович Катасонов", "https://vk.com/id1038206450"),
    "24": ("Андрей Владимирович Огородников", ""),
    "25": ("Галина Николаевна Селина", ""),
    "26": ("Алина Евгеньевна Теперик", "https://vk.com/malinateperik"),
    "27": ("Владислав Александрович Аленин", "https://vk.com/id1043676620"),
    "28": ("Дмитрий Анатольевич Гладышев", "https://vk.com/id152531671"),
    "29": ("Дмитрий Николаевич Погорелов", "https://vk.com/id596326492"),
    "30": ("Андрей Викторович Иголкин", "https://vk.com/igolkin83"),
    "31": ("Андрей Васильевич Бугаков", "https://vk.com/id132130001"),
    "32": ("Станислав Геннадьевич Каменецкий", "https://vk.com/id301354842"),
    "33": ("Борис Владимирович Понаморев", "https://vk.com/okrug33"),
    "34": ("Татьяна Сергеевна Шипилова", "https://vk.com/kaverinats"),
    "35": ("Александр Семёнович Перевозчиков", "https://vk.com/id15070507"),
    "36": ("Сергей Николаевич Евсеев", "https://vk.com/sergeyevseev48")
}

@bot.message_handler(func=lambda m: m.text.isdigit())
def handle_district_number(message):
    num = message.text.strip()
    if num in districts:
        name, link = districts[num]
        text = f"Твой округ: {num}\nПредставитель Клуба Городского Жителя: {name}"
        if link:
            text += f"\n\nПодпишись на него в социальной сети ВК: {link}"
    else:
        text = "Введите число от 1 до 36"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Назад")
    if text.startswith("Введите число"):
        markup.add("Не знаю")
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Не знаю")
def handle_dont_know(message):
    text = (
        "Как узнать номер округа?:\n"
        "- перейди по ссылке на сайт ЦИК РФ: http://www.cikrf.ru/digital-services/nayti-svoy-izbiratelnyy-uchastok/\n"
        "- на сайте введи название города, улицу и номер дома\n"
        "- нажми 'Найти' — и увидишь № УИК\n"
        "- затем напиши мне этот номер в формате 00-00"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: m.text == "Назад")
def handle_back(message):
    main_menu(message.chat.id)

@bot.message_handler(func=lambda m: m.text == "Подписаться на соцсети представителя")
def handle_subscribe(message):
    bot.send_message(message.chat.id, "Эта функция будет реализована позже.")

@bot.message_handler(func=lambda m: m.text == "Поддержать представителя в голосовании")
def handle_support(message):
    bot.send_message(message.chat.id, "Эта функция будет реализована позже.")

bot.infinity_polling()
