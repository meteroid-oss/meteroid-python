# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .billable_metric_id import BillableMetricId
    from .billing_metric_aggregate_enum import BillingMetricAggregateEnum


@dataclasses.dataclass(kw_only=True)
class MetricSummary(BaseModel):
    """The `MetricSummary` object."""

    aggregation_type: BillingMetricAggregateEnum

    code: str

    created_at: datetime

    id: BillableMetricId

    name: str

    aggregation_key: str | None = None

    archived_at: datetime | None = None

    description: str | None = None

    unit_plural: str | None = None
    """What several units of the metric are called, e.g. `tokens`."""

    unit_singular: str | None = None
    """What one unit of the metric is called, e.g. `token`."""
