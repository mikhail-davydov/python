import re

from datetime import date

# Common
WARN_NOTIFICATION_DAYS = 3
NOTE_FIELDS_COUNT = 4
SPLIT_BY = ','
DATE_FORMAT = '%d.%m.%Y'
RATE_REGEX = re.compile(r'^\d+%$')

# Requests
START_DATE = date.fromisoformat('2026-01-01')
DOC_TYPE = 'doc-invoice'
HEADERS = {
    'Accept': 'application/json',
}

# Threads
MAX_WORKERS = 5
TIMEOUT = 30
