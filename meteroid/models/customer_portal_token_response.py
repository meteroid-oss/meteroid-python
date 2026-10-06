# this file is @generated
from __future__ import annotations

import dataclasses
from datetime import datetime

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class CustomerPortalTokenResponse(BaseModel):
    """The `CustomerPortalTokenResponse` object."""

    api_url: str
    """Base URL of the public REST API"""

    expires_at: datetime
    """When the token expires (RFC 3339)"""

    portal_link: str
    """Hosted customer portal URL, token included"""

    portal_url: str
    """Base URL of the customer portal"""

    token: str
    """JWT token for portal access"""
