from __future__ import annotations
import dataclasses
import decimal
import typing as t
import uuid
from datetime import date
from werkzeug.http import http_date

def _default(o: t.Any) -> t.Any:
    """Default JSON serializer for types that aren't supported by default."""
    if isinstance(o, date):
        return http_date(o)
    if isinstance(o, (decimal.Decimal, uuid.UUID)):
        return str(o)
    if dataclasses.is_dataclass(o):
        return dataclasses.asdict(o)
    if hasattr(o, "__html__"):
        return str(o.__html__())
    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")