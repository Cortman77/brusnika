import telebot
from telebot import types
import os
import random  # Импортируем random для случайного выбора
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
    "Зарежу": {"path": os.path.join(base_dir, "audio/zarezhu.mp3")},
    "Может не открыть глаза": {"path": os.path.join(base_dir, "audio/huinya_na_kopceve.mp3")},
    "Сапогом в ебало": {"path": os.path.join(base_dir, "audio/sapogom.mp3")},
    "Пизды выпишу и ВСЁ": {"path": os.path.join(base_dir, "audio/skotina.mp3")},
    "UNлимитное животное": {"path": os.path.join(base_dir, "audio/anlimitnoe.mp3")},
    "Компьютерный мастер": {"path": os.path.join(base_dir, "audio/comp.mp3")},
    "Немытый крестьянин": {"path": os.path.join(base_dir, "audio/nemytyi.mp3")},
    "Федерация Барса": {"path": os.path.join(base_dir, "audio/federaciya_barsa.mp3")},
    "Выдаёт базу": {"path": os.path.join(base_dir, "audio/vydaet_bazu.mp3")},
    "Банана мама": {"path": os.path.join(base_dir, "audio/banana.mp3")},
    "Для девочки": {"path": os.path.join(base_dir, "audio/dvedevocki.mp3")},
    "Уроки французского": {"path": os.path.join(base_dir, "audio/uroki.mp3")},
    "Подвели": {"path": os.path.join(base_dir, "audio/podveli.mp3")},
    "Тополинный пух": {"path": os.path.join(base_dir, "audio/topolinyi_puh.mp3")}, 
    "Песня: 'Ты сука'": {"path": os.path.join(base_dir, "audio/ty_suka.mp3")},
    "Временная яма": {"path": os.path.join(base_dir, "audio/vremennaya_yma.mp3")},
    "Напасовая пиздоболия": {"path": os.path.join(base_dir, "audio/napasovaya.mp3")}, 
    "Власу нельзя": {"path": os.path.join(base_dir, "audio/vlasu_nelzya.mp3")},
    "Жизненный стаж": {"path": os.path.join(base_dir, "audio/STAZH.mp3")},
    "Невнятная 2": {"path": os.path.join(base_dir, "audio/bubosy.mp3")},
    "Бык-осеменитель": {"path": os.path.join(base_dir, "audio/byk_osem.mp3")},
    "Драка с голубями": {"path": os.path.join(base_dir, "audio/draka_golub.mp3")},
    "Плебей ебанный": {"path": os.path.join(base_dir, "audio/osilit_nihya.mp3")},
    "Сгущенка": {"path": os.path.join(base_dir, "audio/v_unitaz.mp3")},
    "Я уебан": {"path": os.path.join(base_dir, "audio/ya_ueban.mp3")},
    "Падкие на баб": {"path": os.path.join(base_dir, "audio/padkie_bab.mp3")},
    "Я приехал": {"path": os.path.join(base_dir, "audio/ya_priehal.mp3")},
    "Полусекс": {"path": os.path.join(base_dir, "audio/polusex.mp3")},
    "Пусть сядет": {"path": os.path.join(base_dir, "audio/pust_syadet.mp3")},
    "Промежуток времени": {"path": os.path.join(base_dir, "audio/promezhutok_vremeni.mp3")},
    "Клара за сотку": {"path": os.path.join(base_dir, "audio/klara_za_sotku.mp3")}, 
    "Насри,Насри": {"path": os.path.join(base_dir, "audio/nasri.mp3")},
    "Нервный тик": {"path": os.path.join(base_dir, "audio/nervnyi_tik.mp3")},
    "Можете не отвечать": {"path": os.path.join(base_dir, "audio/mozhete_ne_otvechat.mp3")},
    "Пива куплю": {"path": os.path.join(base_dir, "audio/piva_kuplu.mp3")},
    "Тебя выебут (Remake Коля)": {"path": os.path.join(base_dir, "audio/tebya_vyebut_remake.mp3")},
    "Ухохо": {"path": os.path.join(base_dir, "audio/uhoho.mp3")},
    "Она его выкинет": {"path": os.path.join(base_dir, "audio/vykinet.mp3")},
    


}

