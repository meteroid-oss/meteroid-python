# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .calendar_unit import CalendarUnit


@dataclasses.dataclass(kw_only=True)
class SlidingWindowResetPeriod(BaseModel):
    """Always ends at now — e.g. 30 days means the last 30 days, old usage drops off automatically.
    A sliding window has no reset moment (`reset_at` is absent) and sends no threshold or
    limit-reached webhooks; it is enforced by the entitlement check."""

    interval: int

    type: t.Literal["SLIDING_WINDOW"] = "SLIDING_WINDOW"

    unit: CalendarUnit
