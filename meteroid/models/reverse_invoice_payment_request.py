# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .reversal_kind import ReversalKind


@dataclasses.dataclass(kw_only=True)
class ReverseInvoicePaymentRequest(BaseModel):
    """The `ReverseInvoicePaymentRequest` object."""

    kind: ReversalKind
    """`CHARGEBACK`, `DEBTOR_RECALL` and `DISPUTE` leave the invoice paid and mark the payment
    disputed. Any other kind makes the amount due again."""

    reason: str | None | Unset = UNSET
    """Additional details about the reversal."""

    reversed_at: datetime | None | Unset = UNSET
    """When the reversal occurred, at most a day ahead. Defaults to the current time."""
