# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_cap import CreditCap


@dataclasses.dataclass(kw_only=True)
class CreditCaps(BaseModel):
    """The `CreditCaps` object."""

    caps: list[CreditCap]
    """One per denomination; usage charged in a denomination without a cap pauses at zero."""

    type: t.Literal["invoice_up_to"] = "invoice_up_to"
