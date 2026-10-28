# this file is @generated
from __future__ import annotations

import dataclasses
from datetime import date

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class BudgetPeriod(BaseModel):
    """The `BudgetPeriod` object."""

    start: date

    end: date | None = None
    """Absent when the period never ends."""
