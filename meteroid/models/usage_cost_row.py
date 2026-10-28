# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime
from decimal import Decimal

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .usage_cost import UsageCost


@dataclasses.dataclass(kw_only=True)
class UsageCostRow(BaseModel):
    """The `UsageCostRow` object."""

    bucket_start: datetime

    exact: bool
    """False when the price depends on the whole period's usage (tiered, volume, package,
    capacity): the cost is then what the bucket adds to the period's price so far. A period's
    rows still add up to its invoiced amount."""

    quantity: Decimal

    cost: UsageCost | None = None

    group: str | None = None
    """The value of `group_by` for the row. Absent when the request is not grouped, or the usage
    has no value for the property."""
