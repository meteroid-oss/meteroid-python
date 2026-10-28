# this file is @generated
from __future__ import annotations

import dataclasses
from datetime import datetime

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class EntitlementCheckPeriod(BaseModel):
    """The `EntitlementCheckPeriod` object."""

    start: datetime

    end: datetime | None = None
    """Absent when the period never ends."""
