# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .entitlement_check_limit_behavior import EntitlementCheckLimitBehavior
    from .usage_limit_id import UsageLimitId


@dataclasses.dataclass(kw_only=True)
class EntitlementCheckLimit(BaseModel):
    """Deprecated: customer usage limits were replaced by entitlement overrides; never returned."""

    behavior: EntitlementCheckLimitBehavior

    has_access: bool

    limit: Decimal

    remaining: Decimal

    usage_limit_id: UsageLimitId

    used: Decimal

    group: dict[str, str] | None = None
    """The group the limit was evaluated for, when the limit is grouped."""
