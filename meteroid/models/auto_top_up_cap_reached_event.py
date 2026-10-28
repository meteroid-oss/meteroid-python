# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .auto_top_up_cap_reached_event_data import AutoTopUpCapReachedEventData
    from .event_id import EventId
    from .event_type import EventType


@dataclasses.dataclass(kw_only=True)
class AutoTopUpCapReachedEvent(BaseModel):
    """The `AutoTopUpCapReachedEvent` object."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("auto_top_up_cap_reached_event_data",)

    auto_top_up_cap_reached_event_data: AutoTopUpCapReachedEventData

    id: EventId

    timestamp: datetime

    type: EventType
