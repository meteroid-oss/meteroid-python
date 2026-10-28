# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_applies_to import CreditAppliesTo
    from .credit_cost import CreditCost
    from .currency import Currency
    from .ledger_entry_type import LedgerEntryType


@dataclasses.dataclass(kw_only=True)
class LedgerEntry(BaseModel):
    """One movement of a customer's credit."""

    amount: int
    """Signed change to the credit on account, in minor units."""

    applies_to: CreditAppliesTo
    """What the moved credit's grant pays: ALL any charge, USAGE only usage charges."""

    balance_after: int
    """The credit on account after this entry, whatever it applies to."""

    credit_grant_id: str
    """The grant the credit moved in or out of."""

    effective_at: datetime
    """When the movement took effect; the ledger is ordered by it."""

    id: str
    """The entry's id (`wle_…`)."""

    reason: str
    """Why the credit moved, as shown on the ledger."""

    recorded_at: datetime
    """When the movement was recorded."""

    sequence: int
    """Position within the currency's ledger in the order the movements took effect, from 1. A
    movement recorded later with an earlier date shifts the positions after it: identify an
    entry by its `id`."""

    type: LedgerEntryType
    """What moved the credit."""

    cost: CreditCost | None = None

    credit_note_id: str | None = None
    """The credit note that gave the credit back or took it back."""

    credit_unit: str | None = None
    """The credit unit (its code) the amounts are in; absent for a currency."""

    credit_unit_precision: int | None = None
    """Decimal places of `credit_unit`: amounts are integers of 10^-precision credit."""

    currency: Currency | None = None

    invoice_id: str | None = None
    """The invoice the credit was applied to, bought on, or given back by."""

    reference: str | None = None
    """Your own reference, e.g. a contract or support ticket."""

    subscription_id: str | None = None
    """The subscription the moved credit's grant belongs to; null when it pays any of the
    customer's subscriptions."""
