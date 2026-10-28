# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .customer_id import CustomerId


@dataclasses.dataclass(kw_only=True)
class AutoTopUpCapReachedEventData(BaseModel):
    """A spending cap stopped an automatic top-up."""

    attempted_amount: int
    """What the suppressed top-up would have charged, tax included once it was quoted (before
    tax when the cap stopped it before then). Caps are always money: for a credit unit wallet,
    `currency` is the customer's currency."""

    cap: int
    """The cap, tax included, in minor units of `currency`."""

    currency: str
    """The currency the cap and the charge are in (ISO 4217)."""

    customer_id: CustomerId

    period: str
    """`DAILY` (rolling day) or `MONTHLY` (calendar month, UTC)."""

    period_end: datetime
    """End of the capped period."""

    period_start: datetime
    """Start of the capped period."""
