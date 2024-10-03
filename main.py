import telebot
from telebot import types
import os
import random  # Импортируем random для случайного выбора



# Создаем экземпляр бота с указанием токена
bot = telebot.TeleBot("6713071175:AAFC3g1CTJGdDameBhacWEvsAh19DfbCoOk")


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
    "Иди на хуй": {"path": os.path.join(base_dir, "audio/idi_nahui.mp3")},
    "Похоже на куколдыча": {"path": os.path.join(base_dir, "audio/kukoldych.mp3")},
    "Что с монитором": {"path": os.path.join(base_dir, "audio/monitor.mp3")},
    "Никого лучше меня": {"path": os.path.join(base_dir, "audio/hui_dozhdetes.mp3")},
    "Установили что он пидр": {"path": os.path.join(base_dir, "audio/ustanovili_pidr.mp3")},
    "Дальше секс и ВСЁ": {"path": os.path.join(base_dir, "audio/dalshe_sex.mp3")},
    "Чисто в хате": {"path": os.path.join(base_dir, "audio/chisto.mp3")},
    "Когда тебе весело...": {"path": os.path.join(base_dir, "audio/kogda_tebe_veselo.mp3")},



    


}

# Словарь с парами "название темы: список дочерних кнопок"
topics = {
    "СВЕЖАЧОК🔥": ["Иди на хуй", "Похоже на куколдыча", "Что с монитором", "Никого лучше меня", "Установили что он пидр", "Дальше секс и ВСЁ", "Чисто в хате", "Когда тебе весело..." ],
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
    os.path.join(base_dir, "audio/dai_na_gusya.mp3"),
    os.path.join(base_dir, "audio/DONATE2.mp3"),
    os.path.join(base_dir, "audio/dai_GUSYA.mp3"),
]

def log_user_action(user_id, action):
    log_file_path = os.path.join(base_dir, 'user_actions.log')
    with open(log_file_path, 'a', encoding='utf-8') as log_file:  # Specify encoding here
        log_file.write(f"User ID: {user_id}, Action: {action}\n")

def notify_users_once(user_ids, message):
    # Путь к файлу для хранения уведомлений
    log_file_path = os.path.join(base_dir, 'update_notified.txt')

    # Проверяем, отправляли ли мы уведомление
    if os.path.exists(log_file_path):
        print("Уведомление уже было отправлено.")
        return

    success_ids = []
    failed_ids = []

    for user_id in user_ids:
        try:
            bot.send_message(user_id, message)
            print(f"Сообщение успешно отправлено пользователю {user_id}.")
            success_ids.append(user_id)  # Добавляем успешный ID в список
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")
            failed_ids.append(user_id)  # Добавляем неуспешный ID в список

    # Записываем в файл, чтобы больше не отправлять уведомление
    with open(log_file_path, 'w', encoding='utf-8') as f:
        f.write('Уведомление о обновлении отправлено.\n')
        f.write("Успешные ID:\n")
        for user_id in success_ids:
            f.write(f"{user_id}\n")
        f.write("Неудачные ID:\n")
        for user_id in failed_ids:
            f.write(f"{user_id}\n")

def create_inline_phrases_keyboard(topic):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    
    # Создаем кнопки для каждой фразы
    for phrase in topics[topic]:
        buttons.append(types.InlineKeyboardButton(text=phrase, callback_data=f"play_{phrase}"))
    
    if len(buttons) % 2 != 0:
        buttons.append(types.InlineKeyboardButton(text=" ", callback_data="none"))

    keyboard.add(*buttons)
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))
    
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for topic in topics.keys():
        keyboard.add(types.InlineKeyboardButton(text=topic, callback_data=f"topic_{topic}"))

    random_button = types.InlineKeyboardButton(text="🎲 Случайная фразочка", callback_data="random_phrase")
    donate_button = types.InlineKeyboardButton(text="Донат на ПИВО 🍺", callback_data="donate")
    keyboard.add(random_button, donate_button)
    
    bot.send_message(message.chat.id, 'Выбери раздел и накинь на пиво😉👌:', reply_markup=keyboard)

