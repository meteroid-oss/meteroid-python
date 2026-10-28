# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class PerUnitPricing(BaseModel):
    """The `PerUnitPricing` object."""

    rate: Decimal

    type: t.Literal["PER_UNIT"] = "PER_UNIT"
