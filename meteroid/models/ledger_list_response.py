# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .ledger_entry import LedgerEntry
    from .pagination_response import PaginationResponse


@dataclasses.dataclass(kw_only=True)
class LedgerListResponse(BaseModel):
    """A page of ledger entries, newest first."""

    data: list[LedgerEntry]

    pagination_meta: PaginationResponse
