# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class CreditPackUnit(BaseModel):
    """The credit unit a credit pack grants."""

    code: str
    """The credit unit's code, e.g. `CREDITS`."""

    credit_unit_id: str
    """The credit unit's id (`cun_…`)."""

    precision: int
    """Decimal places of the unit: credit balances and ledger amounts in it are integers of
    10^-precision credit."""
