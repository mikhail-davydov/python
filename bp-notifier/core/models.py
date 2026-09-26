from collections import namedtuple

import datetime

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    api_key: str | None = Field(min_length=64, default=None)
    db: str | None = Field(min_length=32, default=None)
    firm: str | None = Field(min_length=12, default=None)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="forbid",
    )


class ArchiveItem(BaseModel):
    """
    Модель данных для архивных элементов.
    """

    object: str = Field(alias="Object")
    type: str = Field(alias="Type")
    date: datetime.date = Field(alias="Date")
    name: str = Field(alias="Name")
    sum: float = Field(alias="Sum")
    firm: str = Field(alias="Firm")
    partner: str = Field(alias="Partner")
    payment_sum: float = Field(alias="PaymentSum")
    packet_group: str | None = Field(alias="PacketGroup", default=None)
    packet_group_first: bool = Field(alias="PacketGroupFirst", default=False)
    tag_desc: str | None = Field(alias="TagDesc", default=None)


class InvoiceItem(BaseModel):
    """
    Модель данных для счетов (Invoice).
    """

    object: str = Field(alias="Object")
    type: str = Field(alias="Type")
    firm: str = Field(alias="Firm")
    firm_cargo: str = Field(alias="FirmCargo")
    partner: str = Field(alias="Partner")
    partner_cargo: str = Field(alias="Object")
    date: datetime.date = Field(alias="Date")
    name: str = Field(alias="Name")
    num: int = Field(alias="Num")
    curr: str = Field(alias="Curr")
    by_curr: float = Field(alias="ByCurr")
    sum_method: str = Field(alias="SumMethod")
    precision: int = Field(alias="Precision")
    sum: float = Field(alias="Sum")
    mark: bool = Field(alias="Mark")
    state: str = Field(alias="State")
    note: str | None = Field(alias="Note", default=None)


InvoiceNoteInfo = namedtuple('InvoiceNoteInfo', ['num', 'name', 'phone', 'date_to', 'error'])
