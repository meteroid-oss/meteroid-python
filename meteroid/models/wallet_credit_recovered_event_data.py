# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_note_id import CreditNoteId
    from .customer_id import CustomerId
    from .invoice_id import InvoiceId
    from .payment_transaction_id import PaymentTransactionId


@dataclasses.dataclass(kw_only=True)
class WalletCreditRecoveredEventData(BaseModel):
    """Spent credit reported by `wallet.credit_unrecovered` is backed again."""

    cause: str
    """Cause of the loss this recovers: `PAYMENT_DISPUTED`, `PAYMENT_REVERSED`,
    `PAYMENT_REFUNDED` or `CREDIT_NOTE_REFUNDED`."""

    credit_recovered: int
    """Spent credit an earlier `wallet.credit_unrecovered` reported that is backed again, in
    minor units: the money came back, or the credit was returned and taken back."""

    credit_unrecovered_total: int
    """The loss of this money flow (an invoice's payments, a credit note, or a payment) once
    this event applies."""

    customer_id: CustomerId

    credit_note_id: CreditNoteId | None = None

    credit_unit: str | None = None
    """The credit unit (its code) the amounts are in; absent for a currency."""

    credit_unit_precision: int | None = None
    """Decimal places of `credit_unit`: amounts are integers of 10^-precision credit."""

    currency: str | None = None
    """Absent when the amounts are in a credit unit."""

    invoice_id: InvoiceId | None = None

    payment_id: PaymentTransactionId | None = None
