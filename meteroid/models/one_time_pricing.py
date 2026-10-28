# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class OneTimePricing(BaseModel):
    """The `OneTimePricing` object."""

    quantity: int

    type: t.Literal["ONE_TIME"] = "ONE_TIME"

    unit_price: Decimal
