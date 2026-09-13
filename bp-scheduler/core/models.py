import logging
import time
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Any

import requests

START_DATE = date.fromisoformat('2026-01-01')
DOC_TYPE = 'doc-invoice'
HEADERS = {
    'Accept': 'application/json',
}
MIN_WAIT_TIME = 0.5


@dataclass
class Settings:
    db: str | None = None
    api_key: str | None = None
    firm: str | None = None


@dataclass
class Item:
    Object: str | None = None
    Type: str | None = None
    Date: str | None = None
    Name: str | None = None
    Sum: str | None = None
    Firm: str | None = None
    Partner: str | None = None
    PaymentSum: str | None = None
    PacketGroup: str | None = None
    PacketGroupFirst: str | None = None
    TagDesc: str | None = None


@dataclass
class Invoice:
    Object: str | None = None
    Type: str | None = None
    Firm: str | None = None
    FirmCargo: str | None = None
    Partner: str | None = None
    PartnerCargo: str | None = None
    Date: str | None = None
    Name: str | None = None
    Num: int | None = None
    Curr: str | None = None
    ByCurr: bool | None = None
    SumMethod: str | None = None
    Precision: str | None = None
    Sum: Decimal | None = None
    Mark: bool | None = None
    State: str | None = None
    Note: str | None = None

    def __init__(
            self,
            Object: str | None = None,
            Type: str | None = None,
            Firm: str | None = None,
            FirmCargo: str | None = None,
            Partner: str | None = None,
            PartnerCargo: str | None = None,
            Date: str | None = None,
            Name: str | None = None,
            Num: int | None = None,
            Curr: str | None = None,
            ByCurr: bool | None = None,
            SumMethod: str | None = None,
            Precision: str | None = None,
            Sum: Decimal | None = None,
            Mark: bool | None = None,
            State: str | None = None,
            Note: str | None = None,
            **kwargs,
    ):
        # Игнорируем неизвестные поля через **kwargs
        self.Object = Object
        self.Type = Type
        self.Firm = Firm
        self.FirmCargo = FirmCargo
        self.Partner = Partner
        self.PartnerCargo = PartnerCargo
        self.Date = Date
        self.Name = Name
        self.Num = Num
        self.Curr = Curr
        self.ByCurr = ByCurr
        self.SumMethod = SumMethod
        self.Precision = Precision
        self.Sum = Sum
        self.Mark = Mark
        self.State = State
        self.Note = Note


class Request:
    def __init__(self, api_key: str, db: str, firm: str):
        super().__init__()
        self._init_page = 0
        self._firm = firm
        self._auth = {
            'Authorization': f'Bearer {api_key}',
        }
        self._archive_url = f'https://5.375.ru/bpo-api/v1/{db}/archive'
        self._invoice_url = f'https://5.375.ru/bpo-api/v1/{db}/doc-invoice/'

    def get_all_invoices(self) -> list[Item]:
        all_items = []

        params = {
            'page': self._init_page,
            'type': DOC_TYPE,
            'firm': self._firm,
            'date_start': START_DATE.isoformat(),
        }

        total_count, items = self._get_response_items(params)
        logging.info(f'Get {len(items)} items from {total_count}, page {params.get('page', self._init_page) + 1}')
        while items:
            all_items.extend(items)
            set_page = {
                'page': params.get('page', self._init_page) + 1,
            }
            params.update(set_page)
            _, items = self._get_response_items(params)
            logging.info(f'Get {len(items)} items from {total_count}, page {params.get('page', self._init_page) + 1}')

        return [Item(**item) for item in all_items]

    def get_invoice(self, invoice):
        headers_with_auth = dict(**HEADERS, **self._auth)
        response: dict = self.make_request(
            self._invoice_url + invoice,
            None,
            headers_with_auth,
        )

        logging.info(f'invoice {response=}')
        return Invoice(**response)

    @staticmethod
    def make_request(url, params, headers):
        logging.info(f'{url=}, {params=}')
        response = requests.get(
            url=url,
            params=params,
            headers=headers,
        )

        requests_left = int(response.headers.get('X-RateLimit-Remaining'))
        if requests_left == 0:
            reset_timestamp = int(response.headers.get('X-RateLimit-Reset'))
            current_time = time.time()
            wait_time = reset_timestamp - current_time
            logging.info(f'calculated {wait_time=}')
            should_wait = max(MIN_WAIT_TIME, abs(wait_time))
            logging.info(f'No requests left, wait {should_wait:.2f}s for reset rate limit')
            time.sleep(should_wait)

        if response.status_code == 429:
            logging.info(f'{response.status_code=}, {response.reason=}, {response.headers=}')
            raise RuntimeError('Hit rate limit, should never happen')

        return response.json()

    def _get_response_items(self, params):
        headers_with_auth = dict(**HEADERS, **self._auth)
        response: dict = self.make_request(
            self._archive_url,
            params,
            headers_with_auth,
        )

        items: list[Any] = response.get('items', [])
        total_count = response.get('total_count', None)
        return total_count, items
