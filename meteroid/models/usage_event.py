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
class UsageEvent(BaseModel):
    """The `UsageEvent` object."""

    id: str

    properties: dict[str, str]

    timestamp: datetime

    cost: UsageCost | None = None

    quantity: Decimal | None = None
    """Billed units the event adds. Absent when the metric's aggregation cannot be split per
    event, or when the event does not count towards the metric."""
