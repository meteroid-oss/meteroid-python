# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import date

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .unattributed_metric_usage import UnattributedMetricUsage


@dataclasses.dataclass(kw_only=True)
class UnattributedUsageResponse(BaseModel):
    """The `UnattributedUsageResponse` object."""

    period_end: date

    period_start: date

    usage: list[UnattributedMetricUsage]
