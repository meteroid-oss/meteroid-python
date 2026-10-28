# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_applies_to import CreditAppliesTo
    from .credit_grant_id import CreditGrantId
    from .credit_grant_lapse_reason import CreditGrantLapseReason
    from .customer_id import CustomerId
    from .ledger_entry_id import LedgerEntryId


@dataclasses.dataclass(kw_only=True)
class CreditGrantExpiredEventData(BaseModel):
    """A credit grant expired, or the subscription it belongs to ended, with credit left, which
    lapsed."""

    applicable_product_ids: list[str]
    """The products whose charges the grant pays; empty when it pays every product."""

    applies_to: CreditAppliesTo
    """What the grant pays: ALL any charge, USAGE only usage charges."""

    credit_grant_id: CreditGrantId
    """The grant that expired."""

    customer_id: CustomerId

    expired_amount: int
    """Unspent credit that lapsed, in minor units of `currency` or `credit_unit`."""

    expired_at: datetime
    """When the grant expired, or its subscription ended."""

    ledger_entry_id: LedgerEntryId
    """The credit ledger entry recording the expiry."""

    reason: CreditGrantLapseReason
    """SUBSCRIPTION_ENDED when the subscription the grant belongs to ended at or before the grant's
    expiry, EXPIRED otherwise."""

    credit_unit: str | None = None
    """The credit unit (its code) the amounts are in; absent for a currency."""

    credit_unit_precision: int | None = None
    """Decimal places of `credit_unit`: amounts are integers of 10^-precision credit."""

    currency: str | None = None
    """Absent when the amounts are in a credit unit."""

    subscription_id: str | None = None
    """The subscription the grant belongs to: it pays only that subscription's charges. Null when
    it pays any of the customer's subscriptions."""
