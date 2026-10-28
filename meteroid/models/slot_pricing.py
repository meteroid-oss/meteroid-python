# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import UNSET, BaseModel, Unset


@dataclasses.dataclass(kw_only=True)
class SlotPricing(BaseModel):
    """The `SlotPricing` object."""

    type: t.Literal["SLOT"] = "SLOT"

    unit_rate: Decimal

    max_slots: int | None | Unset = UNSET

    min_slots: int | None | Unset = UNSET
