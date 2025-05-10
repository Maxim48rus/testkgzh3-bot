import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

start_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Начать"))
main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Узнать кто представитель клуба КГЖ"),
    KeyboardButton("Подписаться на соцсети представителя"),
    KeyboardButton("Поддержать представителя в голосовании")
)
back_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Назад"))
district_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Не знаю"))

districts = {
    1: ("Павел Александрович Цуканов", "https://vk.com/pavel.tsukanov48"),
    2: ("Сергей Васильевич Сазонов", "https://vk.com/svsazonov"),
    3: ("Олег Владимирович Косолапов", "https://vk.com/id597083208"),
    4: ("Василий Алексеевич Литовкин", "https://vk.com/id714688672"),
    5: ("Анна Валерьевна Широких", "https://vk.com/id352507585"),
    6: ("Вадим Николаевич Негробов", "https://vk.com/id288778777"),
    7: ("Кирилл Викторович Иванов", "https://vk.com/ivanov_kb"),
    8: ("Юрий Анатольевич Шкарин", "https://vk.com/id565972891"),
    9: ("Михаил Юрьевич Русаков", "https://vk.com/mikhaelrusakov"),
    10: ("Артем Николаевич Голощапов", "https://vk.com/a.goloshchapov"),
    11: ("Андрей Викторович Выжанов", "https://vk.com/avyzhanov"),
    12: ("Евгения Вальерьевна Фрай", "https://vk.com/evgenyafrai"),
    13: ("Сергей Викторович Попов", "https://vk.com/id917351362"),
    14: ("Станислав Алексеевич Полосин", "https://vk.com/stanislavpolosin48"),
    15: ("Екатерина Алексеевна Пинаева", "https://vk.com/pinaeva_ea"),
    16: ("Вера Ивановна Урываева", "https://vk.com/urivaevavi"),
    17: ("Глеб Игоревич Гутевич", "https://vk.com/id1037188881"),
    18: ("Игорь Николаевич Подзоров", "https://vk.com/inpodzorov"),
    19: ("Евгений Сергеевич Колесников", ""),
    20: ("Алексей Иванович Поляков", ""),
    21: ("Павел Викторович Рухлин", "https://vk.com/pavelrukhlin"),
    22: ("Елена Александровна Есина", "https://vk.com/id156008190"),
    23: ("Игорь Александрович Катасонов", "https://vk.com/id1038206450"),
    24: ("Андрей Владимирович Огородников", ""),
    25: ("Галина Николаевна Селина", ""),
    26: ("Алина Евгеньевна Теперик", "https://vk.com/malinateperik"),
    27: ("Владислав Александрович Аленин", "https://vk.com/id1043676620"),
    28: ("Дмитрий Анатольевич Гладышев", "https://vk.com/id152531671"),
    29: ("Дмитрий Николаевич Погорелов", "https://vk.com/id596326492"),
    30: ("Андрей Викторович Иголкин", "https://vk.com/igolkin83"),
    31: ("Андрей Васильевич Бугаков", "https://vk.com/id132130001"),
    32: ("Станислав Геннадьевич Каменецкий", "https://vk.com/id301354842"),
    33: ("Борис Владимирович Понаморев", "https://vk.com/okrug33"),
    34: ("Татьяна Сергеевна Шипилова", "https://vk.com/kaverinats"),
    35: ("Александр Семёнович Перевозчиков", "https://vk.com/id15070507"),
    36: ("Сергей Николаевич Евсеев", "https://vk.com/sergeyevseev48"),
}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Нажми кнопку 'Начать'", reply_markup=start_kb)

@dp.message_handler(lambda m: m.text == "Начать")
async def show_main_menu(message: types.Message):
    await message.answer("Добрый день! Я помощник Клуба Городского Жителя - сокращенно КГЖ. Выбери один из 3-х пунктов", reply_markup=main_menu_kb)

@dp.message_handler(lambda m: m.text == "Узнать кто представитель клуба КГЖ")
async def ask_district(message: types.Message):
    await message.answer("Напиши номер своего избирательного округа (от 1 до 36)", reply_markup=district_kb)

@dp.message_handler(lambda m: m.text == "Не знаю")
async def send_help(message: types.Message):
    await message.answer(
        "Как узнать номер округа?:
"
        "- перейди по ссылке: http://www.cikrf.ru/digital-services/nayti-svoy-izbiratelnyy-uchastok/
"
        "- введи город, улицу и дом
"
        "- нажми "Найти" и система выдаст № УИК
"
        "- затем напиши мне номер УИК в формате 00-00", reply_markup=district_kb
    )

@dp.message_handler(lambda m: m.text.isdigit())
async def show_representative(message: types.Message):
    number = int(message.text)
    if number in districts:
        name, vk = districts[number]
        response = f"Твой округ: {number}. Представитель Клуба Городского Жителя: {name}"
        if vk:
            response += f"

Подпишись на него в социальной сети ВК: {vk}"
        await message.answer(response, reply_markup=back_kb)
    else:
        await message.answer("Введите число от 1 до 36", reply_markup=district_kb)

@dp.message_handler(lambda m: m.text == "Назад")
async def go_back(message: types.Message):
    await show_main_menu(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)