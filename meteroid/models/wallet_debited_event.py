# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .event_id import EventId
    from .event_type import EventType
    from .wallet_debited_event_data import WalletDebitedEventData


@dataclasses.dataclass(kw_only=True)
class WalletDebitedEvent(BaseModel):
    """The `WalletDebitedEvent` object."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("wallet_debited_event_data",)

    wallet_debited_event_data: WalletDebitedEventData

    id: EventId

    timestamp: datetime

    type: EventType
