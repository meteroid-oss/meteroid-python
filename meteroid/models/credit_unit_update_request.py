# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import UNSET, BaseModel, Unset


@dataclasses.dataclass(kw_only=True)
class CreditUnitUpdateRequest(BaseModel):
    """Partial update: an absent field is left unchanged. `code` and `precision` have no field here,
    they are immutable. `symbol` set to `null` clears it."""

    archived: bool | None | Unset = UNSET
    """Blocks the unit from new prices, packs and grants; existing ones keep working."""

    name: str | None | Unset = UNSET
    """Singular display name, 1 to 64 characters."""

    plural_name: str | None | Unset = UNSET
    """Plural display name, 1 to 64 characters."""

    product_id: str | None | Unset = UNSET
    """The product sales of the unit are booked under; `null` clears it, which stops the unit
    from being sold."""

    symbol: str | None | Unset = UNSET
    """Validated by the store (trimmed, at most 8 characters) rather than here: `validator` has
    no built-in support for a double `Option`."""
