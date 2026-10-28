# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .credit_applies_to import CreditAppliesTo
    from .credit_cost_request import CreditCostRequest
    from .credit_grant_type import CreditGrantType
    from .currency import Currency
    from .product_id import ProductId


@dataclasses.dataclass(kw_only=True)
class CreateCreditGrantRequest(BaseModel):
    """Credit granted without charging or invoicing."""

    amount: int
    """Credit granted, in minor units of `currency`, or of `credit_unit` when set (e.g. 500000
    is 5,000.00 credits of a unit with precision 2). Positive."""

    type: CreditGrantType
    """PROMOTIONAL gives credit for free (a goodwill or marketing grant). PAID records credit
    the customer paid for outside of Meteroid: nothing is charged or invoiced, and the grant
    is shown as "Paid outside Meteroid". Usage paid with PAID currency credit is taxed on the
    invoice that bills it, so do not charge tax on the external sale of currency credit, or
    the customer is taxed twice. Credit in a credit unit is the exception: its usage is billed
    in credits, untaxed, so tax its sale as you would any other. Use a top-up to sell credit
    through Meteroid."""

    applicable_product_ids: list[ProductId] | None | Unset = UNSET
    """Restricts the credit to charges of these products; absent applies to every product.
    Combined with `applies_to`. Not available for credit units."""

    applies_to: CreditAppliesTo | None = None
    """ALL pays any charge on an invoice; USAGE only usage charges."""

    cost: CreditCostRequest | None | Unset = UNSET

    credit_unit: str | None | Unset = UNSET
    """Grants in this credit unit (its code) instead of a currency; excludes `currency`. Credit in
    a credit unit pays the usage priced in that unit, so `applies_to` must stay ALL."""

    currency: Currency | None | Unset = UNSET

    expires_at: datetime | None | Unset = UNSET
    """When unspent credit lapses; absent never expires."""

    priority: int | None | Unset = UNSET
    """Lower values are drawn first among grants of the same type that pay the same charges;
    defaults to 100."""

    reason: str | None | Unset = UNSET
    """Shown on the credit ledger."""

    reference: str | None | Unset = UNSET
    """Your own reference, e.g. a contract or support ticket. Required for PAID credit that cost
    more than zero when the customer's invoicing entity is in France: the number of the invoice
    or receipt for the payment, as French law requires a supporting document for every
    accounting entry. Refused with 400 when missing."""

    subscription_id: str | None | Unset = UNSET
    """The customer's subscription (`sub_…`) the credit belongs to: it pays only that
    subscription's charges and lapses when the subscription ends. It must not have ended,
    and its currency must be the grant's. Absent pays any of the customer's subscriptions."""
