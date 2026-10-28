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
class WalletCreditUnrecoveredEventData(BaseModel):
    """Purchased credit was already spent when its money came back."""

    cause: str
    """`PAYMENT_DISPUTED` (lost to a dispute or chargeback), `PAYMENT_REVERSED` (a failed
    collection clawed back), `PAYMENT_REFUNDED` (a payment refunded without a credit note, at
    the provider or as an overpayment, after the credit it backed was spent) or
    `CREDIT_NOTE_REFUNDED`."""

    credit_taken_back: int
    """Unspent credit taken back from the wallet at the same time, in minor units."""

    credit_unrecovered: int
    """Spent credit this event adds to the loss, in minor units. A failed collection reopens its
    invoice, which collects it again; a dispute's loss stays unless the dispute is won.
    `wallet.credit_recovered` reports what comes back."""

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
