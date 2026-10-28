# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .billable_metric_id import BillableMetricId
    from .grouped_usage import GroupedUsage
    from .usage_cost import UsageCost


@dataclasses.dataclass(kw_only=True)
class MetricUsage(BaseModel):
    """The `MetricUsage` object."""

    grouped_usage: list[GroupedUsage]

    metric_code: str

    metric_id: BillableMetricId

    metric_name: str

    total_value: Decimal

    costs: list[UsageCost] | None = None
    """Beta: what the metric's usage adds so far to the subscription's next invoice, per currency
    or credit unit; empty while it bills nothing, as during a free trial or once cancelled."""
