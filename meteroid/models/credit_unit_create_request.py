# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import UNSET, BaseModel, Unset


@dataclasses.dataclass(kw_only=True)
class CreditUnitCreateRequest(BaseModel):
    """A new credit unit."""

    code: str
    """Immutable once created: 4 to 16 characters, A-Z/0-9/_, starting with a letter. Never an
    ISO currency code (those are always 3 letters)."""

    name: str
    """Singular display name, 1 to 64 characters, e.g. "Credit"."""

    plural_name: str
    """Plural display name, 1 to 64 characters, e.g. "Credits"."""

    precision: int
    """Immutable once created: 0 to 6."""

    symbol: str | None | Unset = UNSET
    """Short display symbol, at most 8 characters."""
