# this file is @generated
from __future__ import annotations

import dataclasses
from datetime import datetime

from ..serialization import UNSET, BaseModel, Unset


@dataclasses.dataclass(kw_only=True)
class RecordInvoicePaymentRequest(BaseModel):
    """The `RecordInvoicePaymentRequest` object."""

    amount: int
    """The positive amount received, in minor units of the invoice currency (e.g. cents)."""

    paid_at: datetime | None | Unset = UNSET
    """When the payment was received, at most a day ahead. Defaults to the current time."""

    reference: str | None | Unset = UNSET
    """Reference for the external payment, such as a bank transfer ID."""
