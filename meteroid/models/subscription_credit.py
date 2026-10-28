# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class SubscriptionCredit(BaseModel):
    """Credit on account that only one subscription can use."""

    credit_on_account: int
    """In minor units of the wallet."""

    subscription_id: str
