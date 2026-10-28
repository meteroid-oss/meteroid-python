# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .auto_top_up import AutoTopUp
    from .currency import Currency
    from .subscription_credit import SubscriptionCredit
    from .usage_at_zero import UsageAtZero


@dataclasses.dataclass(kw_only=True)
class Wallet(BaseModel):
    """A customer's credit in one currency or credit unit. Amounts are minor units of it. Read with
    `subscription_id`, every amount counts only the credit that subscription can use."""

    credit_on_account: int
    """The ledger total: credit granted and effective, not yet applied to an invoice or expired,
    whatever it applies to. Usage not invoiced yet is not deducted (see `balance`)."""

    credit_on_account_usage_only: int
    """The part of `credit_on_account` that pays only usage charges."""

    low_balance_thresholds: list[int]
    """Ascending, distinct, at most 5. `wallet.balance_low` fires once when `balance` falls below
    one; a drop below several at once fires once, for the lowest. All credit counts, including
    credit that belongs to a subscription or is limited to usage or products, which
    `wallet.depleted` leaves out: a wallet can be depleted without an alert firing."""

    pauses_at_zero: bool
    """Usage stops as soon as the credit is used up, for at least one active subscription: by
    `usage_at_zero`, or by the plan of a subscription charging usage in this wallet."""

    subscription_credit: list[SubscriptionCredit]
    """The part of `credit_on_account` that belongs to a subscription, which only that
    subscription's charges can use, per subscription. The rest pays any subscription."""

    upcoming_credit: int
    """Credit granted that takes effect later."""

    usage_at_zero: UsageAtZero
    """What this customer's usage does once the credit a subscription can use for it is used up
    (its own credit, credit that belongs to no subscription, and credit limited to the product:
    the `balance` of `GET /wallets/check`). `FOLLOW_PLAN` applies the "when credit runs out"
    rule of each subscription's plan."""

    as_of: datetime | None = None
    """When `balance` and `unbilled_usage` were computed. They follow usage within a few seconds
    while the balance is near zero or a threshold, and within a minute otherwise."""

    auto_top_up: AutoTopUp | None = None

    balance: int | None = None
    """What the customer has left: `credit_on_account` minus the part of `unbilled_usage` that
    credit will pay. Never negative: usage beyond the credit stays in `unbilled_usage`, to be
    invoiced. Low-balance alerts use it; automatic top-ups watch only its part that pays any
    charge (credit that belongs to no subscription and is not limited to usage or products).
    Absent, with `unbilled_usage` and `as_of`, until the customer's usage has been priced once.
    With `subscription_id`: the credit that subscription can spend once every subscription's
    unbilled usage is paid, minus its own unbilled usage no credit pays (negative then), as
    `GET /wallets/check` reads it. Credit restricted to products it is not charged for is
    left out. Credit that belongs to no subscription counts in the balance of every
    subscription that can use it (see `shared_balance`): never add subscriptions' balances up."""

    credit_unit: str | None = None
    """The credit unit (its code) the wallet holds; absent for a currency."""

    credit_unit_precision: int | None = None
    """Decimal places of `credit_unit`: amounts are integers of 10^-precision credit."""

    currency: Currency | None = None

    shared_balance: int | None = None
    """With `subscription_id` only: the part of `balance` that belongs to no subscription, which
    the customer's other subscriptions can spend too."""

    unbilled_usage: int | None = None
    """Usage recorded and priced but not invoiced yet, tax included, in minor units: what the
    next invoices will charge for it, paid from credit as far as the credit goes. With
    `subscription_id`, that subscription's usage only; other subscriptions' usage paid from
    shared credit still lowers `balance`."""

    unit_price: str | None = None
    """Credit unit wallets: the price this customer agreed for one credit, in major units of
    `unit_price_currency`, as a decimal string (e.g. "0.0008"). Purchases and automatic
    top-ups in that currency charge it instead of the list price, unless a purchase sets its
    own `unit_price`. Absent: the list price applies."""

    unit_price_currency: Currency | None = None
