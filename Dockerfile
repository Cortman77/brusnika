# Базовый образ
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в рабочую директорию
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Создаем директорию для логов
RUN mkdir -p /logs

# Запускаем приложение
CMD ["python", "main.py"]


