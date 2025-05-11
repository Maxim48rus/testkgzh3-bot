import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '8191036899:AAFMh27lAeUoP_ON8JyZPhDatRAIDz33RLg'
bot = telebot.TeleBot(TOKEN)

# Словарь округов
okrugs = {
    '1': ("Павел Александрович Цуканов", "https://vk.com/pavel.tsukanov48"),
    '2': ("Сергей Васильевич Сазонов", "https://vk.com/svsazonov"),
    '3': ("Олег Владимирович Косолапов", "https://vk.com/id597083208"),
    '4': ("Василий Алексеевич Литовкин", "https://vk.com/id714688672"),
    '5': ("Анна Валерьевна Широких", "https://vk.com/id352507585"),
    '6': ("Вадим Николаевич Негробов", "https://vk.com/id288778777"),
    '7': ("Кирилл Викторович Иванов", "https://vk.com/ivanov_kb"),
    '8': ("Юрий Анатольевич Шкарин", "https://vk.com/id565972891"),
    '9': ("Михаил Юрьевич Русаков", "https://vk.com/mikhaelrusakov"),
    '10': ("Артем Николаевич Голощапов", "https://vk.com/a.goloshchapov"),
    '11': ("Андрей Викторович Выжанов", "https://vk.com/avyzhanov"),
    '12': ("Евгения Вальерьевна Фрай", "https://vk.com/evgenyafrai"),
    '13': ("Сергей Викторович Попов", "https://vk.com/id917351362"),
    '14': ("Станислав Алексеевич Полосин", "https://vk.com/stanislavpolosin48"),
    '15': ("Екатерина Алексеевна Пинаева", "https://vk.com/pinaeva_ea"),
    '16': ("Вера Ивановна Урываева", "https://vk.com/urivaevavi"),
    '17': ("Глеб Игоревич Гутевич", "https://vk.com/id1037188881"),
    '18': ("Игорь Николаевич Подзоров", "https://vk.com/inpodzorov"),
    '19': ("Евгений Сергеевич Колесников", None),
    '20': ("Алексей Иванович Поляков", None),
    '21': ("Павел Викторович Рухлин", "https://vk.com/pavelrukhlin"),
    '22': ("Елена Александровна Есина", "https://vk.com/id156008190"),
    '23': ("Игорь Александрович Катасонов", "https://vk.com/id1038206450"),
    '24': ("Андрей Владимирович Огородников", None),
    '25': ("Галина Николаевна Селина", None),
    '26': ("Алина Евгеньевна Теперик", "https://vk.com/malinateperik"),
    '27': ("Владислав Александрович Аленин", "https://vk.com/id1043676620"),
    '28': ("Дмитрий Анатольевич Гладышев", "https://vk.com/id152531671"),
    '29': ("Дмитрий Николаевич Погорелов", "https://vk.com/id596326492"),
    '30': ("Андрей Викторович Иголкин", "https://vk.com/igolkin83"),
    '31': ("Андрей Васильевич Бугаков", "https://vk.com/id132130001"),
    '32': ("Станислав Геннадьевич Каменецкий", "https://vk.com/id301354842"),
    '33': ("Борис Владимирович Понаморев", "https://vk.com/okrug33"),
    '34': ("Татьяна Сергеевна Шипилова", "https://vk.com/kaverinats"),
    '35': ("Александр Семёнович Перевозчиков", "https://vk.com/id15070507"),
    '36': ("Сергей Николаевич Евсеев", "https://vk.com/sergeyevseev48")
}

# Клавиатуры

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Узнать кто представитель клуба КГЖ"))
    markup.add(KeyboardButton("Поддержать представителя в голосовании"))
    return markup

def back_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Назад"))
    return markup

def start_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Начать"))
    return markup

def unknown_district_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Не знаю"))
    markup.add(KeyboardButton("Назад"))
    return markup

def voting_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Проголосовать", url="https://pg.er.ru"))
    return markup