user_ids = [529675743, 402417063, 126798048, 1118235356, 582667115, 538677038, 835829519, 1854291293, 340501530, 184765660, 263879978, 107739615, 1165457840, 1198267690, 1998907657, 5193149161, 923695852, 107739615, 837372912, 854854532, 1854291293, 215781246 ]  # Сюда добавьте ID пользователей, которым нужно отправить уведомление
message = "Бот обновился! Ver. 1.03.\n 1) Изменен дизайн бота\n 2) С изменением кнопок частично решена проблема с бесконечным перелистыванием полученных фраз\n 3)Добавлены новые фразы\n 4) Добавлена функциональность уведомления о новых версиях бота.\n Пожалуйста, нажмите /start, чтобы получить новые функции."
notify_users_once(user_ids, message)

@bot.callback_query_handler(func=lambda call: call.data.startswith("topic_"))
def handle_topic_selection(call):
    topic = call.data.split("_")[1]
    log_user_action(call.from_user.id, f"Selected topic: {topic}")  # Логируем выбор темы
    bot.send_message(call.message.chat.id, "Выбери фразу:", reply_markup=create_inline_phrases_keyboard(topic))

@bot.callback_query_handler(func=lambda call: call.data.startswith("play_"))
def handle_phrase_selection(call):
    phrase = call.data.split("_")[1]
    audio_path = audio_files[phrase]["path"]
    log_user_action(call.from_user.id, f"Played phrase: {phrase}")  # Логируем нажатие кнопки фразы
    
    if os.path.exists(audio_path):
        with open(audio_path, 'rb') as audio_file:
            bot.send_audio(call.message.chat.id, audio=audio_file)
    else:
        bot.send_message(call.message.chat.id, f"Файл не найден: {audio_path}")

@bot.callback_query_handler(func=lambda call: call.data == "random_phrase")
def handle_random_phrase(call):
    random_phrase = random.choice(list(audio_files.keys()))
    audio_path = audio_files[random_phrase]["path"]
    log_user_action(call.from_user.id, f"Played random phrase: {random_phrase}")  # Логируем случайную фразу
    
    if os.path.exists(audio_path):
        with open(audio_path, 'rb') as audio_file:
            bot.send_audio(call.message.chat.id, audio=audio_file)
        bot.send_message(call.message.chat.id, f"🎲 Случайная фразочка: {random_phrase}")
    else:
        bot.send_message(call.message.chat.id, f"Файл не найден: {audio_path}")

@bot.callback_query_handler(func=lambda call: call.data == "donate")
def handle_donate_button(call):
    log_user_action(call.from_user.id, "Clicked donate button")  # Логируем донат
    donate_keyboard = types.InlineKeyboardMarkup()

    donate_button = types.InlineKeyboardButton(text="🔥🔥🔥 НА ЖАТЕЦКИЙ ГУСЬ!!! 🔥🔥🔥", callback_data='donate_to_gus')
    donate_keyboard.add(donate_button)

    bot.send_message(call.message.chat.id, "ЗАКИНЬ НА ПИВАСИК БРУСНИКЕ", reply_markup=donate_keyboard)

    image_path = os.path.join(base_dir, "images/beer.jpg")
    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            bot.send_photo(call.message.chat.id, photo=image_file)
    else:
        bot.send_message(call.message.chat.id, f"Картинка не найдена: {image_path}")

    if donate_audio_files:
        random_audio = random.choice(donate_audio_files)
        if os.path.exists(random_audio):
            with open(random_audio, 'rb') as audio_file:
                bot.send_audio(call.message.chat.id, audio=audio_file)
        else:
            bot.send_message(call.message.chat.id, f"Файл не найден: {random_audio}")
    else:
        bot.send_message(call.message.chat.id, "Нет доступных аудиофайлов.")

# Новый обработчик для кнопки "На Жатецкий Гусь"
@bot.callback_query_handler(func=lambda call: call.data == "donate_to_gus")
def handle_donate_to_gus_button(call):
    log_user_action(call.from_user.id, "Нажал кнопку 'На Жатецкий Гусь'")  # Логируем действие пользователя

    donate_url = "https://yoomoney.ru/to/410011621862970"
    bot.send_message(call.message.chat.id, f"ССЫЛОЧКА чтобы перечислить Бруснике на вдохновление!(Хоть рублик, но лучше СОТОЧКА): {donate_url}")

# Обработчик для кнопки "Назад"
@bot.callback_query_handler(func=lambda call: call.data == "back")
def handle_back_button(call):
    log_user_action(call.from_user.id, "Clicked back button")  # Логируем нажатие кнопки "Назад"
    start(call.message)

# Запускаем бота
bot.polling(none_stop=True)

