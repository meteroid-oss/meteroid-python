# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class CreditCap(BaseModel):
    """The `CreditCap` object."""

    amount: int
    """Usage beyond the credit invoiced per billing period, in minor units of `denomination`."""

    denomination: str
    """A currency or credit unit code."""
