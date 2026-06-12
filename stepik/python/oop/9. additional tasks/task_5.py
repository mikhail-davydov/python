import functools
import re


class DomainException(Exception):
    pass


def _validate_domain(func):
    @functools.wraps(func)
    def wrapper(self, domain):
        if not re.match(rf'^[a-z]+\.[a-z]+$', domain, re.I):
            raise DomainException('Недопустимый домен, url или email')
        return func(self, domain)

    return wrapper


class Domain:
    @_validate_domain
    def __init__(self, domain):
        self.domain = domain

    @staticmethod
    def from_url(url):
        try:
            domain = re.findall(rf'^https?://([a-z]+\.[a-z]+)$', url, re.I)[0]
        except IndexError:
            raise DomainException('Недопустимый домен, url или email') from None
        return __class__(domain)

    @staticmethod
    def from_email(email):
        try:
            domain = re.findall(rf'^[a-z]+@([a-z]+\.[a-z]+)$', email, re.I)[0]
        except IndexError:
            raise DomainException('Недопустимый домен, url или email') from None
        return __class__(domain)

    def __str__(self):
        return self.domain


# alt

class Domain:
    _DOMAIN_PATTERN = r'(?P<domain>[a-zA-Z]+\.[a-zA-Z]+)'
    _URL_PATTERN = fr'https?://{_DOMAIN_PATTERN}'
    _EMAIL_PATTERN = fr'[a-zA-Z]+@{_DOMAIN_PATTERN}'

    def __init__(self, domain):
        self.domain = self._parse_domain(self._DOMAIN_PATTERN, domain)

    def __str__(self):
        return self.domain

    @staticmethod
    def _parse_domain(regex, address):
        match = re.fullmatch(regex, address)
        if not match:
            raise DomainException('Недопустимый домен, url или email')
        return match.group('domain')

    @classmethod
    def _from_domain(cls, domain):
        instance = object.__new__(cls)
        instance.domain = domain
        return instance

    @classmethod
    def from_url(cls, url):
        domain = cls._parse_domain(cls._URL_PATTERN, url)
        return cls._from_domain(domain)

    @classmethod
    def from_email(cls, email):
        domain = cls._parse_domain(cls._EMAIL_PATTERN, email)
        return cls._from_domain(domain)
