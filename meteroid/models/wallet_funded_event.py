# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .event_id import EventId
    from .event_type import EventType
    from .wallet_funded_event_data import WalletFundedEventData


@dataclasses.dataclass(kw_only=True)
class WalletFundedEvent(BaseModel):
    """The `WalletFundedEvent` object."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("wallet_funded_event_data",)

    wallet_funded_event_data: WalletFundedEventData

    id: EventId

    timestamp: datetime

    type: EventType
