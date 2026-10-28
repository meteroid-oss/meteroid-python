# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .usage_cost_unit import UsageCostUnit


@dataclasses.dataclass(kw_only=True)
class UsageCost(BaseModel):
    """Usage priced as its invoice line prices it, before discounts and credits: tax-inclusive when
    the subscription's prices are."""

    amount: Decimal

    currency: str
    """A currency code, or a credit unit code when `unit` is `CREDIT_UNIT`."""

    unit: UsageCostUnit
