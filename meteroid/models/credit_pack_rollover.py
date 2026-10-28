# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .credit_pack_expiry import CreditPackExpiry


@dataclasses.dataclass(kw_only=True)
class CreditPackRollover(BaseModel):
    """Unspent included credit carried once into a new grant when it expires, spent before the next
    period's credit."""

    expiry: CreditPackExpiry
    """Term of the rolled credit from the original expiry: DAY or MONTH."""

    max_amount: Decimal | None | Unset = UNSET
    """Cap per pack, in the pack's credit; absent carries all that is left."""
