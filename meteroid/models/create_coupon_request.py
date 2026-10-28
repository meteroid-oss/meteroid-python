# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .coupon_discount import CouponDiscount
    from .plan_id import PlanId


@dataclasses.dataclass(kw_only=True)
class CreateCouponRequest(BaseModel):
    """The `CreateCouponRequest` object."""

    code: str
    """1 to 64 ASCII letters, digits, hyphens or underscores. A promotional-credit (`CREDIT`) code
    is stored upper-case. Codes are matched as described on `Coupon.code`."""

    discount: CouponDiscount

    description: str | None | Unset = UNSET

    expires_at: datetime | None | Unset = UNSET

    plan_ids: list[PlanId] | None = None

    recurring_value: int | None | Unset = UNSET

    redemption_limit: int | None | Unset = UNSET

    reusable: bool | None = None
    """Whether one customer may redeem the coupon more than once. Must be false for a
    promotional-credit (`CREDIT`) coupon."""
