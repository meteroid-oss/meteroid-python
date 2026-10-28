# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .usage_cost_row import UsageCostRow


@dataclasses.dataclass(kw_only=True)
class UsageCostListResponse(BaseModel):
    """The `UsageCostListResponse` object."""

    data: list[UsageCostRow]
