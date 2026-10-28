# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_unit_price import CreditUnitPrice


@dataclasses.dataclass(kw_only=True)
class CreditUnit(BaseModel):
    """A tenant-defined denomination usage can be priced or credit granted in, instead of money.
    `code` and `precision` are immutable once created."""

    archived: bool
    """Archived units take no new prices, packs or grants; existing ones keep working."""

    code: str
    """Upper-case code naming the unit in wallets, grants and webhooks, e.g. `CREDITS`."""

    id: str
    """The unit's id (`cun_…`)."""

    name: str
    """Singular display name, e.g. "Credit"."""

    plural_name: str
    """Plural display name, e.g. "Credits"."""

    precision: int
    """Minor-unit exponent: amounts of this unit are integers of 10^-precision credit."""

    prices: list[CreditUnitPrice]
    """The active selling prices, one per currency."""

    product_id: str | None = None
    """The product sales of this unit are booked under: their tax category and accounting code.
    The unit can be sold (top-ups) only once it is set."""

    symbol: str | None = None
    """Short display symbol, e.g. "cr"."""
