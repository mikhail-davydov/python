from datetime import date


def date_formatter(country_code: str):
    loc = {
        'ru': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr': '%d.%m.%Y',
        'pt': '%d-%m-%Y'
    }

    def get_format_by_country_code(date: date):
        try:
            return date.strftime(loc[country_code])
        except Exception:
            return date.isoformat()

    return get_format_by_country_code


date_ru = date_formatter('invalid')
# date_ru = date_formatter('ca')
today = date(2015, 12, 7)
print(date_ru(today))
