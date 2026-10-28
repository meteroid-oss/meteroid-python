# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .budget import Budget
    from .pagination_response import PaginationResponse


@dataclasses.dataclass(kw_only=True)
class BudgetListResponse(BaseModel):
    """The `BudgetListResponse` object."""

    data: list[Budget]

    pagination_meta: PaginationResponse
