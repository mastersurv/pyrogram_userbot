import asyncio
from pyrogram import Client, filters
import json
import os
from datetime import datetime, timedelta
import time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database import DataBase

# Конфигурация
API_ID = int(os.getenv("API_ID", "123456"))  # Замените на ваш API_ID
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Замените на ваш API_HASH
SESSION_NAME = "my_bot"
DB_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

# Настройка клиента Pyrogram
app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)
scheduler = AsyncIOScheduler()
db = DataBase(DB_URL)

# Триггеры для автоответов
TRIGGERS = {
    "привет": "Здравствуйте! Чем могу помочь?",
    "услуги": "Мы предоставляем онлайн-услуги. Подробнее: example.com",
}

def load_recipients():
    """
    Загружает список получателей из базы данных.
    :return: список user_id
    """
    try:
        query = "SELECT user_id FROM recipients"
        recipients = [row["user_id"] for row in db.execute_query(query)]
        return recipients
    except Exception as e:
        print(f"Ошибка загрузки получателей: {e}")
        return []

@app.on_message(filters.private & filters.text)
async def auto_reply(client, message):
    """
    Автоответчик на входящие сообщения по заданным триггерам.
    :param client: экземпляр клиента Pyrogram
    :param message: объект сообщения
    """
    text = message.text.lower()
    for trigger, response in TRIGGERS.items():
        if trigger in text:
            await message.reply(response)
            break

async def send_bulk_message():
    """
    Отправляет массовые сообщения по списку получателей.
    """
    recipients = load_recipients()
    for user_id in recipients:
        try:
            await app.send_message(user_id, "Привет! Вот наши новые предложения!")
            await asyncio.sleep(1)  # Антиспам-пауза
        except Exception as e:
            print(f"Ошибка отправки {user_id}: {e}")

def schedule_broadcast():
    """
    Запускает планировщик для массовых сообщений.
    """
    scheduler.add_job(send_bulk_message, "interval", hours=24, next_run_time=datetime.now() + timedelta(seconds=10))
    scheduler.start()

if __name__ == "__main__":
    schedule_broadcast()
    app.run()
