# this file is @generated
from __future__ import annotations

import dataclasses
from datetime import datetime

from ..serialization import UNSET, BaseModel, Unset


@dataclasses.dataclass(kw_only=True)
class AmendEventRequest(BaseModel):
    """The `AmendEventRequest` object."""

    properties: dict[str, str]
    """The corrected properties. They replace the stored ones."""

    timestamp: datetime
    """RFC 3339 timestamp of the corrected event.
    Must be between 24 hours ago and 1 hour from now. Set `allow_backfilling` to remove the past limit."""

    allow_backfilling: bool | None | Unset = UNSET
    """Allow a timestamp more than 1 day in the past. Defaults to `false`."""

    customer_alias: str | None | Unset = UNSET
    """External customer alias of the event. Set this or `customer_id`."""

    customer_id: str | None | Unset = UNSET
    """Meteroid customer ID of the event. Set this or `customer_alias`."""
