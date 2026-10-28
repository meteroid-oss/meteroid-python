# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .budget_author import BudgetAuthor
    from .budget_behavior import BudgetBehavior
    from .budget_period import BudgetPeriod
    from .currency import Currency


@dataclasses.dataclass(kw_only=True)
class Budget(BaseModel):
    """A spending limit for one currency, set by you or by the customer, with alerts at percentages
    of it. It counts the customer's whole spend, or one subscription's. A HARD budget also refuses
    access once reached. A budget never charges the customer."""

    amount: int
    """In minor units of the currency or credit unit."""

    behavior: BudgetBehavior

    created_at: datetime

    created_by: BudgetAuthor

    exact: bool
    """Always false: the estimate prices usage that is not yet invoiced."""

    id: str

    thresholds: list[int]
    """Percentages of the amount at which an alert is sent."""

    updated_at: datetime

    version: int
    """Send it back as `expected_version` when patching."""

    archived_at: datetime | None = None

    as_of: datetime | None = None
    """When `estimated_spend` was last measured."""

    credit_unit: str | None = None
    """The credit unit (its code) whose usage the budget counts; absent for a currency."""

    credit_unit_precision: int | None = None
    """Decimal places of `credit_unit`: amounts are integers of 10^-precision credit."""

    currency: Currency | None = None

    estimated_spend: int | None = None
    """Spend in the current billing period, including usage not invoiced yet, in minor units.
    Absent until first measured."""

    period: BudgetPeriod | None = None

    subscription_id: str | None = None
    """The subscription whose spend the budget counts; null when it counts the whole customer's."""
