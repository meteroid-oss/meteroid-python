# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .event_id import EventId
    from .event_type import EventType
    from .refund_event_data import RefundEventData


@dataclasses.dataclass(kw_only=True)
class PaymentEvent(BaseModel):
    """The `PaymentEvent` object."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("refund_event_data",)

    refund_event_data: RefundEventData

    id: EventId

    timestamp: datetime

    type: EventType
