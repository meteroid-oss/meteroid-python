# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .customer_id import CustomerId


@dataclasses.dataclass(kw_only=True)
class WalletBalanceLowEventData(BaseModel):
    """A wallet's balance fell below one of its low-balance thresholds."""

    balance: int
    """The balance when it fell below `threshold`, in minor units: the wallet's `balance`, all
    its credit on account net of the unbilled usage it pays, including credit that belongs to
    a subscription or is limited to usage or products. Sent once per crossing, for the lowest
    threshold crossed; it re-arms once the balance is back at the threshold. Because that
    credit counts here and not in `wallet.depleted`, a wallet can be depleted without this
    event firing."""

    customer_id: CustomerId

    threshold: int
    """The low-balance threshold crossed, in the same minor units."""

    credit_unit: str | None = None
    """The credit unit (its code) the amounts are in; absent for a currency."""

    credit_unit_precision: int | None = None
    """Decimal places of `credit_unit`: amounts are integers of 10^-precision credit."""

    currency: str | None = None
    """Absent when the amounts are in a credit unit."""

    shared_balance: int | None = None
    """The part of `balance` that pays any charge of any subscription: what automatic top-ups
    refill and `wallet.depleted` watches. Absent on events recorded before it was reported."""
