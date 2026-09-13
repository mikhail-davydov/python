from typing import Any, Dict


class BaseItem:
    """
    Базовый класс для моделей данных с конвертацией полей.
    Автоматически преобразует поля из PascalCase (API) в snake_case (Python).
    """

    _FIELD_MAP: Dict[str, str] = {}

    def __init__(self, **kwargs):
        for api_key, python_key in self._FIELD_MAP.items():
            setattr(self, python_key, kwargs.get(api_key))

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, BaseItem):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def to_dict(self) -> Dict[str, Any]:
        """Преобразует объект обратно в словарь."""
        return self.__dict__.copy()


class ArchiveItem(BaseItem):
    """
    Модель данных для архивных элементов.
    """

    _FIELD_MAP = {
        "Object": "object",
        "Type": "type",
        "Date": "date",
        "Name": "name",
        "Sum": "sum",
        "Firm": "firm",
        "Partner": "partner",
        "PaymentSum": "payment_sum",
        "PacketGroup": "packet_group",
        "PacketGroupFirst": "packet_group_first",
        "TagDesc": "tag_desc",
    }


class InvoiceItem(BaseItem):
    """
    Модель данных для счетов (Invoice).
    """

    _FIELD_MAP = {
        "Object": "object",
        "Type": "type",
        "Firm": "firm",
        "FirmCargo": "firm_cargo",
        "Partner": "partner",
        "PartnerCargo": "partner_cargo",
        "Date": "date",
        "Name": "name",
        "Num": "num",
        "Curr": "curr",
        "ByCurr": "by_curr",
        "SumMethod": "sum_method",
        "Precision": "precision",
        "Sum": "sum",
        "Mark": "mark",
        "State": "state",
        "Note": "note",
    }
