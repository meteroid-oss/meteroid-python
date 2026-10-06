# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .entitlement import Entitlement


@dataclasses.dataclass(kw_only=True)
class EntitlementListResponse(BaseModel):
    """The `EntitlementListResponse` object."""

    data: list[Entitlement]
