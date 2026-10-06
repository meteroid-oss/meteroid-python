# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_note_id import CreditNoteId
    from .customer_payment_method_id import CustomerPaymentMethodId
    from .payment_method_info import PaymentMethodInfo
    from .payment_status_enum import PaymentStatusEnum
    from .payment_transaction_id import PaymentTransactionId
    from .payment_type_enum import PaymentTypeEnum
    from .refund_mode import RefundMode
    from .reversal_kind import ReversalKind


@dataclasses.dataclass(kw_only=True)
class Transaction(BaseModel):
    """The `Transaction` object."""

    amount: int

    amount_refunded: int
    """On a PAYMENT: how much was voluntarily given back (the sum of its settled REFUND
    children). The invoice stays paid — the Refund credit note is what reduces it."""

    amount_reversed: int
    """On a PAYMENT: how much was involuntarily clawed back (chargeback, bank recall, lost
    dispute). This is what the invoice nets out, reopening it."""

    currency: str

    id: PaymentTransactionId

    payment_type: PaymentTypeEnum

    status: PaymentStatusEnum

    credit_note_id: CreditNoteId | None = None

    error: str | None = None

    parent_transaction_id: PaymentTransactionId | None = None

    payment_method_id: CustomerPaymentMethodId | None = None

    payment_method_info: PaymentMethodInfo | None = None

    processed_at: datetime | None = None

    provider_transaction_id: str | None = None

    refund_mode: RefundMode | None = None

    reversal_kind: ReversalKind | None = None

    reversal_reason: str | None = None
    """The provider's raw cause, or what the operator typed when reversing by hand."""
