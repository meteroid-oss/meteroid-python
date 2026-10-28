# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .event_id import EventId
    from .event_type import EventType
    from .wallet_balance_low_event_data import WalletBalanceLowEventData


@dataclasses.dataclass(kw_only=True)
class WalletBalanceLowEvent(BaseModel):
    """The `WalletBalanceLowEvent` object."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("wallet_balance_low_event_data",)

    wallet_balance_low_event_data: WalletBalanceLowEventData

    id: EventId

    timestamp: datetime

    type: EventType
