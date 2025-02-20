FROM python:3.10-slim

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Указание переменных окружения
ENV DATABASE_URL="postgresql://user:password@db:5432/dbname"

# Ожидание готовности базы данных перед запуском
CMD ["sh", "-c", "sleep 5 && python main.py"]
