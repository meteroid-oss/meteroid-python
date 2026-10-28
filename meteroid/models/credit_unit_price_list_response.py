# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_unit_price import CreditUnitPrice


@dataclasses.dataclass(kw_only=True)
class CreditUnitPriceListResponse(BaseModel):
    """A credit unit's selling prices, newest first."""

    data: list[CreditUnitPrice]
