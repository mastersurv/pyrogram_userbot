# Telegram Auto-Responder Bot

Этот проект представляет собой Telegram-бота, созданного с использованием Pyrogram и PostgreSQL, который автоматически отвечает на сообщения и поддерживает массовую рассылку с планированием.

## Функционал

- Автоматическая обработка входящих сообщений
- Ответы по триггерам
- Массовая рассылка сообщений с планированием
- Использование PostgreSQL для хранения данных
- Запуск через Docker

## Установка и запуск

### Требования

- Python 3.10+
- PostgreSQL
- Docker (если требуется контейнеризация)

### Настройка

1. Клонируйте репозиторий:

   ```sh
   git clone https://github.com/your-repo/telegram-bot.git
   cd telegram-bot
   ```

2. Установите зависимости:

   ```sh
   pip install -r requirements.txt
   ```

3. Настройте переменные окружения:

   ```sh
   export API_ID=your_api_id
   export API_HASH=your_api_hash
   export DATABASE_URL="postgresql://user:password@localhost/dbname"
   ```

4. Запустите бота:

   ```sh
   python main.py
   ```

### Запуск через Docker

1. Постройте и запустите контейнер:
   ```sh
   docker-compose up --build
   ```

## Структура проекта

```
telegram-bot/
│── database.py        # Работа с базой данных PostgreSQL
│── main.py            # Основной файл бота
│── Dockerfile         # Контейнеризация
│── docker-compose.yml # Оркестрация контейнеров
│── requirements.txt   # Зависимости проекта
│── README.md          # Документация
```

## Лицензия

Проект распространяется под лицензией MIT.

