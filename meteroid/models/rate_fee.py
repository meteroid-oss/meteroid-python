# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class RateFee(BaseModel):
    """The `RateFee` object."""

    rate: Decimal

    type: t.Literal["RATE"] = "RATE"
