# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class CreditExhaustedRuleInvoiceVariant(BaseModel):
    """Usage beyond the credit is invoiced."""

    type: t.Literal["invoice"] = "invoice"
