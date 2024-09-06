import telebot
from telebot import types
import os
from logger import logger  # Импортируем наш модуль логирования
from stats_manager import StatsManager  # Импортируем модуль статистики

# Создаем экземпляр бота с указанием токена
bot = telebot.TeleBot("6713071175:AAFC3g1CTJGdDameBhacWEvsAh19DfbCoOk")

# Инициализируем менеджер статистики
stats_manager = StatsManager(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'phrase_stats.json'))

# Получаем абсолютный путь к директории скрипта
base_dir = os.path.dirname(os.path.abspath(__file__))

# Словарь с парами "название кнопки: путь к аудиофайлу"
audio_files = {
    "Просто пидр": {"path": os.path.join(base_dir, "audio/prosto_pidr.mp3")},
    "Рыгота": {"path": os.path.join(base_dir, "audio/Rygota.mp3")},
    "AAAA": {"path": os.path.join(base_dir, "audio/AAAA.mp3")},
    "гоблинский": {"path": os.path.join(base_dir, "audio/nevyutnaya.mp3")},
    "На человечий перевести?": {"path": os.path.join(base_dir, "audio/cheloveckii.mp3")},
    "Пояснение за город": {"path": os.path.join(base_dir, "audio/za gorod.mp3")},
    "ХАХА": {"path": os.path.join(base_dir, "audio/HAHA.mp3")},
    "Твари": {"path": os.path.join(base_dir, "audio/tvari.mp3")},
    "БЛЯЯЯТЬ": {"path": os.path.join(base_dir, "audio/blyaaat.mp3")},
    "Дуру гнать": {"path": os.path.join(base_dir, "audio/duru_gnat.mp3")},
    "Хуйня не работает": {"path": os.path.join(base_dir, "audio/nerabotaet.mp3")},
    "СУКААА": {"path": os.path.join(base_dir, "audio/SUKAaaa.mp3")},
    "Заебало нахуй": {"path": os.path.join(base_dir, "audio/zaebalonahui.mp3")},
    "Ебальник": {"path": os.path.join(base_dir, "audio/ebalnik.mp3")},
    "Ебальник-2": {"path": os.path.join(base_dir, "audio/ebalnik_rashibu.mp3")},
    "Брусникин ФМ": {"path": os.path.join(base_dir, "audio/brusnikinFM.mp3")},
    "Одобрение кредитки": {"path": os.path.join(base_dir, "audio/kreditka.mp3")},
    "Уметь надо": {"path": os.path.join(base_dir, "audio/umetnado.mp3")},
    "Я вложил в этот чат свою жизнь...": {"path": os.path.join(base_dir, "audio/vetotchaszalozhil.mp3")},
    "Когда получил кредитку": {"path": os.path.join(base_dir, "audio/VYVMENYANEVERILI.mp3")},
    "Хуево": {"path": os.path.join(base_dir, "audio/huevo.mp3")},
    "Лох твой отец": {"path": os.path.join(base_dir, "audio/lohtvoiotec.mp3")},
    "Пацаны охуевают": {"path": os.path.join(base_dir, "audio/pacabiohuevaut.mp3")},
    "Лох это ты": {"path": os.path.join(base_dir, "audio/Poshelnahuiloh.mp3")},
    "Во всём виноват Санёк": {"path": os.path.join(base_dir, "audio/sanekvinovat.mp3")},
    "Политические дебаты": {"path": os.path.join(base_dir, "audio/Shveden.mp3")},
    "Дадут ствол": {"path": os.path.join(base_dir, "audio/stvol dadut zavalyu.mp3")},
    "Айфонодрочер": {"path": os.path.join(base_dir, "audio/suka iphone.mp3")},
    "Запрещу": {"path": os.path.join(base_dir, "audio/zaprechu.mp3")},
    "Заблокировали": {"path": os.path.join(base_dir, "audio/zablokir.mp3")},
    "Падик": {"path": os.path.join(base_dir, "audio/padik.mp3")},
}

# Словарь с парами "название темы: список дочерних кнопок"
topics = {
    "Быкующий🐃🥊": ["Просто пидр", "Рыгота", "На человечий перевести?", "Пояснение за город", "Ебальник", "Ебальник-2"],
    "Макакич🐒": ["Рыгота", "AAAA", "гоблинский", "ХАХА", "Твари", "Запрещу"],
    "Ярость🤬🔥🔥": ["БЛЯЯЯТЬ", "Дуру гнать", "Хуйня не работает", "Заебало нахуй", "Политические дебаты"],
    "Моменты гордости⭐️": ["Брусникин ФМ", "Одобрение кредитки", "Уметь надо", "Я вложил в этот чат свою жизнь...", "Когда получил кредитку"],
    "Искусство дипломатии💭": ["Хуевенько", "Пацаны охуевают", "Дадут ствол", "Айфонодрочер", "Заблокировали", "Во всём виноват Санёк", "Лох это ты", "Лох твой отец", "Падик"],
}

# Функция для создания клавиатуры с фразами
def create_phrases_keyboard(topic):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    for phrase in topics[topic]:
        keyboard.add(phrase)
    keyboard.add("Назад")
    return keyboard

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    buttons = [types.KeyboardButton(text=topic) for topic in topics]
    keyboard.add(*buttons)
    donate_button = types.KeyboardButton(text="Донат на пиво 🍺")
    keyboard.add(donate_button)
    bot.send_message(message.chat.id, 'Выбери раздел или накинь на пиво😉👌. Осторожно: раздел Ярость может быть громким😁:', reply_markup=keyboard)

# Логируем событие
    logger.info(f"/start command received from user {message.chat.id}")


# Обработчик нажатия на родительскую кнопку (тему)
@bot.message_handler(func=lambda message: message.text in topics.keys())
def handle_parent_button(message):
    bot.send_message(message.chat.id, 'Выбери фразу:', reply_markup=create_phrases_keyboard(message.text))

# Логируем событие
    logger.info(f"User {message.chat.id} selected topic: {message.text}")
 
 


    

# Обработчик нажатия на кнопку с фразой
@bot.message_handler(func=lambda message: message.text in audio_files.keys())
def handle_message(message):
    audio_path = audio_files[message.text]["path"]
    if os.path.exists(audio_path):
        with open(audio_path, 'rb') as audio_file:
            bot.send_audio(message.chat.id, audio=audio_file)
    else:
        bot.send_message(message.chat.id, f"Файл не найден: {audio_path}")

# Обработчик нажатия на кнопку "Назад"
@bot.message_handler(func=lambda message: message.text == "Назад")
def handle_back_button(message):
    start(message)  # Возвращаемся к выбору тем

# Логируем событие
    logger.info(f"User {message.chat.id} pressed 'Назад'")


# Обработчик нажатия на кнопку "Донат на пиво 🍺"
@bot.message_handler(func=lambda message: message.text == "Донат на пиво 🍺")
def handle_donate_button(message):
    donate_url = "https://yoomoney.ru/quickpay/fundraise/button?billNumber=12Q314103TU.240518"
    donate_keyboard = types.InlineKeyboardMarkup()
    donate_button = types.InlineKeyboardButton(text="На жатецкий гусь", url=donate_url)
    donate_keyboard.add(donate_button)
    bot.send_message(message.chat.id, "Закинь на пивко Брусникину", reply_markup=donate_keyboard)

# Логируем событие
    logger.info(f"User {message.chat.id} pressed 'Донат на пиво 🍺'")

# Запускаем бота
bot.polling(none_stop=True)




