# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_expiry_unit import CreditExpiryUnit


@dataclasses.dataclass(kw_only=True)
class CreditPackExpiry(BaseModel):
    """How long funded credit stays spendable. BILLING_PERIOD takes value 1."""

    unit: CreditExpiryUnit
    """DAY, MONTH or BILLING_PERIOD."""

    value: int
    """How many days or months; 1 for BILLING_PERIOD."""
