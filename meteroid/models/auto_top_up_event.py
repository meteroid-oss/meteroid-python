# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .auto_top_up_event_data import AutoTopUpEventData
    from .event_id import EventId
    from .event_type import EventType


@dataclasses.dataclass(kw_only=True)
class AutoTopUpEvent(BaseModel):
    """The `AutoTopUpEvent` object."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("auto_top_up_event_data",)

    auto_top_up_event_data: AutoTopUpEventData

    id: EventId

    timestamp: datetime

    type: EventType
