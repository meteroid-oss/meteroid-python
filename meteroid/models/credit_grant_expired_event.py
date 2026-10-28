# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .credit_grant_expired_event_data import CreditGrantExpiredEventData
    from .event_id import EventId
    from .event_type import EventType


@dataclasses.dataclass(kw_only=True)
class CreditGrantExpiredEvent(BaseModel):
    """The `CreditGrantExpiredEvent` object."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("credit_grant_expired_event_data",)

    credit_grant_expired_event_data: CreditGrantExpiredEventData

    id: EventId

    timestamp: datetime

    type: EventType
