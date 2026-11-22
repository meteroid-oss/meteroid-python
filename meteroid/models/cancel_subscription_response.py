# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import date

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .pending_scheduled_event import PendingScheduledEvent
    from .subscription import Subscription


@dataclasses.dataclass(kw_only=True)
class CancelSubscriptionResponse(BaseModel):
    """The `CancelSubscriptionResponse` object."""

    pending_events: list[PendingScheduledEvent]
    """Changes still scheduled after this request, including the cancellation."""

    subscription: Subscription

    scheduled_cancellation_date: date | None = None
    """Date the subscription ends at the start of: its first day without service. Empty when the
    cancellation applied immediately."""
