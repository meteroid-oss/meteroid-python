# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import UNSET, BaseModel, Unset


@dataclasses.dataclass(kw_only=True)
class IssueLicenseRequest(BaseModel):
    """The `IssueLicenseRequest` object."""

    customer_id: str
    """Customer ID or alias"""

    instance_id: str | None | Unset = UNSET
    """Offline only. The installation's id as it reports it, up to 255 characters without
    spaces: the license names it (`aud`) and stays bound to it. Without one, the license is
    not tied to an installation."""

    offline: bool | None = None
    """Delivers the license at once as a signed offline license, for an installation that
    can't reach the license server: no activation code, no refresh. Default: false."""

    subscription_id: str | None | Unset = UNSET
    """Ties the license to this subscription of the customer: it is renewed while the
    subscription is paid, and carries its plan's entitlements."""

    validity_days: int | None | Unset = UNSET
    """Online: lifetime of each license token the installation refreshes, 1 to 31 days.
    Default: 7. Offline: lifetime of the signed license, 1 to 400 days. Default: 365."""
