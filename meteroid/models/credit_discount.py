# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .coupon_credit_scope import CouponCreditScope


@dataclasses.dataclass(kw_only=True)
class CreditDiscount(BaseModel):
    """Promotional credit added to the customer's credit balance when the subscription the coupon is
    redeemed on starts. It never discounts an invoice and applies before tax. A customer redeems
    it at most once, so the coupon cannot be `reusable`. Its code is case-insensitive: it is stored
    upper-case and redeemed whatever the case."""

    amount: str
    """Credit added per redemption, in major units (e.g. "25.00")."""

    currency: str
    """ISO 4217 code; it must match the currency of the subscription the coupon is redeemed on."""

    type: t.Literal["CREDIT"] = "CREDIT"

    expires_in_days: int | None | Unset = UNSET
    """Days the credit stays spendable after redemption, 1 to 3660. Absent: it never expires."""

    scope: CouponCreditScope | None = None
    """CUSTOMER (default): the credit pays any of the customer's subscriptions. SUBSCRIPTION: the
    credit pays only the subscription the code is redeemed on, and ends with it."""
