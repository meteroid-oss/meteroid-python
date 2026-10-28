# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_unit import CreditUnit


@dataclasses.dataclass(kw_only=True)
class CreditUnitListResponse(BaseModel):
    """The tenant's credit units."""

    data: list[CreditUnit]
