# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class CapacityPricing(BaseModel):
    """The `CapacityPricing` object."""

    included: int

    overage_rate: Decimal

    rate: Decimal

    type: t.Literal["CAPACITY"] = "CAPACITY"
