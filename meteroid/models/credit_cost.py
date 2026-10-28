# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .currency import Currency


@dataclasses.dataclass(kw_only=True)
class CreditCost(BaseModel):
    """Money in minor units of `currency`, net of tax."""

    amount: int
    """In minor units of `currency`."""

    currency: Currency
