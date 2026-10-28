# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .budget_behavior import BudgetBehavior


@dataclasses.dataclass(kw_only=True)
class PatchBudgetRequest(BaseModel):
    """The currency or credit unit, and the subscription, are fixed at creation."""

    expected_version: int
    """The `version` you read; a newer stored version is refused with 409."""

    amount: int | None | Unset = UNSET

    behavior: BudgetBehavior | None | Unset = UNSET

    thresholds: list[int] | None | Unset = UNSET
