# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .billable_metric_id import BillableMetricId
    from .billing_period_enum import BillingPeriodEnum
    from .capacity_threshold import CapacityThreshold
    from .plan_fee_credit_unit import PlanFeeCreditUnit


@dataclasses.dataclass(kw_only=True)
class CapacityPlanFee(BaseModel):
    """Capacity-based fee with included committed usage and overage"""

    cadence: BillingPeriodEnum

    metric_id: BillableMetricId

    thresholds: list[CapacityThreshold]

    type: t.Literal["CAPACITY"] = "CAPACITY"

    credit_unit: PlanFeeCreditUnit | None | Unset = UNSET
