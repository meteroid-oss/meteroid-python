# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .budget_behavior import BudgetBehavior
    from .currency import Currency


@dataclasses.dataclass(kw_only=True)
class CreateBudgetRequest(BaseModel):
    """The `CreateBudgetRequest` object."""

    amount: int
    """In minor units of the currency or credit unit."""

    behavior: BudgetBehavior | None | Unset = UNSET

    credit_unit: str | None | Unset = UNSET
    """A credit unit (its code): the budget counts the usage priced in that unit, in its minor
    units."""

    currency: Currency | None | Unset = UNSET

    subscription_id: str | None | Unset = UNSET
    """An active subscription of the customer (`sub_…`): the budget then counts only that
    subscription's spend, in its currency. Absent counts the whole customer's."""

    thresholds: list[int] | None | Unset = UNSET
    """Percentages of the amount (1 to 100, at most 10). Defaults to 50, 80 and 100."""