# Словарь с парами "название темы: список дочерних кнопок"
topics = {
    "НОВИНКИ🆕:Угрозы☠️☠️": ["Зарежу", "Может не открыть глаза", "Сапогом в ебало", "Пизды выпишу и ВСЁ", "Плебей ебанный"  ],
    "НОВИНКИ🆕:Брусника поясняет🤌" : ["UNлимитное животное", "Компьютерный мастер", "Немытый крестьянин", "Федерация Барса", "Выдаёт базу", "Напасовая пиздоболия" ],
    "НОВИНКИ🆕:КРИКИ и песни😱&🎤" : ["Банана мама", "Для девочки", "Уроки французского", "Подвели", "Тополинный пух", "Песня: 'Ты сука'", "Временная яма", "Власу нельзя", "Я уебан", "Она его выкинет"  ],
    "НОВИНКИ🆕:Просто приколюхи🥳🥳": ["Жизненный стаж", "Невнятная 2", "Бык-осеменитель", "Драка с голубями","Сгущенка", "Падкие на баб", "Я приехал", "Полусекс", "Пусть сядет", "Промежуток времени" ],
    "НОВИНКИ🆕:Короткие💨💨": ["Клара за сотку", "Насри,Насри", "Нервный тик", "Можете не отвечать", "Пива куплю", "Тебя выебут (Remake Коля)", "Ухохо"  ],
    "Быкующий🐃🥊": ["Просто пидр", "Рыгота", "На человечий перевести?", "Пояснение за город", "Ебальник", "Ебальник-2"],
    "Макакич🐒": ["Рыгота", "AAAA", "гоблинский", "ХАХА", "Твари", "Запрещу"],
    "Ярость🤬🔥🔥": ["БЛЯЯЯТЬ", "Дуру гнать", "Хуйня не работает", "Заебало нахуй", "Политические дебаты"],
    "Моменты гордости⭐️": ["Брусникин ФМ", "Одобрение кредитки", "Уметь надо", "Я вложил в этот чат свою жизнь...", "Когда получил кредитку"],
    "Искусство дипломатии💭": ["Хуевость", "Пацаны охуевают", "Дадут ствол", "Айфонодрочер", "Заблокировали", "Во всём виноват Санёк", "Лох это ты", "Лох твой отец", "Падик"],
    
}

donate_audio_files = [
    os.path.join(base_dir, "audio/DONATe.mp3"),
    os.path.join(base_dir, "audio/DONATE2.mp3")
]



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
    
    # Добавляем кнопку "🎲 Случайный аудио"
    random_button = types.KeyboardButton(text="🎲 Случайная фразочка")
    donate_button = types.KeyboardButton(text="Донат на ПИВО 🍺")
    keyboard.add(random_button, donate_button)
    
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
        
        # Обновляем статистику для пользователя
        user_id = str(message.chat.id)  # Используем chat.id как уникальный идентификатор пользователя
        phrase = message.text
        logger.info(f"Updating stats for user {user_id} with phrase '{phrase}'")  # Логируем обновление
        stats_manager.update_stat(user_id, phrase)  # Обновляем статистику
        
    else:
        bot.send_message(message.chat.id, f"Файл не найден: {audio_path}")

# Обработчик команды /stats
@bot.message_handler(commands=['stats'])
def send_stats(message):
    stats = stats_manager.load_stats()  # Загружаем статистику
    if not stats:
        bot.send_message(message.chat.id, "Статистика пуста.")
        return
    
    # Формируем сообщение со статистикой
    stats_message = "Статистика:\n"
    for user_id, phrases in stats.items():
        stats_message += f"\nПользователь {user_id}:\n"
        for phrase, count in phrases.items():
            stats_message += f"  - {phrase}: {count} раз(а)\n"
    
    bot.send_message(message.chat.id, stats_message)

    # Логируем событие
    logger.info(f"User {message.chat.id} requested stats.")


# Обработчик нажатия на кнопку "Назад"
@bot.message_handler(func=lambda message: message.text == "Назад")
def handle_back_button(message):
    start(message)  # Возвращаемся к выбору тем

# Логируем событие
    logger.info(f"User {message.chat.id} pressed 'Назад'")

@bot.message_handler(func=lambda message: message.text == "Донат на ПИВО 🍺")
def handle_donate_button(message):
    # Отправляем сообщение с кнопкой для доната
    donate_url = "https://yoomoney.ru/to/410011621862970"
    donate_keyboard = types.InlineKeyboardMarkup()
    donate_button = types.InlineKeyboardButton(text="НА ЖАТЕЦКИЙ ГУСЬ!!!!", url=donate_url)
    donate_keyboard.add(donate_button)
    bot.send_message(message.chat.id, "ЗАКИНЬ НА ПИВАСИК БРУСНИКЕ", reply_markup=donate_keyboard)

    # Отправка изображения
    image_path = os.path.join(base_dir, "images/beer.jpg")  # Укажите правильный путь к изображению
    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, photo=image_file)
    else:
        bot.send_message(message.chat.id, f"Картинка не найдена: {image_path}")

    # Случайный выбор аудиофайла и его отправка
    random_audio = random.choice(donate_audio_files)
    
    # Проверяем, существует ли файл, и отправляем его
    if os.path.exists(random_audio):
        with open(random_audio, 'rb') as audio_file:
            bot.send_audio(message.chat.id, audio=audio_file)
    else:
        bot.send_message(message.chat.id, f"Файл не найден: {random_audio}")
    
    # Логируем событие
    logger.info(f"User {message.chat.id} pressed 'Донат на пиво 🍺' and received audio: {random_audio}")


# Обработчик нажатия на кнопку "🎲 "
@bot.message_handler(func=lambda message: message.text == "🎲 Случайная фразочка")
def handle_random_audio(message):
    random_phrase = random.choice(list(audio_files.keys()))  # Случайный ключ из словаря audio_files
    audio_path = audio_files[random_phrase]["path"]
    
    if os.path.exists(audio_path):
        with open(audio_path, 'rb') as audio_file:
            bot.send_audio(message.chat.id, audio=audio_file)
        bot.send_message(message.chat.id, f"🎲 Случайная фразочка: {random_phrase}")  # Сообщаем пользователю, какой аудиофайл был выбран
    else:
        bot.send_message(message.chat.id, f"Файл не найден: {audio_path}")

# Запускаем бота
bot.polling(none_stop=True)


