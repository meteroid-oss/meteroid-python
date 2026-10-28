# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .customer_id import CustomerId


@dataclasses.dataclass(kw_only=True)
class WalletRecoveredEventData(BaseModel):
    """A wallet's balance (credit that pays any charge of any of the customer's subscriptions, net of
    unbilled usage) came back above zero."""

    balance: int
    """The balance (credit on account that pays any charge of any of the customer's subscriptions,
    net of unbilled usage) now that it is back above zero, in
    minor units."""

    customer_id: CustomerId

    credit_unit: str | None = None
    """The credit unit (its code) the amounts are in; absent for a currency."""

    credit_unit_precision: int | None = None
    """Decimal places of `credit_unit`: amounts are integers of 10^-precision credit."""

    currency: str | None = None
    """Absent when the amounts are in a credit unit."""
