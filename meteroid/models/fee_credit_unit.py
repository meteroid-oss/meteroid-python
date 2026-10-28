# this file is @generated
from __future__ import annotations

import dataclasses
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class FeeCreditUnit(BaseModel):
    """The credit unit a usage fee's amounts are expressed in, with its value in the subscription
    currency."""

    code: str
    """The credit unit's code, e.g. `CREDITS`."""

    credit_unit_id: str
    """The credit unit's id (`cun_…`)."""

    precision: int
    """Decimal places of the unit: credit balances and ledger amounts in it are integers of
    10^-precision credit."""

    rate: Decimal
    """Subscription-currency major units per credit: the money billed, before tax, for each
    credit the customer's balance in the unit does not cover."""
