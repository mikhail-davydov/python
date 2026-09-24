from datetime import date

# Common
WARN_NOTIFICATION_DAYS = 3
NOTE_FIELDS_COUNT = 3
SPLIT_BY = ','
DATE_FORMAT = '%d.%m.%Y'

# Requests
START_DATE = date.fromisoformat('2026-01-01')
DOC_TYPE = 'doc-invoice'
HEADERS = {
    'Accept': 'application/json',
}

# Threads
MAX_WORKERS = None
TIMEOUT = 30
