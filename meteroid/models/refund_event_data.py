# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_note_id import CreditNoteId
    from .decline_kind import DeclineKind
    from .invoice_id import InvoiceId
    from .payment_status_enum import PaymentStatusEnum
    from .payment_transaction_id import PaymentTransactionId
    from .payment_type_enum import PaymentTypeEnum
    from .refund_mode import RefundMode
    from .reversal_kind import ReversalKind


@dataclasses.dataclass(kw_only=True)
class RefundEventData(BaseModel):
    """A refund row, or the payment that failed or was clawed back — the same shape the REST invoice
    exposes as a transaction. `reversal_reason` is deliberately absent: it is free provider text and is
    not carried on the outbox event."""

    amount: int

    amount_refunded: int

    amount_reversed: int

    currency: str

    payment_type: PaymentTypeEnum

    status: PaymentStatusEnum

    transaction_id: PaymentTransactionId

    credit_note_id: CreditNoteId | None = None

    decline_kind: DeclineKind | None = None

    error: str | None = None

    invoice_id: InvoiceId | None = None

    parent_transaction_id: PaymentTransactionId | None = None

    processed_at: datetime | None = None

    provider_transaction_id: str | None = None

    refund_mode: RefundMode | None = None

    reversal_kind: ReversalKind | None = None
