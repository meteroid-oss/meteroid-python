# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .actor import Actor
    from .credit_applies_to import CreditAppliesTo
    from .credit_grant_id import CreditGrantId
    from .credit_note_id import CreditNoteId
    from .customer_id import CustomerId
    from .invoice_id import InvoiceId
    from .ledger_entry_id import LedgerEntryId


@dataclasses.dataclass(kw_only=True)
class WalletDebitedEventData(BaseModel):
    """Credit left a customer's wallet."""

    amount: int
    """In minor units of `currency` or `credit_unit`."""

    applicable_product_ids: list[str]
    """The products whose charges the grant pays; empty when it pays every product."""

    applies_to: CreditAppliesTo
    """What the grant pays: ALL any charge, USAGE only usage charges."""

    credit_grant_id: CreditGrantId
    """The grant the credit left."""

    customer_id: CustomerId

    ledger_entry_id: LedgerEntryId
    """The credit ledger entry recording the movement."""

    reason: str
    """Why the credit moved, as shown on the ledger."""

    actor: Actor | None = None

    credit_note_id: CreditNoteId | None = None

    credit_unit: str | None = None
    """The credit unit (its code) the amounts are in; absent for a currency."""

    credit_unit_precision: int | None = None
    """Decimal places of `credit_unit`: amounts are integers of 10^-precision credit."""

    currency: str | None = None
    """Absent when the amounts are in a credit unit."""

    invoice_id: InvoiceId | None = None

    subscription_id: str | None = None
    """The subscription the grant belongs to: it pays only that subscription's charges. Null when
    it pays any of the customer's subscriptions."""
