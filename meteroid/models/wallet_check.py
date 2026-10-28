# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .currency import Currency


@dataclasses.dataclass(kw_only=True)
class WalletCheck(BaseModel):
    """Whether a customer may keep consuming what their prepaid credit pays for."""

    as_of: datetime
    """When `balance` was computed."""

    balance: int
    """The balance: credit on account net of the usage not invoiced yet that it will pay, in
    minor units of `currency` or `credit_unit`; never negative for the customer as a whole,
    as `balance` of `GET /wallets`. With `product_id`, only the credit that can pay for that
    product, net of its usage no credit covers. With `subscription_id`, only the credit that
    subscription can spend (credit restricted to products it is not charged for left out),
    net of its usage no credit covers; credit that belongs to no subscription counts in every
    subscription's balance (see `shared_balance`)."""

    exact: bool
    """Always false: `balance` may lag usage by a few seconds (see `as_of`), and the answer is
    cached for one second."""

    exhausted: bool
    """True once `balance` is at or below zero, or, with `subscription_id`, once no credit is
    left for some of its usage. Independent of `has_access`: a wallet that allows overage
    still reports this, so the caller can warn without refusing."""

    has_access: bool
    """False only once `balance` is at or below zero and `blocks_when_exhausted` is true.
    Customers without a wallet in `currency` do not prepay, and always have access. With
    `subscription_id`: false when `blocks_when_exhausted` is true and no credit that
    subscription can spend is left for some of its usage (of `product_id` when given), as the
    access gate refuses it; a subscription charged no usage in the wallet keeps access."""

    lag_ms: int
    """Age of `balance`, in milliseconds."""

    pauses_at_zero: bool
    """Whether usage is refused as soon as the credit is used up: the wallet's `usage_at_zero`,
    else the plan of the subscription checked (of any active subscription without one). A plan
    that invoices usage up to a cap refuses it past the cap only, as `has_access` reports."""

    credit_unit: str | None = None
    """The credit unit (its code) checked; absent for a currency."""

    credit_unit_precision: int | None = None
    """Decimal places of `credit_unit`: `balance` is in integers of 10^-precision credit."""

    currency: Currency | None = None

    shared_balance: int | None = None
    """With `subscription_id` only: the part of `balance` that belongs to no subscription, which
    the customer's other subscriptions can spend too."""
