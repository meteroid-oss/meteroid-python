# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .usage_event import UsageEvent


@dataclasses.dataclass(kw_only=True)
class UsageEventListResponse(BaseModel):
    """The `UsageEventListResponse` object."""

    data: list[UsageEvent]

    next_cursor: str | None = None
    """Absent on the last page."""
