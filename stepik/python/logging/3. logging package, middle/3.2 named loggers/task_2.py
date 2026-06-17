import logging
import sys

audit_stat = {}


def audit_counter(record: logging.LogRecord) -> bool:
    if hasattr(record, 'user_id'):
        audit_stat[record.user_id] = audit_stat.get(record.user_id, 0) + 1
    return True


logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format='[%(levelname)-8s] - %(name)-15s - %(threadName)s - %(message)s'
)

log_app = logging.getLogger('app')
log_app_api = logging.getLogger('app.api')
log_app_api.setLevel(logging.INFO)

log_app_database = logging.getLogger('app.database')
log_utils = logging.getLogger('utils')
log_utils.setLevel(logging.WARNING)

log_app_audit = logging.getLogger('app.audit')
log_app_audit.setLevel(logging.DEBUG)
log_app_audit.propagate = False

audit_file_handler = logging.FileHandler(
    filename='audit.log',
    encoding='u8'
)
audit_file_formatter = logging.Formatter(
    fmt='[%(levelname)-8s] - %(name)s - %(user_id)d - %(message)s',
    defaults={'user_id': -1}
)
audit_file_handler.setFormatter(audit_file_formatter)
log_app_audit.addHandler(audit_file_handler)
log_app_audit.addFilter(audit_counter)

# alt

import logging
import sys

audit_stat = {}


def audit_counter(record: logging.LogRecord) -> bool:
    pass


log_root = logging.getLogger()
log_root.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(stream=sys.stdout)
general_format = logging.Formatter(
    fmt="[%(levelname)-8s] - %(name)-15s - %(threadName)s - %(message)s",
    defaults={"user_id": -1},
)
stream_handler.setFormatter(general_format)
log_root.addHandler(stream_handler)

log_app = logging.getLogger("app")

log_app_api = logging.getLogger("app.api")
log_app_api.setLevel(logging.INFO)


class AuditLoggerFactory:
    def __init__(self, *, logger_name: str = "app.audit", filename: str = "audit.log"):
        self.logger_name = logger_name
        self.filename = filename

    def record_filter(self, record: logging.LogRecord) -> bool:
        user_id = getattr(record, 'user_id', -1)
        if user_id != -1:
            audit_stat[user_id] = audit_stat.get(user_id, 0) + 1
        return True

    def create_logger(self) -> logging.Logger:
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.DEBUG)

        audit_handler = logging.FileHandler(self.filename)
        audit_fmt = logging.Formatter(
            fmt="[%(levelname)-8s] - %(name)s - %(user_id)d - %(message)s",
            defaults={"user_id": -1},
        )
        audit_handler.setFormatter(audit_fmt)
        logger.addHandler(audit_handler)
        logger.addFilter(self.record_filter)
        logger.propagate = False

        return logger


log_app_audit = AuditLoggerFactory().create_logger()

log_app_database = logging.getLogger("app.database")
log_app_database.setLevel(logging.DEBUG)

log_utils = logging.getLogger("utils")
log_utils.setLevel(logging.WARNING)
