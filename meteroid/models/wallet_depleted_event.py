# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .event_id import EventId
    from .event_type import EventType
    from .wallet_depleted_event_data import WalletDepletedEventData


@dataclasses.dataclass(kw_only=True)
class WalletDepletedEvent(BaseModel):
    """The `WalletDepletedEvent` object."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("wallet_depleted_event_data",)

    wallet_depleted_event_data: WalletDepletedEventData

    id: EventId

    timestamp: datetime

    type: EventType
