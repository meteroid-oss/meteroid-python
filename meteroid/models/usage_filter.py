# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class UsageFilter(BaseModel):
    """Restricts the customer's usage events a subscription bills to those whose `property` equals
    `value` (for example `api_key` = `key-A`). Among the customer's subscriptions pricing the same
    metric, one with a usage filter bills the events matching it (an event two filters match goes
    to the older subscription); one without bills the events matching no other subscription's
    filter. Two subscriptions without a usage filter both bill every such event. Events matching
    no filter while every subscription pricing their metric has one are billed by none and
    reported as unattributed usage."""

    property: str
    """Event property name, e.g. `api_key`."""

    value: str
    """Value the property must have."""
