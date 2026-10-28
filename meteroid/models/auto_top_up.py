# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .auto_top_up_method import AutoTopUpMethod
    from .auto_top_up_status import AutoTopUpStatus


@dataclasses.dataclass(kw_only=True)
class AutoTopUp(BaseModel):
    """Automatic top-up of the credit that applies to ALL charges: it charges the customer's payment
    method when the balance falls below `threshold`."""

    method: AutoTopUpMethod
    """FIXED buys `amount` each time; TO_TARGET buys back up to `target`."""

    status: AutoTopUpStatus
    """ACTIVE, DISABLED (terms kept) or SUSPENDED after repeated failed charges."""

    threshold: int
    """Tops up once the balance is at or below this, in minor units of the wallet."""

    amount: int | None = None
    """FIXED only: credit bought each time, in minor units of the wallet."""

    customer_consent_attested_at: datetime | None = None
    """When an operator attested that the customer agreed to automatic charges on exactly these
    terms. Absent when the customer confirmed them in their portal, or the terms changed since."""

    daily_cap: int | None = None
    """Most charged in a rolling day, tax included. For a credit unit wallet caps are money, in
    minor units of the customer's currency."""

    last_error: str | None = None
    """Why the last charge failed; may carry payment provider detail."""

    last_succeeded_at: datetime | None = None
    """The last charge that succeeded."""

    maximum: int | None = None
    """Largest single charge, in the same money as `minimum`."""

    minimum: int | None = None
    """Smallest single charge. For a credit unit wallet it is money (the price before tax, in
    minor units of the customer's currency), like the caps; the threshold, amount and target
    are credits."""

    monthly_cap: int | None = None
    """Most charged in a calendar month (UTC), tax included."""

    payment_method_id: str | None = None
    """Absent charges the customer's default payment method."""

    suspended_at: datetime | None = None
    """Set while SUSPENDED: since when."""

    target: int | None = None
    """TO_TARGET only: the balance a top-up brings the wallet back to, in minor units."""
