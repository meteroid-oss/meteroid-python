# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .license_signing_key import LicenseSigningKey
    from .licensing_endpoints import LicensingEndpoints


@dataclasses.dataclass(kw_only=True)
class LicenseSigningKeysResponse(BaseModel):
    """The `LicenseSigningKeysResponse` object."""

    endpoints: LicensingEndpoints

    keys: list[LicenseSigningKey]
    """Active key first. The first key is created on first issue."""