@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda m: m.text.lower() in ['привет', 'старт', 'start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=start_menu())

@bot.message_handler(func=lambda m: m.text == "Начать")
def step_1(message):
    bot.send_message(
        message.chat.id,
        "Добрый день! Я помощник Клуба Городского Жителя - сокращенно КГЖ. Выбери один из 2-х пунктов",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda m: m.text == "Поддержать представителя в голосовании")
def support_vote(message):
    bot.send_message(
        message.chat.id,
        "Голосование состоится в период с 19 по 25 мая 2025 года. Для голосования нажми на кнопку «проголосовать».",
        reply_markup=voting_menu()
    )

@bot.callback_query_handler(func=lambda call: call.data == "back")
def callback_back(call):
    bot.send_message(
        call.message.chat.id,
        "Добрый день! Я помощник Клуба Городского Жителя - сокращенно КГЖ. Выбери один из 2-х пунктов",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda m: m.text == "Узнать кто представитель клуба КГЖ")
def ask_district(message):
    bot.send_message(
        message.chat.id,
        "Напиши номер своего избирательного округа (от 1 до 36) или нажми кнопку «Не знаю»",
        reply_markup=unknown_district_menu()
    )

@bot.message_handler(func=lambda m: m.text == "Не знаю")
def dont_know(message):
    text = (
        "Как узнать номер округа?:\n\n"
        "1. Перейди по ссылке на сайт ЦИК РФ http://www.cikrf.ru/digital-services/nayti-svoy-izbiratelnyy-uchastok/\n"
        "2. На сайте введи название города, наименование улицы и номер дома по адресу регистрации\n"
        "3. Нажми кнопку \"Найти\" и система выдаст № УИК\n"
        "4. Затем напиши мне сообщением номер УИК с соблюдением формата 00-00"
    )
    bot.send_message(message.chat.id, text, reply_markup=back_menu())

@bot.message_handler(func=lambda m: m.text == "Назад")
def go_back(message):
    bot.send_message(
        message.chat.id,
        "Добрый день! Я помощник Клуба Городского Жителя - сокращенно КГЖ. Выбери один из 2-х пунктов",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda m: m.text.isdigit())
def handle_district_number(message):
    district = message.text
    if district in okrugs:
        name, link = okrugs[district]
        msg = f"Твой округ: {district}. Представитель Клуба Городского Жителя: {name}."
        if link:
            msg += f"\n\nПодпишись на него в социальной сети ВК: {link}"
        bot.send_message(message.chat.id, msg, reply_markup=back_menu())
    else:
        text = (
            "Введите число от 1 до 36\n\n"
            "Как узнать номер округа?:\n\n"
            "1. Перейди по ссылке на сайт ЦИК РФ http://www.cikrf.ru/digital-services/nayti-svoy-izbiratelnyy-uchastok/\n"
            "2. На сайте введи название города, наименование улицы и номер дома по адресу регистрации\n"
            "3. Нажми кнопку \"Найти\" и система выдаст № УИК\n"
            "4. Затем напиши мне сообщением номер УИК с соблюдением формата 00-00"
        )
        bot.send_message(message.chat.id, text, reply_markup=unknown_district_menu())

uik_to_okrug = {
    uik: '1' for uik in ['21-01', '21-02', '21-03', '21-04', '21-05']
} | {
    uik: '2' for uik in ['21-06', '21-07', '21-08', '21-09', '21-10', '21-11']
} | {
    uik: '3' for uik in ['23-15', '23-16', '23-18', '23-19', '23-20', '23-21']
} | {
    uik: '4' for uik in ['21-13', '21-14', '21-15', '21-17', '21-18', '21-19', '21-20', '21-21']
} | {
    uik: '5' for uik in ['22-01', '22-02', '22-03', '22-04', '22-05']
} | {
    uik: '6' for uik in ['22-06', '22-07', '22-08', '22-09', '22-10']
} | {
    uik: '7' for uik in ['22-11', '22-12', '22-13', '22-14', '22-16', '22-47']
} | {
    uik: '8' for uik in ['25-05', '25-06', '25-07', '25-08', '25-09', '25-10']
} | {
    uik: '9' for uik in ['25-11', '25-12', '25-21', '25-22', '25-23']
} | {
    uik: '10' for uik in ['25-17', '25-18', '25-20', '25-26']
} | {
    uik: '11' for uik in ['25-13', '25-14', '25-15', '25-16', '25-19']
} | {
    uik: '12' for uik in ['25-01', '25-02', '25-03', '25-04']
} | {
    uik: '13' for uik in ['22-15', '22-17', '22-18', '22-19', '22-21']
} | {
    uik: '14' for uik in ['22-20', '22-22', '22-24', '22-25', '22-30']
} | {
    uik: '15' for uik in ['22-23', '22-26', '22-27', '22-28', '22-35']
} | {
    uik: '16' for uik in ['22-29', '22-31', '22-32', '22-33', '22-34']
} | {
    uik: '17' for uik in ['22-41', '22-42', '22-43', '22-44', '22-45', '22-46']
} | {
    uik: '18' for uik in ['22-36', '22-37', '22-38', '22-39', '22-40']
} | {
    uik: '19' for uik in ['24-01', '24-02', '24-03', '24-04', '24-05', '24-06', '24-11']
} | {
    uik: '20' for uik in ['21-12', '21-16', '24-07', '24-08', '24-09', '24-10']
} | {
    uik: '21' for uik in ['24-12', '24-13', '24-14', '24-15', '24-16']
} | {
    uik: '22' for uik in ['24-17', '24-18', '24-19', '24-29', '24-31']
} | {
    uik: '23' for uik in ['24-20', '24-21', '24-23', '24-27', '24-28', '24-30']
} | {
    uik: '24' for uik in ['24-22', '24-24', '24-25', '24-26', '24-32']
} | {
    uik: '25' for uik in ['24-33', '24-34', '24-41', '24-42', '24-43']
} | {
    uik: '26' for uik in ['24-39', '24-44', '24-45', '24-46', '24-47']
} | {
    uik: '27' for uik in ['24-35', '24-36', '24-37', '24-38', '24-40']
} | {
    uik: '28' for uik in ['24-48', '24-49', '24-50', '24-51', '24-52']
} | {
    uik: '29' for uik in ['24-53', '24-54', '24-55', '24-56', '24-57', '24-58']
} | {
    uik: '30' for uik in ['24-59', '24-60', '24-61', '24-62', '24-63']
} | {
    uik: '31' for uik in ['23-01', '23-02', '23-03', '23-04', '23-05', '23-06', '23-07']
} | {
    uik: '32' for uik in ['23-12', '23-13', '23-14', '23-22', '23-23', '23-24']
} | {
    uik: '33' for uik in ['23-08', '23-09', '23-10', '23-11', '23-17']
} | {
    uik: '34' for uik in ['23-25', '23-26', '23-27', '23-28', '23-29']
} | {
    uik: '35' for uik in ['23-30', '23-31', '23-32', '23-33', '23-34']
} | {
    uik: '36' for uik in ['25-24', '25-25', '25-27', '25-28', '25-29', '25-30']
}

# Добавляем обработку формата УИК 00-00
@bot.message_handler(func=lambda m: '-' in m.text and len(m.text.strip()) == 5)
def handle_uik_format(message):
    uik = message.text.strip()
    if uik in uik_to_okrug:
        district = uik_to_okrug[uik]
        name, link = okrugs[district]
        msg = f"Твой округ: {district}. Представитель Клуба Городского Жителя: {name}."
        if link:
            msg += f"\n\nПодпишись на него в социальной сети ВК: {link}"
        bot.send_message(message.chat.id, msg, reply_markup=back_menu())
    else:
        bot.send_message(message.chat.id, "Не удалось определить округ. Попробуй ещё раз или проверь формат.", reply_markup=unknown_district_menu())


# Запуск бота
print("Бот запущен")
bot.infinity_polling()
