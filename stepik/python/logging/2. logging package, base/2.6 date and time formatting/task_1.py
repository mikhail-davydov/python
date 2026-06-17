import logging

dt_formats = (
    '%F',
    '%x',
    '%d.%m.%Y'
)

for date_format in dt_formats:
    logging.basicConfig(format="%(asctime)s", datefmt=date_format, force=True)
    logging.warning("")