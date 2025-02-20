import pytest
from unittest.mock import AsyncMock, MagicMock
from bot import Bot
from database import DataBase

@pytest.fixture
def mock_bot():
    mock = AsyncMock(spec=Bot)
    mock.send_message = AsyncMock()
    return mock

@pytest.fixture
def mock_db():
    mock = MagicMock(spec=DataBase)
    mock.execute_query = MagicMock()
    return mock

def test_send_message(mock_bot):
    """Тест отправки сообщения."""
    recipient_id = 123456
    message_text = "Hello!"
    
    pytest.run(mock_bot.send_message(recipient_id, message_text))
    mock_bot.send_message.assert_called_once_with(recipient_id, message_text)

def test_database_query(mock_db):
    """Тест выполнения SQL-запроса."""
    query = "SELECT * FROM recipients;"
    mock_db.execute_query(query)
    mock_db.execute_query.assert_called_once_with(query)

def test_message_sending(mock_bot, mock_db):
    """Тест отправки сообщений всем пользователям из базы."""
    mock_db.execute_query.return_value = [(123, 'user1'), (456, 'user2')]
    message_text = "Scheduled Message!"
    
    for user_id, _ in mock_db.execute_query("SELECT id FROM recipients;"):
        pytest.run(mock_bot.send_message(user_id, message_text))
    
    assert mock_bot.send_message.call_count == 2
