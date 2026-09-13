import logging
import time
from abc import ABC, abstractmethod
from datetime import date
from typing import Any
from urllib.parse import urljoin

import requests

from core.constants import HEADERS, MIN_WAIT_TIME
from core.models import ArchiveItem, InvoiceItem


class Request:
    def __init__(self, api_key: str, db: str, firm: str):
        self._auth = {
            'Authorization': f'Bearer {api_key}',
        }
        self._db = db
        self._firm = firm

    @staticmethod
    def make_request(url: str, params: dict | None, headers: dict) -> dict:
        logging.info(f'{url=}, {params=}')
        response = requests.get(
            url=url,
            params=params,
            headers=headers,
        )

        requests_left = int(response.headers.get('X-RateLimit-Remaining') or '0')
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

    def _build_headers(self) -> dict:
        return dict(**HEADERS, **self._auth)


class ArchiveRequest(Request):
    def __init__(self, api_key: str, db: str, firm: str):
        super().__init__(api_key, db, firm)
        self._archive_url = f'https://5.375.ru/bpo-api/v1/{self._db}/archive'

    def get_full_doc_type_archive(self, doc_type: str, start_date: date, init_page: int = 0) -> list[ArchiveItem]:
        all_items = []

        params = {
            'page': init_page,
            'type': doc_type,
            'firm': self._firm,
            'date_start': start_date,
        }

        total_count, items = self._get_response_items(params)
        logging.info(f'Get {len(items)} items from {total_count}, page {params.get("page", init_page) + 1}')
        while items:
            all_items.extend(items)
            params['page'] = params.get('page', init_page) + 1
            _, items = self._get_response_items(params)
            logging.info(f'Get {len(items)} items from {total_count}, page {params.get("page", init_page) + 1}')

        return [ArchiveItem(**item) for item in all_items]

    def _get_response_items(self, params: dict) -> tuple[Any, list[Any]]:
        response: dict = self.make_request(
            self._archive_url,
            params,
            self._build_headers(),
        )

        items: list[Any] = response.get('items', [])
        total_count = response.get('total_count', None)
        return total_count, items


class DocTypeRequest(Request, ABC):
    @abstractmethod
    def get_item(self, invoice_id: str) -> InvoiceItem:
        ...


class DocInvoiceRequest(DocTypeRequest):
    def __init__(self, api_key: str, db: str, firm: str):
        super().__init__(api_key, db, firm)
        self._base_invoice_url = f'https://5.375.ru/bpo-api/v1/{self._db}/doc-invoice/'

    def get_item(self, invoice_id: str) -> InvoiceItem:
        invoice_url = urljoin(self._base_invoice_url, invoice_id)
        response: dict = self.make_request(
            invoice_url,
            None,
            self._build_headers(),
        )

        logging.info(f'invoice {response=}')
        return InvoiceItem(**response)
