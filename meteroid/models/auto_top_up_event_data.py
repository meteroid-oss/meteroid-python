# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .customer_id import CustomerId


@dataclasses.dataclass(kw_only=True)
class AutoTopUpEventData(BaseModel):
    """An automatic top-up charge failed, or the automatic top-up was suspended."""

    amount: int
    """The charge in minor units of `currency`: the credit it would have added, or for a credit
    unit wallet the price of those credits in the customer's currency. When the credits could
    not be priced (no selling price), the credits themselves, with `currency` the unit code. On
    a suspension after a top-up payment was refunded or disputed: that payment's top-up."""

    consecutive_failures: int
    """Failed charges in a row, this one included."""

    currency: str
    """The currency charged (ISO 4217), or the credit unit code when the credits had no price."""

    customer_id: CustomerId

    error: str
    """May carry payment provider detail."""

    suspended_at: datetime | None = None
    """Set on `wallet.auto_top_up_suspended`: when it was suspended."""
