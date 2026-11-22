# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import date

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .plan_version_id import PlanVersionId
    from .scheduled_event_id import ScheduledEventId
    from .scheduled_event_type import ScheduledEventType


@dataclasses.dataclass(kw_only=True)
class PendingScheduledEvent(BaseModel):
    """The `PendingScheduledEvent` object."""

    customer_initiated: bool

    event_type: ScheduledEventType

    id: ScheduledEventId

    scheduled_date: date
    """Date the event takes effect at the start of"""

    cancel_reason: str | None = None

    new_plan_name: str | None = None

    new_plan_version_id: PlanVersionId | None = None
