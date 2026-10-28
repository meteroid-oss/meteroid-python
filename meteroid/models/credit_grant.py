# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_applies_to import CreditAppliesTo
    from .credit_cost import CreditCost
    from .credit_grant_kind import CreditGrantKind
    from .credit_grant_source import CreditGrantSource
    from .credit_grant_status import CreditGrantStatus
    from .credit_grant_type import CreditGrantType
    from .currency import Currency
    from .product_id import ProductId


@dataclasses.dataclass(kw_only=True)
class CreditGrant(BaseModel):
    """A lot of credit given to or bought by a customer. An invoice applies promotional currency
    credit before tax and paid credit after it. Within each, it draws the grants that belong to
    the invoiced subscription first, then grants restricted to products (the fewest products
    first), then usage-only grants, then the others; then by lowest `priority`, then the soonest
    to lapse."""

    amount: int
    """Amount granted, in minor units of `currency` or `credit_unit`."""

    applicable_product_ids: list[ProductId]
    """The products whose charges the credit pays, combined with `applies_to`; empty when it
    applies to every product."""

    applies_to: CreditAppliesTo
    """ALL pays any charge on an invoice; USAGE only usage charges."""

    created_at: datetime
    """When the grant was recorded."""

    effective_at: datetime
    """When the credit became spendable."""

    id: str
    """The grant's id (`cgr_…`)."""

    kind: CreditGrantKind
    """The group the grant is shown in: INCLUDED, PREPAID, BONUS or ACCOUNT_BALANCE."""

    kind_label: str
    """The group's name as Meteroid shows it: "Included with <plan>", "Purchased credit", "Free
    credit" or "Account balance"."""

    priority: int
    """Lower values are drawn first among grants of the same type that pay the same charges; 100
    by default."""

    reason: str
    """Shown on the credit ledger."""

    remaining: int
    """Not spent yet, in the same minor units."""

    source: CreditGrantSource
    """Where the credit came from."""

    status: CreditGrantStatus
    """PENDING until `effective_at`, then ACTIVE, DEPLETED once spent, or EXPIRED."""

    type: CreditGrantType
    """PAID or PROMOTIONAL: whether it applies after or before tax."""

    bonus_grant_id: str | None = None
    """Only on the response that created a PAID currency grant whose `cost` was below its
    amount: the PROMOTIONAL "Bonus credit" grant created beside it for the difference, with
    the same expiry, scope and priority."""

    cost: CreditCost | None = None

    cost_basis: str | None = None
    """`cost` per one major unit of credit, in major units of the cost currency (e.g. "0.008"),
    rounded to 12 decimal places, for display only."""

    credit_note_id: str | None = None
    """The credit note that gave the credit back."""

    credit_unit: str | None = None
    """The credit unit (its code) the amounts are in; absent for a currency."""

    credit_unit_precision: int | None = None
    """Decimal places of `credit_unit`: amounts are integers of 10^-precision credit."""

    currency: Currency | None = None

    ended_at: datetime | None = None
    """When the subscription the grant belongs to ended, if it ended. Unspent credit lapses then
    (status EXPIRED), even before `expires_at`."""

    expired_amount: int | None = None
    """Lost to expiry; present only on an expired grant."""

    expires_at: datetime | None = None
    """When unspent credit lapses; absent never expires."""

    invoice_id: str | None = None
    """The invoice that sold the credit, or whose void or negative total gave it back."""

    reference: str | None = None
    """Your own reference, e.g. a contract or support ticket."""

    subscription_id: str | None = None
    """The subscription the grant belongs to (`sub_…`): it pays only that subscription's
    charges, and lapses when the subscription ends. Null when it pays any of the customer's
    subscriptions."""
