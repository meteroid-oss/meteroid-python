# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class ExtraRecurringPricing(BaseModel):
    """The `ExtraRecurringPricing` object."""

    quantity: int

    type: t.Literal["EXTRA_RECURRING"] = "EXTRA_RECURRING"

    unit_price: Decimal
