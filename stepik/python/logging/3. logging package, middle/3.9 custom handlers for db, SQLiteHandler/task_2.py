import json
import logging
import sqlite3

TABLE_NAME = "audit_logs"

DEFAULT_FIELDS_MAP = {'created': 'created',
                      'levelno': 'levelno',
                      'levelname': 'levelname',
                      'name': 'name',
                      'filename': 'filename',
                      'funcName': 'funcName',
                      'lineno': 'lineno',
                      'message': 'message',
                      'thread': 'thread',
                      'process': 'process',
                      'exc_info': 'exc_info',
                      'exc_text': 'exc_text',
                      'stack_info': 'stack_info'}

DEFAULT_FIELDS_TYPE = {'created': 'REAL',
                       'levelno': 'INTEGER',
                       'levelname': 'TEXT',
                       'name': 'TEXT',
                       'filename': 'TEXT',
                       'funcName': 'TEXT',
                       'lineno': 'INTEGER',
                       'message': 'TEXT',
                       'thread': 'INTEGER',
                       'process': 'INTEGER',
                       'exc_info': 'TEXT',
                       'exc_text': 'TEXT',
                       'stack_info': 'TEXT'}


class SQLiteHandler(logging.Handler):
    def __init__(self, db_path, fields_map=None, level=logging.NOTSET, table_name=TABLE_NAME):
        super().__init__(level)
        self.db_path = db_path
        self.table_name = table_name
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.db_path, check_same_thread=False, timeout=5)
            self.fields_map = fields_map or DEFAULT_FIELDS_MAP
            self._formatter = logging.Formatter()
            self._std_attrs = self._get_std_attrs()
            self._columns = self._get_columns()
            self._init_db()
        except Exception:
            if self.conn:
                self.conn.close()
            raise

    def _get_columns(self):
        columns_def = ["id INTEGER PRIMARY KEY AUTOINCREMENT"]
        for col_name, attr_name in self.fields_map.items():
            col_type = DEFAULT_FIELDS_TYPE.get(attr_name, 'TEXT')
            columns_def.append(f"{col_name} {col_type}")
        columns_def.append("extra_data TEXT")
        return columns_def

    def _init_db(self):
        cursor = self.conn.cursor()
        sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({', '.join(self._columns)})"
        cursor.execute(sql)
        self.conn.commit()

    @staticmethod
    def _get_std_attrs():
        dumb_record = logging.LogRecord("", 0, "", 0, "", (), None)
        return set(dumb_record.__dict__)

    def _get_extra_data(self, record):
        extra = {k: v for k, v in record.__dict__.items() if k not in self._std_attrs}
        return extra

    def _get_values(self, record):
        extra_dict = self._get_extra_data(record)
        extra_json = json.dumps(extra_dict, ensure_ascii=False, default=str)

        meta_data = {}
        exc_text = ""
        if record.exc_info:
            exc_text = record.exc_text or self._formatter.formatException(record.exc_info)
        elif record.exc_text:
            exc_text = record.exc_text
        meta_data["exc_text"] = exc_text
        meta_data["stack_info"] = self._formatter.formatStack(record.stack_info) if record.stack_info else ""
        meta_data["message"] = record.getMessage()

        values = []
        for record_attr_name in self.fields_map.values():
            if record_attr_name in ("exc_text", "stack_info", "message"):
                val = meta_data[record_attr_name]
            else:
                val = getattr(record, record_attr_name, None)
            if not isinstance(val, (str, int, float, type(None))):
                val = str(val)
            values.append(val)
        values.append(extra_json)

        return values

    def emit(self, record):
        try:
            placeholders = ["?"] * (len(self.fields_map) + 1)
            sql = (f"INSERT INTO {self.table_name} "
                   f"({', '.join(self.fields_map)}, extra_data) "
                   f"VALUES ({', '.join(placeholders)})")
            cursor = self.conn.cursor()
            values = self._get_values(record)
            cursor.execute(sql, values)
            self.conn.commit()
        except Exception:
            self.handleError(record)

    def close(self):
        if self.conn:
            try:
                self.conn.commit()
            finally:
                self.conn.close()
        super().close()


# Используется для проверки/демонстрации вашего решения
logger = logging.getLogger("SecurePy")
logger.setLevel(logging.DEBUG)

# 1. Режим "Полный аудит" (автоматически все поля + JSON для extra) fields_map не передан!
db_handler = SQLiteHandler("full_audit.db", level=logging.INFO)
logger.addHandler(db_handler)
logger.debug("Это сообщение НЕ должно быть обработано!")
logger.info("Системное событие", extra={'session_id': 'abc-123', 'ip': '192.168.1.1'})
logger.warning("Недопустимая операция", extra={'user_id': 55, 'error_code': 500})
try:
    1 / 0
except ZeroDivisionError:
    logger.error("Произошла ошибка деления", exc_info=True, stack_info=True)


# Проверка записи
def check_table(db: str) -> None:
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    print(f"\n=== Структура таблицы {TABLE_NAME} в {db} ===")
    cursor.execute(f"PRAGMA table_info({TABLE_NAME})")
    columns = cursor.fetchall()
    print("Колонки:", ", ".join(col[1] for col in columns))

    print(f"\n=== Данные в таблице {TABLE_NAME} ===")
    for row in cursor.execute(f"SELECT * FROM {TABLE_NAME}"):
        print(row)


check_table("full_audit.db")

# 2. Компактный режим (указанные поля в fields_map + JSON для extra)
compact_handler = SQLiteHandler("compact_audit.db", fields_map={'time': 'created', 'msg': 'message'})
logger.removeHandler(db_handler)
logger.addHandler(compact_handler)
logger.debug("Событие отладки должно быть обработано")
logger.warning("Предупреждение с контекстом", extra={'user_action': 'delete', 'item_id': 999})

check_table("compact_audit.db")
