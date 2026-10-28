# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class SlotFee(BaseModel):
    """The `SlotFee` object."""

    initial_slots: int

    type: t.Literal["SLOT"] = "SLOT"

    unit: str

    unit_rate: Decimal

    max_slots: int | None = None

    min_slots: int | None = None
