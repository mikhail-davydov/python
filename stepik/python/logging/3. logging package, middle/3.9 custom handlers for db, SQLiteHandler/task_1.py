import logging
import sqlite3

TABLE_NAME = "logs"


class SQLiteHandler(logging.Handler):
    def __init__(self, database: str, level=logging.NOTSET):
        super().__init__(level=level)
        self.connection = sqlite3.connect(database)
        self._create_table()

    def _create_table(self):
        cursor = self.connection.cursor()
        sql = f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created REAL,
                levelname TEXT,
                name TEXT,
                message TEXT
            )
        """
        cursor.execute(sql)
        self.connection.commit()

    def emit(self, record):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO {TABLE_NAME} (created, levelname, name, message) VALUES (?, ?, ?, ?)",
                       (record.created, record.levelname, record.name, record.getMessage())
                       )
        self.connection.commit()

    def close(self):
        self.connection.close()
        super().close()


# alt

class SQLiteHandler(logging.Handler):
    def __init__(self, database, level=logging.NOTSET):
        super().__init__(level=level)
        self.con = sqlite3.connect(database)
        self._create_table()

    def _create_table(self):
        cursor = self.con.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created REAL,
                levelname TEXT,
                name TEXT,
                message TEXT
            )
        """
                       )
        self.con.commit()

    def emit(self, record):
        message = record.getMessage()
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO logs (created, levelname, name, message) VALUES (?, ?, ?, ?)",
                       (record.created, record.levelname, record.name, message)
                       )
        self.con.commit()

    def close(self):
        self.con.close()
        super().close()


logger = logging.getLogger("db_logger")
logger.setLevel(logging.DEBUG)
handler = SQLiteHandler("logs.db")
logger.addHandler(handler)
logger.debug("Пример сообщения")
logger.warning("Пример сообщения с аргументом %d", 42)

conn = sqlite3.connect('logs.db')
cursor = conn.cursor()

# Проверяем имена столбцов таблицы, печатая их
cursor.execute("PRAGMA table_info(logs)")
columns = cursor.fetchall()
print(*(col[1] for col in columns))

# Проверяем содержимое таблицы логов, печатая строки
for row in cursor.execute("SELECT * FROM logs"):
    print(*row)
