# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class CreditUnitPriceSetRequest(BaseModel):
    """The new price of one credit in a currency."""

    unit_price: str
    """Major units of the currency per credit, as a decimal string: positive, at most 12 decimal
    places."""
