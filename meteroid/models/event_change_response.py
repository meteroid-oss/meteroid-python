# this file is @generated
from __future__ import annotations

import dataclasses
from datetime import datetime

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class EventChangeResponse(BaseModel):
    """The `EventChangeResponse` object."""

    ingested_at: datetime
    """RFC 3339 stamp of the queued change, with nanoseconds. Changes to the same event resolve by
    this stamp: the latest wins."""
