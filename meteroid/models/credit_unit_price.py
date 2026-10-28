# this file is @generated
from __future__ import annotations

import dataclasses
from datetime import datetime

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class CreditUnitPrice(BaseModel):
    """What one credit sells for in a currency. A price is never edited: setting a new one for the
    same currency archives it."""

    created_at: datetime
    """When the price was set."""

    currency: str
    """ISO 4217 code of the currency the unit sells in."""

    id: str
    """The price's id (`cup_…`)."""

    unit_price: str
    """Major units of `currency` per credit, as a decimal string (e.g. "0.001")."""

    archived_at: datetime | None = None
    """When a newer price, or its removal, replaced it; absent while active."""
