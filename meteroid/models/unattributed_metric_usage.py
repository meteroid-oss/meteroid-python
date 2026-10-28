# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime
from decimal import Decimal

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .billable_metric_id import BillableMetricId


@dataclasses.dataclass(kw_only=True)
class UnattributedMetricUsage(BaseModel):
    """A metric's usage over `[from, until)` that no subscription bills: it matches none of the
    usage filters of the subscriptions pricing the metric, and none of them bills without one."""

    _JSON_KEYS: t.ClassVar[t.Mapping[str, str]] = {
        "from_": "from",
    }

    from_: datetime

    metric_code: str

    metric_id: BillableMetricId

    metric_name: str

    total_value: Decimal

    until: datetime
