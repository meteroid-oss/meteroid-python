# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .event_id import EventId
    from .event_type import EventType
    from .wallet_recovered_event_data import WalletRecoveredEventData


@dataclasses.dataclass(kw_only=True)
class WalletRecoveredEvent(BaseModel):
    """The `WalletRecoveredEvent` object."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("wallet_recovered_event_data",)

    wallet_recovered_event_data: WalletRecoveredEventData

    id: EventId

    timestamp: datetime

    type: EventType
