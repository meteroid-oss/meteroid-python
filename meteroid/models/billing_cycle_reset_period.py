# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class BillingCycleResetPeriod(BaseModel):
    """Resets each time your subscription renews — anchored to your billing cycle."""

    type: t.Literal["BILLING_CYCLE"] = "BILLING_CYCLE"
