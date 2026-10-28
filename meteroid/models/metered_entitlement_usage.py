# this file is @generated
from __future__ import annotations

import dataclasses
from datetime import datetime
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class MeteredEntitlementUsage(BaseModel):
    """The `MeteredEntitlementUsage` object."""

    consumed: Decimal | None = None

    limit_reached: bool | None = None
    """Switched on, but refused: the `BLOCK` limit (plus its grace) is reached, so `enabled` is
    false until the window resets. Never set for a limit grouped by a property."""

    remaining: Decimal | None = None

    reset_at: datetime | None = None
