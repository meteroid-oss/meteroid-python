# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .invoice_line_usage_breakdown_item import InvoiceLineUsageBreakdownItem


@dataclasses.dataclass(kw_only=True)
class InvoiceLineUsageBreakdown(BaseModel):
    """The `InvoiceLineUsageBreakdown` object."""

    items: list[InvoiceLineUsageBreakdownItem]
    """Largest amount first. Past 99 values, the rest are summed in one last item flagged `others`."""

    key: str
    """The event property the usage is broken down by, e.g. `project_id`."""
