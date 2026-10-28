# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .event_id import EventId
    from .event_type import EventType
    from .wallet_credit_unrecovered_event_data import WalletCreditUnrecoveredEventData


@dataclasses.dataclass(kw_only=True)
class WalletCreditUnrecoveredEvent(BaseModel):
    """The `WalletCreditUnrecoveredEvent` object."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("wallet_credit_unrecovered_event_data",)

    wallet_credit_unrecovered_event_data: WalletCreditUnrecoveredEventData

    id: EventId

    timestamp: datetime

    type: EventType
