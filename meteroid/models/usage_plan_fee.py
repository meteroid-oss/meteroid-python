# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .billable_metric_id import BillableMetricId
    from .billing_period_enum import BillingPeriodEnum
    from .plan_fee_credit_unit import PlanFeeCreditUnit
    from .plan_usage_pricing_model import PlanUsagePricingModel


@dataclasses.dataclass(kw_only=True)
class UsagePlanFee(BaseModel):
    """Usage-based fee"""

    cadence: BillingPeriodEnum

    metric_id: BillableMetricId

    pricing: PlanUsagePricingModel

    type: t.Literal["USAGE"] = "USAGE"

    credit_unit: PlanFeeCreditUnit | None | Unset = UNSET
