# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class LicensingEndpoints(BaseModel):
    """The public endpoints your installations talk to."""

    activate_url: str

    events_url: str

    jwks_url: str

    refresh_url: str
