# this file is @generated
from __future__ import annotations

import dataclasses
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class InvoiceLineUsageBreakdownItem(BaseModel):
    """The `InvoiceLineUsageBreakdownItem` object."""

    amount_subtotal: int
    """Its part of the line's amount before discounts and tax, in minor units."""

    quantity: Decimal
    """Usage of this value, in the units the line is priced in."""

    credits_consumed: int | None = None
    """Its part of `credit_unit.consumed`, on a line priced in a credit unit."""

    others: bool | None = None
    """Set on the last item when there are more than 99 values: it sums the rest."""

    quoted_amount_subtotal: int | None = None
    """Its part of the tax-included amount quoted, on a line billed from tax-inclusive prices."""

    value: str | None = None
    """The property's value; absent for events without it, and for `others`."""
