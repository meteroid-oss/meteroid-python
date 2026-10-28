# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .actor_type import ActorType


@dataclasses.dataclass(kw_only=True)
class Actor(BaseModel):
    """Who made a change."""

    type: ActorType
    """USER, CUSTOMER, API_KEY, OAUTH_APP or SYSTEM."""

    id: str | None = None
    """The user's id (`usr_…`) for USER, the customer's (`cus_…`) for CUSTOMER, the API key's
    or app's for API_KEY and OAUTH_APP; absent for SYSTEM."""
