# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime
from decimal import Decimal

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .config_value import ConfigValue
    from .entitlement_check_feature import EntitlementCheckFeature
    from .entitlement_check_limit import EntitlementCheckLimit
    from .entitlement_check_period import EntitlementCheckPeriod
    from .entitlement_check_reason import EntitlementCheckReason


@dataclasses.dataclass(kw_only=True)
class EntitlementCheck(BaseModel):
    """Whether a customer may consume more of a feature now."""

    as_of: datetime
    """When the usage behind the answer was measured."""

    exact: bool
    """Always false: the answer reflects usage up to `as_of`."""

    feature: EntitlementCheckFeature

    has_access: bool

    in_overage: bool
    """The entitlement allows overage (`ALLOW`) and the requested units go beyond its limit:
    access is granted, and the overage is billed."""

    lag_ms: int
    """Age of that usage, in milliseconds."""

    limits: list[EntitlementCheckLimit]
    """Deprecated: always empty. Customer-specific limits are entitlement overrides, reported in
    `used`, `limit` and `remaining`."""

    near_limit: bool
    """True when a hard limit is within 5% of being reached, reached, or refuses the request.
    While true, check before every request with its actual `requested`, and do not cache an
    answer that grants access."""

    reason: EntitlementCheckReason

    limit: Decimal | None = None

    period: EntitlementCheckPeriod | None = None

    remaining: Decimal | None = None
    """Units left before the limit, grace excluded: 0 while `has_access` is true when usage is
    within the grace allowance."""

    retry_after_ms: int | None = None
    """When to check again, in milliseconds. After a refusal by a limit whose period ends within
    24 hours: the time until it ends (a smaller `requested` may still be allowed sooner);
    absent after a refusal by a sliding window, whose usage leaves it gradually. While
    `near_limit` is true and access is granted: 1000."""

    used: Decimal | None = None
    """`used`, `limit`, `remaining` and `period` report the entitlement's limit. Absent when the
    entitlement has no limit."""

    value: ConfigValue | None = None
