# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .entitlement_overage_behavior import EntitlementOverageBehavior
    from .reset_period import ResetPeriod


@dataclasses.dataclass(kw_only=True)
class MeteredEntitlementValue(BaseModel):
    """The `MeteredEntitlementValue` object."""

    type: t.Literal["METERED"] = "METERED"

    enabled: bool | None = None
    """Per-entitlement kill switch. `false` means disabled."""

    grace_pct: int | None | Unset = UNSET
    """`BLOCK` only: usage allowed beyond the limit before it is refused, in percent of the
    limit (1 to 1000)."""

    group_by: str | None | Unset = UNSET
    """Event property the limit applies to separately, one limit per value (e.g. `user_id`)."""

    limit: Decimal | None | Unset = UNSET
    """Cap on usage. Null means unlimited."""

    overage_behavior: EntitlementOverageBehavior | None | Unset = UNSET

    reset_period: ResetPeriod | None = None

    thresholds: list[int] | None | Unset = UNSET
    """Percents of the limit (1 to 100, at most 10) at which an alert is sent, once per period:
    `entitlement.usage_threshold_reached`, or `entitlement.limit_reached` at 100. Requires a
    limit and a window that is not sliding."""

    warning_threshold_pct: int | None | Unset = UNSET
    """Deprecated: use `thresholds`. A single alert threshold, read only when `thresholds` is
    omitted; returned as the lowest of `thresholds`."""
