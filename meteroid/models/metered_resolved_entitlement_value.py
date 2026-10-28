# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .billable_metric_id import BillableMetricId
    from .entitlement_overage_behavior import EntitlementOverageBehavior
    from .reset_period import ResetPeriod


@dataclasses.dataclass(kw_only=True)
class MeteredResolvedEntitlementValue(BaseModel):
    """The `MeteredResolvedEntitlementValue` object."""

    enabled: bool

    metric_id: BillableMetricId

    reset_period: ResetPeriod

    type: t.Literal["METERED"] = "METERED"

    grace_pct: int | None = None
    """`BLOCK` only: usage allowed beyond the limit before it is refused, in percent of it."""

    group_by: str | None = None
    """Event property the limit applies to separately; usage is then the largest value's."""

    limit: Decimal | None = None

    overage_behavior: EntitlementOverageBehavior | None = None

    thresholds: list[int] | None = None
    """Percents of the limit at which an alert is sent, ascending."""

    warning_threshold_pct: int | None = None
    """Deprecated: the lowest of `thresholds`."""
