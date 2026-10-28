# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import date, datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .metric_usage import MetricUsage
    from .usage_cost import UsageCost


@dataclasses.dataclass(kw_only=True)
class UsageResponse(BaseModel):
    """The `UsageResponse` object."""

    period_end: date

    period_start: date

    usage: list[MetricUsage]

    computed_at: datetime | None = None
    """Beta: when `totals` and the metrics' `costs` were computed. These are present only when a
    subscription's current billing period is read (no `start_date` nor `end_date`) and its
    usage could be priced."""

    totals: list[UsageCost] | None = None
    """Beta: the sum of the metrics' `costs`, per currency or credit unit."""
