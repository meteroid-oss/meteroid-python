# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class FixedDiscount(BaseModel):
    """The `FixedDiscount` object."""

    amount: str

    currency: str

    type: t.Literal["FIXED"] = "FIXED"
