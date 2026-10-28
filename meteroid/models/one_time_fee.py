# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class OneTimeFee(BaseModel):
    """The `OneTimeFee` object."""

    quantity: int

    rate: Decimal

    type: t.Literal["ONE_TIME"] = "ONE_TIME"
