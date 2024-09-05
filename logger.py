import logging
import os

# Получаем абсолютный путь к директории /logs
log_dir = '/logs'

# Убедитесь, что директория для логов существует
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Настройка логирования
logging.basicConfig(
    filename=os.path.join(log_dir, 'bot_activity.log'),  # Путь к файлу логов
    level=logging.INFO,  # Уровень логирования
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Формат записи логов
)

# Получаем логгер
logger = logging.getLogger(__name__)

