# this file is @generated
from __future__ import annotations

import dataclasses
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class InvoiceLineCreditUnit(BaseModel):
    """How a usage line priced in a credit unit was paid: the credits it consumed, those the
    customer's balance in the unit covered, and the rate the rest was billed at."""

    code: str
    """The credit unit's code, e.g. `CREDITS`."""

    consumed: int
    """Credits the usage priced."""

    covered: int
    """Of which paid by the customer's credit wallet."""

    precision: int
    """Credit amounts are integers in 10^-precision credit."""

    rate: Decimal
    """Invoice-currency major units per credit."""

    unit_price: Decimal | None = None
    """Credits per usage unit."""
