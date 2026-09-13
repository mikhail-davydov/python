from datetime import date

### Common
WARN_NOTIFICATION_DAYS = None
NOTE_FIELDS_COUNT = 3
SPLIT_BY = ','
DATE_FORMAT = '%d.%m.%Y'

### Requests
START_DATE = date.fromisoformat('2026-01-01')
DOC_TYPE = 'doc-invoice'
HEADERS = {
    'Accept': 'application/json',
}
MIN_WAIT_TIME = 0.5
