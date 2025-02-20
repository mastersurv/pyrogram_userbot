import psycopg2
from psycopg2.extras import RealDictCursor

class DataBase:
    """
    Класс для работы с базой данных PostgreSQL.
    """
    def __init__(self, db_url):
        """
        Инициализация класса с параметрами подключения.
        :param db_url: URL базы данных
        """
        self.db_url = db_url
        self.create_tables()

    def execute_query(self, query, params=None, fetch=False):
        """
        Выполняет SQL-запрос к базе данных.
        :param query: строка SQL-запроса
        :param params: параметры для SQL-запроса
        :param fetch: если True, возвращает результат запроса
        :return: результат запроса (если fetch=True), иначе None
        """
        try:
            conn = psycopg2.connect(self.db_url, cursor_factory=RealDictCursor)
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                result = cursor.fetchall() if fetch else None
                conn.commit()
            conn.close()
            return result
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            return None

    def create_tables(self):
        """
        Создает необходимые таблицы в базе данных.
        """
        queries = [
            """
            CREATE TABLE IF NOT EXISTS recipients (
                id SERIAL PRIMARY KEY,
                user_id BIGINT UNIQUE NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS messages (
                id SERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        ]
        for query in queries:
            self.execute_query(query)