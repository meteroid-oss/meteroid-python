# this file is @generated
from __future__ import annotations

import dataclasses
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class PlanFeeCreditUnit(BaseModel):
    """The credit unit a plan's usage price is expressed in, with its value in the plan currency."""

    credit_unit_id: str
    """An active credit unit of the tenant (`GET /api/v1/credit-units`)."""

    rate: Decimal
    """Plan-currency major units per credit (e.g. "0.01"), positive: the money billed for each
    credit the customer's balance in the unit does not cover, before tax."""
