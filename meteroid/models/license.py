# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .customer_id import CustomerId
    from .license_id import LicenseId
    from .license_status import LicenseStatus
    from .subscription_id import SubscriptionId


@dataclasses.dataclass(kw_only=True)
class License(BaseModel):
    """The `License` object."""

    auto_issued: bool
    """Issued automatically for a subscription to a plan that issues licenses."""

    created_at: datetime

    customer_id: CustomerId

    customer_name: str

    has_activation_code: bool
    """Whether the activation code can still be retrieved: only until activation or revocation."""

    id: LicenseId

    offline: bool
    """Issued as a signed offline license: never activated nor refreshed."""

    revoked_immediately: bool
    """Revoked to stop at once: the installation drops its license on its next refresh instead
    of keeping it until it expires."""

    status: LicenseStatus

    validity_days: int
    """Lifetime of each license token the installation receives on refresh; for an offline
    license, the lifetime it was issued with."""

    instance_id: str | None = None
    """The installation the license is bound to, once activated."""

    last_refreshed_at: datetime | None = None

    plan_name: str | None = None

    revoked_at: datetime | None = None

    subscription_id: SubscriptionId | None = None
