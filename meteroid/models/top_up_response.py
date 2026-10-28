# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .currency import Currency
    from .top_up_status import TopUpStatus


@dataclasses.dataclass(kw_only=True)
class TopUpResponse(BaseModel):
    """Where a top-up stands. Its credit is granted once it is paid; `wallet.funded` reports it."""

    amount: int
    """Credit bought, in minor units of `currency`, or of `credit_unit` when set."""

    currency: Currency
    """The money the top-up is charged in."""

    status: TopUpStatus
    """SUCCEEDED once paid; otherwise what the payment is waiting for."""

    charged_amount: int | None = None
    """Charged to the payment method, tax included, in minor units of `currency`; absent until a
    charge is made."""

    checkout_url: str | None = None
    """Hosted page where the customer completes the payment; present while it awaits them."""

    credit_unit: str | None = None
    """Set when credits of this credit unit were bought: `amount` is in its minor units."""

    invoice_id: str | None = None
    """The invoice documenting the purchase."""

    payment_transaction_id: str | None = None
    """The charge made on the payment method; absent until a charge is made."""
