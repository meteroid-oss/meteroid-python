# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_pack_expiry import CreditPackExpiry
    from .credit_pack_rollover import CreditPackRollover
    from .credit_pack_unit import CreditPackUnit


@dataclasses.dataclass(kw_only=True)
class CreditFee(BaseModel):
    """A credit pack: charged like a fixed fee, it grants `credit_amount` × `quantity` of credit once
    paid, in the subscription currency or in `credit_unit`. A zero `unit_price` makes it credit
    included with the plan (promotional). A currency pack priced below its credit grants the price
    paid as paid credit and the difference as promotional bonus credit, which applies before tax."""

    credit_amount: Decimal
    """Credit granted per pack, in major units of the subscription currency, or a number of
    credits of `credit_unit` when set."""

    quantity: int
    """Packs billed and granted each time."""

    type: t.Literal["CREDIT"] = "CREDIT"

    unit_price: Decimal
    """Price of one pack, in major units of the subscription currency."""

    credit_unit: CreditPackUnit | None = None

    expiry: CreditPackExpiry | None = None

    once: bool | None = None
    """When true, billed and granted once, on the subscription's first invoice, instead of every
    period."""

    rollover: CreditPackRollover | None = None
