# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class OfflineLicense(BaseModel):
    """The `OfflineLicense` object."""

    license: str
    """The signed license (a JWT) to install in the air-gapped installation."""
